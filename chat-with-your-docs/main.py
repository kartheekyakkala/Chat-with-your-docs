from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from getpass import getpass
from load import load_page, load_docs
from split import split_page
from indexing import indexing_page
from retrieve import retriever
from generate import generator

Huggingface_api_key = getpass()
repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
llm = HuggingFaceEndpoint(repo_id = repo_id, temperature = 0.5, max_new_tokens = 128, huggingfacehub_api_token = Huggingface_api_key)
page = "https://lilianweng.github.io/posts/2023-06-23-agent/"
print("Choose your Knowledge base: \n If your knowledge base is in the form of Documents, choose 1 \n If your knowledge base is a website choose 2.")
choice = int(input('Enter your choice:'))
if choice in [1,2]:
    if choice == 1:
        print("This assumes you have placed required files in chat-with-your-docs/data folder.")
        docs = load_docs("chat-with-your-docs/data")
    docs = load_page(page)
    splits  =  split_page(docs)
    vector_store = indexing_page(splits,Huggingface_api_key)
    retrieved  = retriever(vector_store)
    chain = generator(retrieved,llm)
    print(chain.invoke("What is Task Decomposition?"))
else:
    print("Wrong Choice!!!, start again.")