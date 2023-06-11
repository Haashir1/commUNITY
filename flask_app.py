from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/help')
def help():
    return render_template('Help Us.html')

@app.route('/donate')
def donate():
    return render_template('Donate.html')

@app.route('/signup')
def signup():
    return render_template('Sign Up for Donations.html')

@app.route('/contact')
def contact():
    return render_template('Contact Us.html')

@app.route('/save-form-data', methods=['POST'])
def save_form_data():
    # Handle form data submission here
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Process the form data and save it

    return "Form submitted successfully!"

# Route for serving static files
@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9029)
