import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import os
import time

smtpserver='smtp.qq.com'
username='1172533210@qq.com'
password='xbpyjhmfbmysgjgh'

sender='1172533210@qq.com'
receiver="1172533210@qq.com"
subject='Python email test'

sendfile=open('D:\\a.png','rb').read()
att=MIMEText(sendfile,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="result.html"'
msgRoot=MIMEMultipart('related')
msgRoot['Subject']=subject
msgRoot.attach(att)
msg=MIMEText('<html><h1>你好</h1></html>','html','utf-8')
msg['Subject']=Header(subject,'utf-8')


smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()
