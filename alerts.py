import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "2023cs_jennessajoellavalder_a@nie.ac.in"
EMAIL_PASSWORD = "igar uzkw gtki wtlv"
EMAIL_RECEIVER = "jennvalder2004@gmail.com"


def send_alert(message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = "Integrity Alert"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
    except Exception as e:
        print("Alert failed:", e)