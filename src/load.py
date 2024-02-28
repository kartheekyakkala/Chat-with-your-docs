import bs4
from langchain_community.document_loaders import WebBaseLoader

# Only keep post title, headers, and content from the full HTML.
def load_page(page):
    bs4_strainer = bs4.SoupStrainer(class_=("post-title", "post-header", "post-content"))
    loader = WebBaseLoader(
        web_paths=(page,),
        bs_kwargs={"parse_only": bs4_strainer},
    )
    docs = loader.load()
    return docs