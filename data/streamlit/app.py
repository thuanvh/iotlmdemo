import streamlit as st
from streamlit_chat import message
import tempfile
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import ConversationalRetrievalChain

DB_FAISS_PATH = 'vectorstore/db_faiss'

def load_llm():
    llm = CTransformers(
        model = 'llama-2-7b-chat.ggmlv3.q4_0.bin',
        model_type = 'llama',
        max_new_tokens = 512,
        temperature = 0.5
    )
    return llm

st.title('Chat with csv using llama v2')
st.header('Chat with csv using ll')
st.markdown('<h3>AI chat</h3>', unsafe_allow_html=True)
uploaded_file = st.sidebar.file_uploader('Update data', type = 'csv')
print('hello')
if uploaded_file is not None:
    print('hello2')
    
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        temp_file_path = tmp_file.name
    print(temp_file_path)
    loader = CSVLoader(file_path=temp_file_path, encoding='utf-8', csv_args={
        'delimiter':','
    })
    data = loader.load()
    st.json(data)
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                       model_kwargs={'device':'cpu'}
                                       )
    db = FAISS.from_documents(data, embeddings)
    db.save_local(DB_FAISS_PATH)
    llm = load_llm()
    chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=db.as_retriever())
    
    def conversational_chat(query):
        print(query)
        result = chain({'question':query, 'chat_history':st.session_state['history']})
        print(result)
        st.session_state['history'].append((query,result['answer']))
        return result['answer']
    
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ['Hello, ask me anything about ' + uploaded_file.name]
        
    if 'past' not in st.session_state:
        st.session_state['past'] = ['Hey']
        
    # container for the chat history
    response_container = st.container()
    
    container = st.container()
    
    with container:
        with st.form(key='my_form', clear_on_submit=True):
            user_input = st.text_input('Query:', placeholder = 'Talk to your csv data',
                                       key = 'input')
            submit_button = st.form_submit_button(label='chat')
        if submit_button and user_input:
            print(user_input)
            output = conversational_chat(user_input)
            st.session_state['past'].append(user_input)
            st.session_state['generated'].append(output)
            
    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state['past'][i], is_user=True, key=str(i) + '_user', avatar_style='big-smile')
                message(st.session_state['generated'][i], key = str(i), avatar_style='thumbs')
