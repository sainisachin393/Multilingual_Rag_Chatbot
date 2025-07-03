
import streamlit as st
import requests

# --- Configuration ---
FLASK_API_URL = "http://127.0.0.1:5000"
LANGUAGE_PROMPTS = {
    'English': {}, 'Japanese': {}, 'Chinese': {} # Keys for the selectbox
}

# --- Streamlit UI ---
st.set_page_config(page_title="Multilingual Doc Analyzer", layout="wide")
st.title("📄 Multilingual Document Q&A (via API)")
st.caption(f"Backend API located at: {FLASK_API_URL}")

# Sidebar
with st.sidebar:
    st.header("Settings")
    language = st.selectbox("Document Language", list(LANGUAGE_PROMPTS.keys()))
    uploaded_file = st.file_uploader(
        "Upload Document",
        type=["pdf", "png", "jpg", "jpeg", "docx"],
        accept_multiple_files=False
    )
    
    if st.button("Process Document") and uploaded_file:
        with st.spinner("Sending file to backend for processing..."):
            files = {'file': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            data = {'language': language}
            try:
                response = requests.post(f"{FLASK_API_URL}/ingest", files=files, data=data)
                response.raise_for_status() # Raises an exception for 4XX/5XX errors
                
                result = response.json()
                st.session_state.doc_id = result['doc_id']
                st.session_state.file_name = result['file_name']
                st.success(f"Backend processed '{result['file_name']}' successfully!")
                
            except requests.exceptions.RequestException as e:
                st.error(f"API connection error: {e}")
            except Exception as e:
                st.error(f"Failed to process document: {e}")

# Main Interface
if "doc_id" in st.session_state and "file_name" in st.session_state:
    st.success(f"Ready to answer questions about: **{st.session_state.file_name}**")
    question = st.text_input("Enter your question:", key="question_input")
    
    if st.button("Get Answer") and question:
        with st.spinner("Querying backend for an answer..."):
            payload = {
                'doc_id': st.session_state.doc_id,
                'question': question,
                'language': language
            }
            try:
                response = requests.post(f"{FLASK_API_URL}/query", json=payload)
                response.raise_for_status()
                
                result = response.json()
                st.markdown(f"**Answer:**\n\n{result['answer']}")
                
            except requests.exceptions.RequestException as e:
                st.error(f"API connection error: {e}")
            except Exception as e:
                st.error(f"Failed to get answer: {e}")
else:
    st.info("Please upload and process a document using the sidebar to begin.")

# Clear Session button
if st.sidebar.button("Clear Session"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()