import bs4
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader


# Only keep post title, headers, and content from the full HTML.
def load_page(page):
    loader = WebBaseLoader(page)
    docs = loader.load()
    return docs

def load_pdf(path):
    loader = PyPDFLoader(path)
    docs = loader.load()
    return docs