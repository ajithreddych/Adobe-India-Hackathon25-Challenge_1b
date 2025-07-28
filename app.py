from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os
from utils import process_documents

app = Flask(__name__, template_folder='../frontend')
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    files = request.files.getlist('documents')
    persona = request.form['persona']
    job = request.form['job']

    filenames = []
    for file in files:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        filenames.append(file.filename)

    output = process_documents(filenames, persona, job)
    output['metadata'] = {
        "input_documents": filenames,
        "persona": persona,
        "job_to_be_done": job,
        "processing_timestamp": datetime.now().isoformat()
    }

    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)
