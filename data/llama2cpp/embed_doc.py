import sys
from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.embeddings import LlamaCppEmbeddings
from langchain.document_loaders.csv_loader import CSVLoader


DB_FAISS_PATH = 'vectorstore/db_faiss_cpp'
MODEL_PATH ="../model/llama-2-7b-chat.ggmlv3.q4_0.bin"

# Callbacks support token-wise streaming
# callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
# Verbose is required to pass to the callback manager

# # Make sure the model path is correct for your system!
# llm = LlamaCpp(
#     model_path=MODEL_PATH,
#     input={"temperature": 0.75, "max_length": 2000, "top_p": 1},
#     callback_manager=callback_manager,
#     verbose=True,
# )
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                        model_kwargs={'device':'cpu'}
                )

# embeddings = LlamaCppEmbeddings(model_path=MODEL_PATH) 
# llm = LlamaCpp(model_path=MODEL_PATH)

def embed_csv(file_path, embedding):
    loader = CSVLoader(file_path=file_path, encoding='utf-8', csv_args={
        'delimiter':','
    })
    data = loader.load()
   
    db = FAISS.from_documents(data, embeddings)
    db.save_local(DB_FAISS_PATH)

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of data:", sys.argv[1])
embed_csv(sys.argv[1], embeddings)

# db = FAISS.load_local(DB_FAISS_PATH, embeddings)


# chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=db.as_retriever())

# template = """Question: {question}

# Answer: Let's work this out in a step by step way to be sure we have the right answer."""

# prompt = PromptTemplate(template=template, input_variables=["question"])


# prompt = """
# Question: A rap battle between Stephen Colbert and John Oliver
# """
# llm(prompt)

# history = []
# def conversational_chat(query):
#     print(query)
#     result = chain({'question':query, 
#                     'chat_history':history})
#     print(result)
#     history.append((query,result['answer']))
#     return result['answer']
# conversational_chat("What is the GDP of China?")
