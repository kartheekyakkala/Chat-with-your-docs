from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from getpass import getpass
from load import load_page
from split import split_page
from indexing import indexing_page
from retrieve import retriever
from generate import generator

Huggingface_api_key = getpass()
repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
llm = HuggingFaceEndpoint(repo_id = repo_id, temperature = 0.5, max_new_tokens = 128, huggingfacehub_api_token = Huggingface_api_key)
page = "https://lilianweng.github.io/posts/2023-06-23-agent/"
docs = load_page(page)
splits  =  split_page(docs)
vector_store = indexing_page(splits,Huggingface_api_key)
retrieved  = retriever(vector_store)
chain = generator(retrieved,llm)
print(chain.invoke("What is Task Decomposition?"))