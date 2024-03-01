def retriever(vectorstore):
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})
    # retrieved_docs = retriever.invoke("What are the approaches to Task Decomposition?")
    return retriever