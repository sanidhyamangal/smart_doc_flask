from flask import Flask, render_template, request, flash, redirect, jsonify, send_from_directory, url_for
import base64
from predictions import predict_malaria, predict_pneumonia
from werkzeug.utils import secure_filename
import os
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


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


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
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            try:
                result = predict_malaria(
                    os.path.join(app.config['UPLOAD_FOLDER'], filename))
                if result:
                    result_response["result"] = "True"
                else:
                    result_response["result"] = "False"
                return render_template("result.html",
                                       result=result_response["result"],
                                       filename=filename)
            except Exception:
                return redirect("/")
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
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            try:
                result = predict_pneumonia(
                    os.path.join(app.config['UPLOAD_FOLDER'], filename))
                if result:
                    result_response["result"] = "True"
                else:
                    result_response["result"] = "False"
                return render_template("result.html",
                                       result=result_response["result"],
                                       filename=filename)
            except Exception:
                return redirect("/")
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
