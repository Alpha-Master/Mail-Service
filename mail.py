import smtplib

def sendmail(name,mailid):
    host='smtp.servicename.com'
    host_port=587
    from_mail='sender_mail_id@mail.com'
    subject="subject"
    password='auth password'
    content='This is a no reply mail.'
    try:
        smtpObj = smtplib.SMTP(host,host_port)
        smtpObj.starttls()
        smtpObj.login(from_mail,password)
        smtpObj.sendmail(from_mail, mailid, 'Subject: '+subject+'\r\n\r\nHi '+name+', \r\n\t'+content+'\r\nSincerely,\r\nName \n')
        smtpObj.quit()
    except smtplib.SMTPException as error:
        return error
    return 'Success'
