from email.message import EmailMessage
import smtplib


with open('email_info_key.txt','r') as f:
    content = f.readlines()

def email(recipient_email, subject, body):
        
        try:
            sender_email=content[0]
            app_password=content[1]
            # GMAIL SMTP 
            
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, app_password)
            
            # Message INFO
            message = f"Subject: {subject}\n\n{body}"
            
            # SENT Email
            server.sendmail(sender_email, recipient_email, message)
            print("Email was sent.")
        
            server.quit()  # Close Conection
        except Exception as e:
            print("Email was not sent:", e)
