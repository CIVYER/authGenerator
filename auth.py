# email libs
from email.message import EmailMessage
import ssl
import smtplib
import secrets

# data passing lib
import sys

def authenticate(receiver_in):
    # Email Verification
    gmail_user = 'auth.group2@gmail.com'
    gmail_password = 'tinidqskatqnlllh'
    receiver = receiver_in

    # Generate a random verification code (3 bytes of randomness)
    verification_code = secrets.token_hex(3)
    
    subject = 'Verification Code'

    # Compose the email body with the verification code
    body = "Your Verification Code is: " + str(verification_code) + "\nPLEASE IGNORE IF YOU DID NOT REQUEST ANY AUTHENTICATION!!"

    # Create an EmailMessage object
    em = EmailMessage()
    em['From'] = "EMAIL VERIFICATION"
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    try:
        # Connect to Gmail's SMTP server using SSL
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(gmail_user, gmail_password)
            # Send the email
            smtp.sendmail(gmail_user, receiver, em.as_string())
    except:
        # Handle exceptions, e.g., if the email could not be sent
        return "INVALID EMAIL"
    
    return verification_code

# Retrieve the email address from command-line arguments and call the authenticate function
inpt = " ".join(sys.argv[1:])
print(authenticate(inpt))
