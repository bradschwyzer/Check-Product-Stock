import requests
import time
from bs4 import BeautifulSoup
import smtplib

# Put in your Gmail username and password. You will be using Gmail to send the files to text message or email.
username = 'username'
password = 'pass'
sender = 'test@gmail.com'
receivers = ['test@test.com'] 
# many carriers have an email address you can use to send email to phone.   
#http://sms411.net/how-to-send-email-to-a-phone/  - Use add block. It has alot of the email addresses to use to send to a mobile.



#define a function to send email. This will be using gmail SMTP server. Requires a GMAIL account.
# may have to enable less secure accounts or use an app specific password if 2fa 
def sendemail(listofstores1):
    message = """From: From Test <Test@gmail.com>
    To: To Test <a@test.com>
    Subject: Switch in stock
    """ + listofstores1
    

    try:
       smtpObj = smtplib.SMTP('smtp.gmail.com:587')
       smtpObj.ehlo()
       smtpObj.starttls()
       smtpObj.login(username, password)
       smtpObj.sendmail(sender, receivers, message)        
       return True
    except smtplib.SMTPException:
       return False
# main function. This will check the website listed below and find the most recent updates with "TX" for text in them. 
while True:
    result =''
    r = requests.get('http://www.istocknow.com/product/switch/system')
    soup = BeautifulSoup(r.content, 'html.parser')
    storelist = soup.find_all('a', class_='storename')
    for store in storelist:    
        if "TX" in store.text:
            result = result + "\n" + store.text
        else:
            continue
    if result is not '':
        sendemail(result)
        print (result)
    time.sleep(300)
