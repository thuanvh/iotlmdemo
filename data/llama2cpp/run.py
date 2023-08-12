from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

template = """Question: {question}

Answer: Let's work this out in a step by step way to be sure we have the right answer."""

prompt = PromptTemplate(template=template, input_variables=["question"])

# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
# Verbose is required to pass to the callback manager

# Make sure the model path is correct for your system!
llm = LlamaCpp(
    model_path="../model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    #input={"temperature": 0.75, "max_length": 2000, "top_p": 1},
    callback_manager=callback_manager,
    verbose=True,
)

prompt = """
Question: A rap battle between Stephen Colbert and John Oliver
"""
print(prompt)
llm(prompt)
while True:
    question = input("Question:")
    prompt = """
Question: {}
"""
    prompt = prompt.format(question)
    print(prompt)
    llm(prompt)
