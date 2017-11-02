import smtplib
import getpass
import sys


try:
    email_addresses = [input(
    'Fill in email addresses you want to sent to, seperated with commas: ')]  # put your email addresses you want to sent it to here
    gmail_user = input('Your gmail username: ')  # put the gmail username here
    gmail_password = getpass.getpass('Your gmail password: ')  # put the gmail password here
except KeyboardInterrupt:
    sys.exit('Closing...')
sent_from = gmail_user
to = email_addresses
subject = 'HU site information'  # put the subject text here
body = 'The HU site is UP!'  # put the body text here

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)


def mail():
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Site is up!')
    except:
        print('Something went wrong...')
