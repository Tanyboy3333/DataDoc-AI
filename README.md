# 🦙 DataDoc AI – AI-Powered Document Q&A Chatbot

Welcome to **DataDoc AI**, an intelligent web application that allows you to upload a document and interact with it through a conversational chatbot powered by state-of-the-art Large Language Models (LLMs). Simply upload your document and start asking questions — the AI will respond with accurate, contextually relevant answers.

This project leverages powerful AI APIs and frameworks, including:

✅ **Gradio** – for building an interactive web interface  
✅ **LlamaParse** – for parsing and extracting content from various file formats  
✅ **Cohere Embeddings** – for semantic representation of document content  
✅ **Groq LLM** – for fast, accurate language model inference  
✅ **LlamaIndex** – for creating and querying an index of your document  
✅ **Render.com** – for deploying the web application

---

## ✨ Key Features

- Upload a document and parse its contents automatically
- Supports multiple file formats: `.pdf`, `.docx`, `.doc`, `.txt`, `.csv`, `.xlsx`, `.pptx`, `.html`, `.jpg`, `.png`, `.webp`, `.svg`
- Converts parsed content into semantic embeddings using **Cohere**
- Stores embeddings in a **vector index** using **LlamaIndex**
- Queries the index using a fast **Groq-powered LLM** to answer user questions
- Chatbot interface with **streaming responses**
- Beautiful, modern UI powered by **Gradio**
- Fully deployable as a **web service on Render.com**

---

## 📁 Project Structure

```bash
├── app.py               # Main Python application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation


🖼️ System Overview

Here’s how the system works end-to-end:

1. User uploads a document → file saved temporarily

2. Document parsed by LlamaParse depending on its file type

3. Parsed text embedded using CohereEmbedding

4. Embeddings stored in a VectorStoreIndex

5. User asks a question → query passed to query engine

6. Groq LLM generates an answer from the indexed embeddings

7. Streaming response displayed in the chat interface





📝 Full Workflow

1) Upload a document: user uploads a .pdf, .docx, .txt, etc.

2) Document parsed: LlamaParse extracts readable content into Markdown

3) Embedding created: CohereEmbedding turns content into semantic vectors

4) Index created: VectorStoreIndex stores those embeddings

5) Chat interface enabled: Gradio chatbot interface becomes active

6) User queries: typed queries passed to query engine

7) Answer generated: Groq LLM streams generated answer

8) Displayed: streamed answer updates chatbot UI in real-time

9) Clear/reset: user can clear uploaded file and start over

✅ Parsing supports PDFs, docs, text files, images, spreadsheets, presentations


🏗️ Installation & Setup
Follow these instructions to set up the project locally or prepare for deployment.

1️. Clone the repository

git clone https://github.com/Tanyboy3333/DataDoc-AI.git
cd DataDoc-AI


2️. Create a .env file
In the project root, create a .env file (make sure this file is never uploaded to GitHub):

LLAMA_CLOUD_API_KEY=your_llama_cloud_api_key_here
GROQ_API_KEY=your_groq_api_key_here
COHERE_API_KEY=your_cohere_api_key_here
👉 Replace your_llama_cloud_api_key_here etc. with your actual API keys from LlamaParse, Groq, and Cohere.

⚠️ Important: Add .env to your .gitignore file:

.env

3️. Install Python dependencies
Ensure you have Python 3.9+ installed.

pip install -r requirements.txt


4️. Run the app locally

python app.py

The app will launch locally at http://127.0.0.1:7860/. You can now upload a document and start chatting.

NOTE:

📝 Environment Variables
The following environment variables are required:

Variable	Description
LLAMA_CLOUD_API_KEY	API key for LlamaParse
GROQ_API_KEY	API key for Groq LLM
COHERE_API_KEY	API key for Cohere embeddings

✅ Locally they are loaded via .env using python-dotenv
✅ In Render.com, they are set via Render dashboard under Environment → Environment Variables


🌐 Deployment on Render
Deploying to Render.com as a Web Service:

Push your code to a GitHub repository (public or private)

Login to Render → click New → Web Service

Connect your GitHub repo

Set build and start commands:

Field	Value
Build Command	pip install -r requirements.txt
Start Command	python app.py

Set Python version under "Environment" → python_version = 3.9

Add Environment Variables from your .env file directly into Render (Settings → Environment)

Choose Instance Type → Starter or Free tier

Click Create Web Service

✅ Render will automatically build and deploy → available at your Render domain!


📝 Future Improvements
✅ Store multiple document indexes per user session
✅ Persist indexes across sessions / restart
✅ Add authentication (e.g., Firebase Auth)
✅ Support multi-file queries / multi-modal files
✅ Add PDF/Word preview inside app
✅ Add export of chat history
✅ GPU acceleration for faster inference



```
