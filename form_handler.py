from flask import Flask, request

app = Flask(__name__)

@app.route('/save-form-data', methods=['POST'])
def save_form_data():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Perform any necessary processing with the form data
    # For example, you can save it to a database or write it to a file

    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run()
