## Chat with your docs

Have you ever wondered, if there's a way to summarise your docs obtain answers from a knowledge base that may not be accessible to chat assistants? We've addressed that challenge for you! With "Chat-with-your-docs", you can simply upload your document or provide a website link. Our assistant will be able to answers based on the provided documents in no time. 

Don't forget to star our repository if liked it :) .

## Quick Install

Clone our repository:
```bash
git clone https://github.com/kartheekyakkala/Chat-with-your-docs.git
```

Clone our repository:
```bash
git clone https://github.com/kartheekyakkala/Chat-with-your-docs.git
```

Install poetry:
```bash
pip install poetry
```

Install dependencies:
```bash
poetry install
```
Thats'it you can run the main file to start chat.
```bash
poetry run python chat-with-your-docs/main.py
```

This repo uses LangChain as framework to integrate with open source LLM and Retreival Augmented Generation (RAG) Technique to add context from knowledge base as prompt to the LLM.
