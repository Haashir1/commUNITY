import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, jsonify

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

def send_email(name, email, message):
    sender_email = 'hahmed2@wihi.org'  # Replace with your email address
    receiver_email = 'hahmed2@wihi.org'  # Replace with the recipient email address
    password = 'xfx83nwq'  # Replace with your email password

    subject = 'Form1 Reply'  # Replace with the desired subject for the email
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"  # Compose the email body

    # Create a multipart message and set the email headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the email body to the message
    message.attach(MIMEText(body, 'plain'))

    # Send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)


@app.route('/save-form-data', methods=['POST'])
def save_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    send_email(name, email, message)

    return jsonify({'message': 'Form submitted successfully!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9029)

# Route for serving static files
@app.route('/static/<path:filename>')
def serve_static(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9029)
