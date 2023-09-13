import os, secrets
from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mail import Mail, Message
from dotenv import load_dotenv

app = Flask(__name__)

#Enable environment 
load_dotenv()

#Configure sessions key
secret_key = secrets.token_hex(16)

#Configure Flask Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get("EMAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.environ.get("EMAIL_PASSWORD")
app.config['MAIL_DEFAULT_SENDER'] = 'Coffee Lover\'s Club'
app.config['SECRET_KEY'] = secret_key

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
    recipient_name = request.form["name"]

    msg = Message("Coffee Lover's Club: Thank You!", recipients=[recipient_email])
    msg.body = "Thank you for checking out Coffee Lover's Club! We are thrilled to have you!\n\nCoffee enthusiasts are similar no matter where they come from: They have a keen sense of refined taste and know what they want. Mild, medium, dark...there's something for everyone.\n\nCheck out the creator of Coffee Lover's Club at https://ryan-szalaty.github.io.\n\nHave a great day!"

    try:
        mail.send(msg)
        session["flash_message"] = {
            "message" : f"Email sent successfully! Please check your inbox, {recipient_name}.",
            "category" : "success"
        }
        return redirect("/")
    except Exception:
        session["flash_message"] = {
            "message" : f"Email not sent. Please check your email address and try again. If this error persists, please contact us.",
            "category" : "warning"
        }
        return redirect(url_for("about"))