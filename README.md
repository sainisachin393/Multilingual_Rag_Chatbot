Multilingual Document Q&A
Table of Contents
About the Project

Features

Built With

Getting Started

Prerequisites

Installation

Usage

Project Structure

Contributing

License

Contact

Acknowledgments

About The Project
This project provides a robust solution for multilingual document question-answering. It leverages a Flask backend for document ingestion and querying, powered by Azure OpenAI services for embeddings and language model completions, and a Streamlit frontend for an interactive user interface. Users can upload various document types (PDF, images, DOCX), process them, and then ask questions in English, Japanese, or Chinese to get relevant answers extracted from the document content.

The system is designed to handle both text extraction (including OCR for images within PDFs or standalone images) and intelligent question-answering based on the ingested content, utilizing FAISS for efficient similarity search.

Features
Multilingual Support: Process and query documents in English, Japanese, and Chinese.

Multiple Document Types: Supports PDF, PNG, JPG, JPEG, and DOCX file formats.

OCR Capability: Extracts text from images embedded in PDFs or standalone image files.

RAG (Retrieval-Augmented Generation): Uses FAISS vector store for efficient document retrieval and Azure OpenAI for generating accurate answers based on the retrieved context.

User-Friendly Interface: A Streamlit frontend for easy document upload and question submission.

Scalable Backend: Flask API for handling document processing and queries, designed to be deployed independently.

Built With
Python

Flask: For the backend API.

Streamlit: For the interactive web UI.

Azure OpenAI:

AzureOpenAIEmbeddings: For generating document embeddings.

AzureOpenAI (vision client): For OCR and language model completions.

LangChain: For document processing utilities (RecursiveCharacterTextSplitter, Document).

FAISS: For efficient vector storage and similarity search.

pdfplumber: For extracting text and images from PDF files.

python-docx: For extracting text from DOCX files.

Pillow (PIL): For image processing.

python-dotenv: For managing environment variables.

requests: For API communication between frontend and backend.

Getting Started
To get a local copy of this project up and running, follow these steps.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.8+

pip (Python package installer)

Azure OpenAI Account: You will need access to Azure OpenAI services with deployed models for completions and embeddings.

Installation
Clone the repository:

git clone https://github.com/YOUR_USERNAME/multilingual-doc-qa.git
cd multilingual-doc-qa

Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

(Note: You'll need to create a requirements.txt file based on the pip install commands for the libraries listed in "Built With".)

Set up Azure OpenAI Environment Variables:

Create a .env file in the root directory of the project with your Azure OpenAI credentials:

AZURE_OPENAI_API_VERSION="2024-02-01" # Or your specific version
AZURE_OPENAI_ENDPOINT="https://YOUR_AZURE_OPENAI_RESOURCE_NAME.openai.azure.com/"
AZURE_OPENAI_API_KEY="YOUR_AZURE_OPENAI_API_KEY"
AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME="YOUR_COMPLETION_MODEL_DEPLOYMENT_NAME" # e.g., gpt-4o
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME="YOUR_EMBEDDING_MODEL_DEPLOYMENT_NAME" # e.g., text-embedding-ada-002

Make sure the deployment names match what you have configured in your Azure OpenAI studio.

Usage
Start the Flask Backend:

Open your terminal, navigate to the project root, and run:

python app.py

The backend API will start on http://127.0.0.1:5000.

Start the Streamlit Frontend:

Open a new terminal window (keep the backend running), navigate to the project root, and run:

streamlit run ui.py

This will open the Streamlit application in your web browser.

Interact with the Application:

In the Streamlit UI, use the sidebar to select the document language.

Upload a document (PDF, image, or DOCX).

Click "Process Document" to send it to the backend for ingestion.

Once processed, enter your question in the text input field.

Click "Get Answer" to receive a response based on the document content.

You can clear the session using the "Clear Session" button in the sidebar.

Project Structure
.
├── app.py              # Flask backend application for API endpoints (ingest, query)
├── rag_core.py         # Core RAG logic: document processing, text extraction, embeddings, FAISS, LLM interaction
├── ui.py               # Streamlit frontend for user interaction
├── .env.example        # Example environment variables file
├── requirements.txt    # List of Python dependencies
└── faiss_index/        # Directory to store FAISS indices of processed documents (created automatically)

Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeature).

Make your changes and commit them (git commit -m 'Add YourFeature').

Push to the branch (git push origin feature/YourFeature).

Open a Pull Request.

License
Distributed under the MIT License. See the LICENSE file for more information.


Project Link: https://github.com/YOUR_USERNAME/multilingual-doc-qa

Acknowledgments
Azure OpenAI Service

LangChain

FAISS

Streamlit

Flask
