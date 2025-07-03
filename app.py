from flask import Flask, request, jsonify
import rag_core
import logging

app = Flask(__name__)

@app.route('/ingest', methods=['POST'])
def ingest():
    """Endpoint to upload and process a file."""
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    language = request.form.get('language', 'English')
    
    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400
        
    try:
        file_bytes = file.read()
        file_type = file.content_type
        file_name = file.filename
        
        doc_id = rag_core.ingest_document(file_bytes, file_type, file_name, language)
        return jsonify({"success": True, "doc_id": doc_id, "file_name": file_name})
        
    except Exception as e:
        logging.error(f"API Ingest Error: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/query', methods=['POST'])
def query():
    """Endpoint to ask a question to a processed document."""
    data = request.get_json()
    if not data or not all(k in data for k in ['doc_id', 'question', 'language']):
        return jsonify({"error": "Missing 'doc_id', 'question', or 'language' in request body"}), 400
        
    try:
        answer = rag_core.query_document(data['doc_id'], data['question'], data['language'])
        return jsonify({"success": True, "answer": answer})
        
    except Exception as e:
        logging.error(f"API Query Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Note: For production, use a proper WSGI server like Gunicorn or uWSGI
    app.run(host='0.0.0.0', port=5000, debug=True)