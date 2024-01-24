'''Send emails through coding'''
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'ZTM'
email['to'] = 'thanujacherukuri111@gmail.com'
email['subject'] = 'You won MONEY'
email.set_content(html.substitute(
    {'name': 'Thanu', 'amount': '10000$'}), 'html')

with smtplib.SMTP('smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Generate App password and add it here not you actual password
    smtp.login('ztmmastery@gmail.com', 'wgkv ucsr zrty nuvl')
    smtp.send_message(email)
    print('All good boss')
    smtp.quit()
