import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '{my_login}'
    password = '{my_password}'
    message = f"<hr>New Feedback Submission</h3><ul><li>Customer : {customer}</li><li>Dealer : {dealer}</li><li>Rating : {rating}</li><li>Comments : {comments}</li></ul>"

    sender_email = 'bunta.aja@gmai.com'
    receiver_email = 'bunta.aja@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())