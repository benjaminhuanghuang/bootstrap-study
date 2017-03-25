from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from flask_uploads import UploadSet, configure_uploads, All


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['UPLOADED_FILES_DEST'] = 'uploads'
# Init bootstrap
Bootstrap(app)
# Init files_uploads
files = UploadSet('files', All)
configure_uploads(app, files)


@app.route('/')
def index():
    return render_template('index.html', title="Index")


@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == "POST" and 'media' in request.files:
        filename = files.save(request.files['media'])
        print filename
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True, port=9527)
