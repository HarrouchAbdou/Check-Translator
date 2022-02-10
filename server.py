import os
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
from Aligment_FR import SearchByCos

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)


@app.route('/')
def upload():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['fileFr']
        f1 = request.files['fileAr']
        f.save("Francais_Normalise.txt")
        f1.save("Arabe_Normalise.txt")
        return render_template('ALigment.html')


@app.route('/aligment', methods=['GET'])
def al():
    return jsonify({"data": str(SearchByCos("Francais_Normalise.txt", "Arabe_Normalise.txt"))})


port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, host="0.0.0.0", port=port, debug=True)
