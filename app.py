import os

from flask import Flask, render_template, request, redirect, send_file, url_for

from s3_demo import list_files, list_filename


app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "1831-learn"


@app.route('/')
def entry_point():
    return 'Hello World!'


@app.route("/storage")
def storage():
    contents = list_files(BUCKET)
    return render_template('storage.html', contents=contents)


@app.route("/file/<filename>"+"/", methods=['GET'])
def file(filename):
    contents = list_filename(BUCKET,filename)
    return render_template('storage.html', contents=contents)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8085) #debug=True)
