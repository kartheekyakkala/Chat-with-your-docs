from langchain_community.vectorstores.chroma import Chroma
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

def indexing_page(splits,inference_api_key):
    embeddings = HuggingFaceInferenceAPIEmbeddings(
    api_key=inference_api_key, model_name="meta-llama/Llama-2-7b")
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings())
    return vectorstore