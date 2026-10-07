from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.message import EmailMessage
import os
app = Flask(__name__)
app.secret_key = "churchboii-secret-key"

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD") # App password (keep safe)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        # Send confirmation to user
        send_email_to_user(name, email)

        # Send message to YOU
        send_email_to_me(name, email, subject, message)

        flash("Message sent successfully! Please check your email.", "success")
        return redirect(url_for("home"))

    return render_template("index.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


# -------- EMAIL TO USER --------
def send_email_to_user(name, user_email):
    msg = EmailMessage()
    msg["Subject"] = "Thank you for contacting me!"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = user_email

    msg.set_content(f"""
Hi {name},

Thank you for reaching out through my portfolio website.
I have received your message and will get back to you shortly.

Best regards,
Churchboii
""")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)


# -------- EMAIL TO YOU --------
def send_email_to_me(name, user_email, subject, message):
    msg = EmailMessage()
    msg["Subject"] = f"New Contact Form Message: {subject}"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS  # 👈 You receive it

    msg.set_content(f"""
New message received from your portfolio website:

Name: {name}
Email: {user_email}
Subject: {subject}

Message:
{message}
""")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
