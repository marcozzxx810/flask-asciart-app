from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename
from asciitool import imageToAscii
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.dirname(__file__) + '/static/images'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def findFileExtension(filename):
    return filename.rsplit('.', 1)[1].lower()

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/convert', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        if 'image' not in request.files:
            return 'Failed'
        file = request.files['image']
        if file.filename == '':
            return 'Failed'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            fileExtension = findFileExtension(filename)
            filePath = os.path.join(app.config['UPLOAD_FOLDER'], "input."+fileExtension)
            outputPath = os.path.join(app.config['UPLOAD_FOLDER'], "out.txt")
            file.save(filePath)
            imageToAscii(filePath, outputPath)
        return redirect(url_for('result'))

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)