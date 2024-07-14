import os
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from langchain.llms.ollama import Ollama
from langchain.chains import LLMChain
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from src.prompt import *

def data_processing(filepath: str):
    file = filepath
    loader = PyPDFLoader(file)
    question_gen = ""

    data = loader.load()

    for page in data:
        question_gen += page.page_content

    
    splitter_ques_gen = TokenTextSplitter(
        
        chunk_size= 1000,
        chunk_overlap = 200
    )

    chunk_ques_gen = splitter_ques_gen.split_text(question_gen)
    document_ques_gen = [Document(page_content = t) for t in chunk_ques_gen]

    return document_ques_gen

def llm_pipeline(documents: Document):

    embedding_model = OllamaEmbeddings(model="mxbai-embed-large")
    vector_store = FAISS.from_documents(documents, embedding= embedding_model)
    questioning_model = Ollama(model="llama3")
    answering_model = Ollama(model = "llama3")
    PROMPT_QUESTION = PromptTemplate(template=questions_prompt_template, input_variables=["text"])
    question_chain = LLMChain(llm = questioning_model, verbose = True, prompt= PROMPT_QUESTION)
    llm_generated_questions = question_chain.invoke(documents)
    answering_chain = RetrievalQA.from_chain_type(llm=answering_model,chain_type="stuff",retriever=vector_store.as_retriever())
    answers = []
    for question in llm_generated_questions:
        answers = answers.append(answering_chain.invoke(question))

        

    return answers
    

