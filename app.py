
from flask import Flask


app = Flask(__name__)
<<<<<<< HEAD

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
=======
    
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def test():
    return "<p>Tessting new route endpoint!</p>"
>>>>>>> 6ba4803d78e4a5dbe774d4cd6faadae2257c0a8c
