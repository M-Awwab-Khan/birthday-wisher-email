import smtplib

my_email = 'mawwabkhank2006@gmail.com'
password = 'efcb xgpp xfgb waba'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='docsofawwab@gmail.com',
        msg='Subject:Testing smtplib\n\nThis is a test message to check the working of python-smtplib module.\nThank You.'
    )