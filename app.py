from flask import Flask


app = Flask(__name__)

<<<<<<< HEAD

=======
>>>>>>> aebaa6cbec44ed0b1be1ab4ddced3abfc426d80f
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def test():
<<<<<<< HEAD
    return "<p>Testing new route endpoint!</p>"

=======
    return "<p>Testing new route endpoint!</p>"
>>>>>>> aebaa6cbec44ed0b1be1ab4ddced3abfc426d80f
