from flask import Flask, request, jsonify, send_file, render_template
from werkzeug.utils import secure_filename
import os
import tempfile
from pdf_utils import extract_paragraphs, find_relevant_paragraphs, highlight_paragraphs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = tempfile.gettempdir()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_pdf():
    if 'pdf' not in request.files or 'query' not in request.form:
        return jsonify({'error': 'PDF file and query required'}), 400

    file = request.files['pdf']
    query = request.form['query']
    filename = secure_filename(file.filename)
    pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(pdf_path)

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], f"highlighted_{filename}")

    try:
        paragraphs = extract_paragraphs(pdf_path)
        relevant = find_relevant_paragraphs(paragraphs, query)
        highlight_paragraphs(pdf_path, output_path, relevant)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return send_file(output_path, as_attachment=True, download_name=f"highlighted_{filename}")

if __name__ == "__main__":
    app.run(debug=True)
