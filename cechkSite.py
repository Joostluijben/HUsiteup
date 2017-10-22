import requests, time, checkSiteMail

payload = {
    'username': 'USERNAME',  # fill in your HU username
    'password': 'PASSWORD'  # fill in your HU password
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}  # login with the mozilla browser

with requests.Session() as session:
    cookie = session.get("https://sharepoint.hu.nl").cookies  # get the cookie from the main site
    login = session.post('https://mijn.sharepoint.hu.nl/my.policy', data=payload, headers=headers,
                         cookies=cookie)  # login

    site = session.post(
        'https://cursussen.sharepoint.hu.nl/fnt/53/TICT-V1PROG-15')  # open session to the site you want to check
    while True:
        if site.text == 'Cannot connect to the configuration database.':  # in my case the site said this if it was offline. Put what your offline site says here
            time.sleep(300)     # wait for 5 minutes, because it could cause a overload
            site = session.post('https://cursussen.sharepoint.hu.nl/fnt/53/TICT-V1PROG-15')     # try again
        else:
            checkSiteMail.mail()        # if it is online, send email
            break
