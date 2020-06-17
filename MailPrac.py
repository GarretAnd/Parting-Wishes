import smtplib  # Access Inbox
from email.mime.text import MIMEText  # Email Text
from email.mime.multipart import MIMEMultipart  # Email Attachments
from email.mime.base import MIMEBase
from email import encoders


def get_server(email_, password_):
    server_ = smtplib.SMTP('smtp.gmail.com', 587)  # logs into the gmail servers specified at port 587
    server_.starttls()
    server_.login(email_, password_)  # uses the provided email and password to get the server ID
    return server_  # returns server to be used to send emails from


def address(key, server_, value, user):
    message = "Congratulations! \n" \
              "Open the attached files to see the Parting Wishes your peers sent you! \n" \
              "Warmly, \n" \
              "The Parting Wishes Organizers"  # specified Message to be sent with email

    send_to_email = key  # send to the provided email
    email_address = user  # the email account currently being used.

    print('Email being sent to: ' + send_to_email)  # flag for progress
    msg = MIMEMultipart()
    msg['From'] = email_address  # sets up letter with sections
    msg['To'] = send_to_email
    msg['Subject'] = "Open For Your Parting Wishes"

    i = 0
    while i < value:  # passed value tells it how many pngs to attach
        filename = 'finalPDF/output' + str(i) + '.png'  # creates the file to be sent
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename=Letter" + str(i) + ".png",  # gets needed file and adds it
            )

            msg.attach(part)  # attaches file
            i += 1

    filename = 'Assets/Parting Message.png'  # goes to the Parting Message

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename=Congratulations.png",  # Adds the Parting Message to the file
        )

        msg.attach(part)  # Adds it

    filename = 'Assets/Last Page.png'  # Goes to the Last Page

    with open(filename, "rb") as attachment:  # opens the file
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename=Last_Page.png",  # Adds it to the header
        )

        msg.attach(part)  # Attaches the email

    msg.attach(MIMEText(message, 'plain'))  # Attached the message
    text = msg.as_string()
    server_.sendmail(email_address, send_to_email, text)  # sends the email!
    print("Message Sent!")  # flag for progress

