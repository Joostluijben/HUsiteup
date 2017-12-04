import smtplib
import getpass
import sys

emailAdresses = [input('Fill in email addresses you want to sent to, seperated with commas: ')]  # put your email addresses you want to sent it to here
gmailUser = input('Your gmail username: ')  # put the gmail username here
gmailPassword = getpass.getpass(prompt='Your gmail password: ')  # put the gmail password here


sentFrom = gmailUser
to = emailAdresses
subject = 'HU site information'  # put the subject text here
body = 'The HU site is UP!'  # put the body text here

emailText = """\
From: %s
To: %s
Subject: %s

%s
""" % (sentFrom, ", ".join(to), subject, body)


def mail():
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmailUser, gmailPassword)
        server.sendmail(sentFrom, to, emailText)
        server.close()

        print('Site is up!')
    except:
        print('Something went wrong...')
