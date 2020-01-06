from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Tao header
Msg = MIMEMultipart()
Msg['To'] = 'banhmibotoisua@gmail.com'
Msg['From'] = 'phamphong5499@gmail.com'
Msg['Subject'] = 'Test email'

# Tao body
Part = MIMEText('text','plain')
Body = 'test email by google'
Part.set_payload(Body)
Msg.attach(Part)

# Gui thu
SMTP_Sever = 'aspmx.l.google.com'
SMTP_Port = 25
Session = smtplib.SMTP(SMTP_Sever,SMTP_Port)
Session.ehlo()
Session.sendmail('banhmibotoisua@gmail.com','phamphong5499@gmail.com',Msg.as_string())
Session.quit()

