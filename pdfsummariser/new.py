import os
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
api_key=input("enter your Openai_api_key: ")
if api_key:
    llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=api_key)
    ploader = PyPDFLoader("job.pdf")
    pages = ploader.load()
    text = [p.page_content for p in pages]

    def summariser(text_list):
        return "\n".join(text_list)   # Join all pages together

    a = summariser(text)
    response = llm.invoke(f"Make all the text in a structured manner. Text follows:\n{a}\n\nGive it back in paragraphs.")
    print(response.content)
else:
    print("please set OPENAI_API_KEY environment variable")

    