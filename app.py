import os
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from dotenv import load_dotenv

app = Flask(__name__)

#Enable environment 
load_dotenv()

#Configure Flask Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get("EMAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("EMAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = 'Coffee Lover\'s Club'

mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/coffee")
def coffee():
    return render_template("/coffee.html")

#Sending Emails
@app.route("/mail", methods=["POST"])
def send_mail():
    recipient_email = request.form["email"]

    msg = Message("Coffee Lover's Club: Thank You!", recipients=[recipient_email])
    msg.html = "<p>Check out the creator of Coffee Lover's Club <a href='https://ryan-szalaty.github.io'>here</a>.</p>"

    try:
        mail.send(msg)
        return f"Email sent successfully! Please check your inbox at {recipient_email}."
    except Exception as error:
        return f"Email not sent. Error: {str(error)}."