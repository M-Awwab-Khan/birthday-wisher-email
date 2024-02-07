import datetime as dt
import smtplib
import random

my_email = 'mawwabkhank2006@gmail.com'
password = 'efcb xgpp xfgb waba'

with open('quotes.txt', 'r', encoding="utf8") as f:
    quotes = f.readlines()


if dt.datetime.now().weekday() == 2:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        random_quote = random.choice(quotes)
        subject = random_quote.split('–')[-1].strip()
        connection.sendmail(
            from_addr=my_email,
            to_addrs='docsofawwab@gmail.com',
            msg=f'Subject:{subject}\n\n{random_quote}'.encode('utf-8')
        )