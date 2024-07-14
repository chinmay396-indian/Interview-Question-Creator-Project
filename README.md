# Interview Question Answer Generator App

Welcome to the Interview Question Answer Generator App! 🚀 This application is designed to help you prepare for interviews by generating thoughtful questions and providing accurate answers using advanced Large Language Models (LLMs). 

## Overview

This app leverages the latest advancements in Natural Language Processing (NLP) to extract content from PDF documents, generate interview questions, and retrieve answers. It’s perfect for job seekers, interview coaches, and anyone looking to enhance their interview preparation.

## Features

- PDF Upload and Content Extraction: Upload a PDF file and extract text content for question generation.
- Question Generation: Automatically generate insightful interview questions from the extracted content.
- Answer Retrieval: Retrieve accurate answers to the generated questions using sophisticated retrieval-based QA techniques.
- Customizable Prompt Templates: Tailor the question generation process with customizable prompt templates.

## Tech Stack

- Python: The primary programming language used for development.
- LangChain: A framework for building applications with LLMs.
  - Document Loaders: `PyPDFLoader` for loading PDF documents.
  - Text Splitters: `TokenTextSplitter` for managing text chunks.
  - LLM Models: `Ollama` LLMs for question generation and answering.
  - Embeddings: `OllamaEmbeddings` for creating vector representations of text.
  - Vector Stores: `FAISS` for efficient similarity search and retrieval.
  - Chains: `LLMChain` for question generation and `RetrievalQA` for answering questions.
  - Prompt Templates: `PromptTemplate` for customizing question prompts.

## How It Works

1. Upload PDF: Add your interview preparation material in PDF format.
2. Text Extraction: Extract text content from the PDF.
3. Generate Questions: Use LLMs to generate interview questions based on the text content.
4. Retrieve Answers: Retrieve answers to the questions using vector-based search and LLMs.
5. Review Results: View a list of questions and answers to aid in your interview preparation.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/your-username/interview-question-answer-generator-app.git
cd interview-question-answer-generator-app
pip install -r requirements.txt
