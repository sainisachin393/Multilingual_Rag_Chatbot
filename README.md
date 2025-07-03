# 📄 Multilingual Document Q&A using RAG and Azure OpenAI

This is a multilingual document-based question answering system powered by **Flask**, **Streamlit**, **LangChain**, **FAISS**, and **Azure OpenAI**.  
It allows users to upload documents in **PDF**, **DOCX**, or **Image** formats and query them in **English**, **Japanese**, or **Chinese**.

---

## 🚀 Features

- ✅ Supports PDF, DOCX, and image files (JPEG/PNG)
- ✅ OCR for scanned images using GPT-4 Vision
- ✅ Multilingual support: English, Japanese, and Chinese
- ✅ RAG (Retrieval-Augmented Generation) architecture
- ✅ FAISS vector search for fast semantic retrieval
- ✅ Simple UI built with Streamlit
- ✅ RESTful backend API using Flask

---

## 🏗️ Project Structure

```
├── app.py           # Flask backend API
├── rag_core.py      # Core logic for ingestion, OCR, embeddings, FAISS, and querying
├── ui.py            # Streamlit frontend for user interaction
├── faiss_index/     # Stores FAISS vector DBs (auto-created)
├── .env             # Azure OpenAI credentials (not committed)
```

---

## ⚙️ Setup Instructions

### 1. Install Python dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install manually:

```bash
pip install streamlit flask requests python-dotenv pdfplumber faiss-cpu openai langchain langchain-openai python-docx pillow
```

### 2. Set up `.env` file

Create a `.env` file in the root directory:

```env
AZURE_OPENAI_API_KEY=your_azure_api_key
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_COMPLETION_DEPLOYMENT_NAME=gpt-4-vision
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=text-embedding-ada-002
```

---

## ▶️ How to Run

### 1. Start the Flask API

```bash
python app.py
```

### 2. Run the Streamlit UI (in a separate terminal)

```bash
streamlit run ui.py
```

Then open your browser at `http://localhost:8501`.

---

---

## 📄 Supported File Types

- PDFs (including scanned PDFs)
- DOCX (Microsoft Word)
- Images (PNG, JPG, JPEG)

---

## ❓ FAQ

- **OCR not working?** Ensure GPT-4 Vision is enabled for your Azure OpenAI deployment.
- **Query not returning accurate results?** Check if the document text was properly extracted during ingestion.
- **API errors?** Verify `.env` credentials and confirm both Flask and Streamlit servers are running.

---

## 🛠 Future Improvements

- Add support for Excel and TXT files
- Dockerize for easy deployment
- Add login/authentication
- Deploy backend as a cloud API

---

## 📜 License

This project is released under the [MIT License](LICENSE).


