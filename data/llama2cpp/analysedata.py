import sys
from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import ConversationalRetrievalChain
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.embeddings import LlamaCppEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import AnalyzeDocumentChain


DB_FAISS_PATH = 'vectorstore/db_faiss'
MODEL_PATH ="../model/llama-2-7b-chat.ggmlv3.q4_0.bin"
DATA_FILE = sys.argv[1]
# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
# Verbose is required to pass to the callback manager

# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path=MODEL_PATH,
    input={"temperature": 0.75, "max_length": 2000, "top_p": 1},
    callback_manager=callback_manager,
    verbose=True,
)

with open(DATA_FILE) as f:
    state_of_the_union = f.read()

qa_chain = load_qa_chain(llm, chain_type="map_reduce")

qa_document_chain = AnalyzeDocumentChain(combine_docs_chain=qa_chain)

qa_document_chain.run(input_document=state_of_the_union, question="What is the GDP of China?")
