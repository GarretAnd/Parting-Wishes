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


def address(key, server_, value):
    message = "Congratulations! \n" \
              "Open the attached files to see the Parting Wishes your peers sent you! \n" \
              "Warmly, \n" \
              "The Parting Wishes Organizers"

    send_to_email = 'garretd16@gmail.com'  # key will be actual email, not the hardwired value
    email_address = 'gd2strems@gmail.com'

    print('Email being sent to: ' + send_to_email)
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = send_to_email
    msg['Subject'] = "Open For Your Parting Wishes" + str(key)

    i = 0
    while i < value:
        filename = 'finalPDF/output' + str(i) + '.png'
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename=Letter" + str(i) + ".png",
            )

            msg.attach(part)
            i += 1

    filename = 'Assets/Parting Message.png'

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename=Congratulations.png",
        )

        msg.attach(part)

    filename = 'Assets/Last Page.png'

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename=Last_Page.png",
        )

        msg.attach(part)

    msg.attach(MIMEText(message, 'plain'))
    text = msg.as_string()
    server_.sendmail(email_address, send_to_email, text)
    print("Message Sent!")


#global_username = 'partingwishes2020@gmail.com'
#global_password = 'Closure1769!'
#email_to = 'gd2strems@gmail.com'

#server = get_server(global_username, global_password)  # Re-Enters email server this time for sending
#address(email_to, server, 6)
#server.quit()
