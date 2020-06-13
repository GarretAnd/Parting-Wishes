import smtplib  # Access Inbox
from email.mime.text import MIMEText  # Email Text
from email.mime.multipart import MIMEMultipart  # Email Attachments
from email.mime.base import MIMEBase
from email import encoders


def get_server(email_, password_):
    server_ = smtplib.SMTP('smtp.gmail.com', 587)
    server_.starttls()
    server_.login(email_, password_)
    return server_


def address(key, server_, tf):
    email_address = global_username
    if not tf:
        message = 'Hello!'
    else:
        message = 'Hello!'

    send_to_email = key
    print('Email being sent to: ' + send_to_email)
    subject = 'say'
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = send_to_email
    msg['Subject'] = subject

    filename = 'finalPDF/pic.png'

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename=Card.png",
        )

        msg.attach(part)

    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()
    server_.sendmail(email_address, send_to_email, text)

    print("Message Sent!")


global_username = 'partingwishes2020@gmail.com'
global_password = 'Closure1769!'
email_to = 'gd2strems@gmail.com'

server = get_server(global_username, global_password)  # Re-Enters email server this time for sending
address(email_to, server, True)
server.quit()
