import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Email Credentials
sender_email="mgrsam778@gmail.com"
receiver_email="rumancha12@gmail.com"
password="qfph oadv ymdd kijw" #use app password, Not your Gmail password app testing

#Create the email
message=MIMEMultipart()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]="Test Email"

#Email Body
body="Hello, this is a test email sent from Samiksha"
message.attach(MIMEText(body, "plain"))

#Send the email
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent succesfully")
except Exception as e:
    print(f"Error: {e}")