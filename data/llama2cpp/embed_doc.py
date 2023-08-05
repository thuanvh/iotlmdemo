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
import argparse

def create_huggingface_embedding():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
                                            model_kwargs={'device':'cpu'}
                    )
    return embeddings

def embed_csv(file_path, embeddings, output_dir):
    loader = CSVLoader(file_path=file_path, encoding='utf-8', csv_args={
        'delimiter':','
    })
    data = loader.load()

    db = FAISS.from_documents(data, embeddings)
    db.save_local(output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog='ProgramName',
                        description='What the program does',
                        epilog='Text at the bottom of help')

    parser.add_argument('filename')           
    parser.add_argument('output_folder')      

    args = parser.parse_args()
    print(args.filename, args.output_folder)

    DB_FAISS_PATH = 'vectorstore/db_faiss_cpp'
    MODEL_PATH ="../model/llama-2-7b-chat.ggmlv3.q4_0.bin"

    embeddings = create_huggingface_embedding()

    # total arguments
    n = len(sys.argv)
    print("Total arguments passed:", n)
    
    # Arguments passed
    print("Name of input csv:", args.filename)
    embed_csv(args.filename, embeddings, args.output_folder)

    
