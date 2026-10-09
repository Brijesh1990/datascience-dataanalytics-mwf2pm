# sending email via smtp 
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
# send email to reciever and sender details 

sender_email='brijeshdeveloper36@gmail.com'
# reciever_email='brijeshpandey.tops@gmail.com'
reciever_email='mfaizesumara20@gmail.com'
apppassword=""

# create a email services setup for send email
message=MIMEMultipart()
message["from"]=sender_email
message["to"]=reciever_email
message["subject"]="For sending email of customers details"

# set email text 
body="Hello : \n This is just a testing of email via python smtplib library"
message.attach(MIMEText(body,"plain"))
# used exception handling to send email
file_path='brijesh.jpeg'
try:
    # connect email with gmail server
    with open(file_path,'rb') as attachment:
        part=MIMEBase("application","octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        
        # attachment web formate send read data
        part.add_header(
            
            "Content-Disposition",
            f"attachment; filename={file_path}" 
            
        ) 
        message.attach(part)
    
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender_email,apppassword)    
    # send email here
    server.sendmail(    
        sender_email,
        reciever_email,
        message.as_string()
        )
    # print a success message
    print("Your email successfully send check your email address")
        
except Exception as e:
    print("something went wrong while sending email",e)

finally:
    server.quit()
     


