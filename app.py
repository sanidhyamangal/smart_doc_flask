from flask import Flask, render_template, request, flash, redirect, jsonify
import base64
from predictions import predict_malaria, predict_pneumonia
import uuid



app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/predict/malaria', methods=['POST', 'GET'])
def malaria():
    if request.method == 'POST':
            # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            result_response = {}
            result = predict_malaria(base64.b64encode(file.read()))
            if result:
                result_response["result"] = "True"
            else:
                result_response["result"] = "False"
            return jsonify(result_response)
        return redirect("/")


@app.route('/predict/pneumonia', methods=['POST', 'GET'])
def pneumonia():
    if request.method == 'POST':
            # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            result_response = {}
            result = predict_pneumonia(base64.b64encode(file.read()))
            if result:
                result_response["result"] = "True"
            else:
                result_response["result"] = "False"
            return jsonify(result_response)
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)