import smtplib

email_addresses = ['example@gmail.com',
                   'example2@gmail.com']  # put your email addresses you want to sent it to here
gmail_user = 'YOURUSERNAME'         # put the gmail username here
gmail_password = 'YOURPASSWORD'     # put the gmail password here

sent_from = gmail_user
to = email_addresses
subject = 'Hu Site informatie'      # put the subject text here
body = 'De site is up!'             # put the body text here

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
