from langchain.agents import create_pandas_dataframe_agent
import pandas as pd
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
import seaborn as sns
import pyarrow as pa
import pyarrow.parquet as parquet
import pyarrow.feather as feather

file_data = "../pmfpdata/iot_pmfp_data.feather"
file_label = "../pmfpdata/iot_pmfp_labels.feather"
data_df = feather.read_feather(file_data)
DB_FAISS_PATH = 'vectorstore/db_faiss'
MODEL_PATH ="../model/llama-2-7b-chat.ggmlv3.q4_0.bin"



def create_agent():
    """
    Create an agent that can access and use a large language model (LLM).

    Args:
        filename: The path to the CSV file that contains the data.

    Returns:
        An agent that can access and use the LLM.
    """

    
    # Callbacks support token-wise streaming
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    # Verbose is required to pass to the callback manager

    # Make sure the model path is correct for your system!
    llm = LlamaCpp(
        model_path=MODEL_PATH,
        input={"temperature": 0.75, "max_length": 2000, "top_p": 1},
        callback_manager=callback_manager,
        verbose=True,
        n_ctx = 2048
    )

    # Read the CSV file into a Pandas DataFrame.
    df = [data_df, label_df]

    # Create a Pandas DataFrame agent.
    return create_pandas_dataframe_agent(llm, df, verbose=False)


def query_agent(agent, query):
    """
    Query an agent and return the response as a string.

    Args:
        agent: The agent to query.
        query: The query to ask the agent.

    Returns:
        The response from the agent as a string.
    """

    prompt = (
        """
            For the following query, if it requires drawing a table, reply as follows:
            {"table": {"columns": ["column1", "column2", ...], "data": [[value1, value2, ...], [value1, value2, ...], ...]}}

            If the query requires creating a bar chart, reply as follows:
            {"bar": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}
            
            If the query requires creating a line chart, reply as follows:
            {"line": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}
            
            There can only be two types of chart, "bar" and "line".
            
            If it is just asking a question that requires neither, reply as follows:
            {"answer": "answer"}
            Example:
            {"answer": "The title with the highest rating is 'Gilead'"}
            
            If you do not know the answer, reply as follows:
            {"answer": "I do not know."}
            
            Return all output as a string.
            
            All strings in "columns" list and data list, should be in double quotes,
            
            For example: {"columns": ["title", "ratings_count"], "data": [["Gilead", 361], ["Spider's Web", 5164]]}
            
            Lets think step by step.
            
            Below is the query.
            Query: 
            """
        + query
    )

    # Run the prompt through the agent.
    response = agent.run(prompt)
    
print(type(data_df))
print(data_df)

label_df = feather.read_feather(file_label)
print(label_df)
agent = create_agent()
query_agent(agent, "How many rows in the dataset?")
