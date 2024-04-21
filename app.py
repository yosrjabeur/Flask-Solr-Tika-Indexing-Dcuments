from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from tika import parser
import pysolr

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  

SOLR_URL = 'http://localhost:8983/solr/projet'  
solr_connection = pysolr.Solr(SOLR_URL, always_commit=True)

def extract_text_from_file(file_path):
    parsed = parser.from_file(file_path)
    return parsed['content']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier n\'a été envoyé.'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nom de fichier vide.'}), 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        extracted_text = extract_text_from_file(file_path)

        solr_doc = {
            'id': os.path.splitext(filename)[0],
            'content_txt_fr': extracted_text,
        }
        solr_connection.add([solr_doc])
        solr_connection.commit()

        return jsonify({'message': 'Fichier uploadé et indexé avec succès.'}), 200

@app.route('/search', methods=['GET'])
def search_documents():
    query = request.args.get('q', '')  

    results = solr_connection.search(f'content_txt_fr:{query}', **{
        'hl': 'true',  
        'hl.simple.pre': '<em>',  
        'hl.simple.post': '</em>',  
        'fl': '*,score' 
    })

    search_results = [{'title': result['id'], 'content': result['content_txt_fr'], 'score': result['score']} for result in results]

    return jsonify(search_results)

if __name__ == '__main__':
    app.run(debug=True)
