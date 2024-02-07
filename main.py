##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import random
import pandas as pd

my_email = 'mawwabkhank2006@gmail.com'
password = 'efcb xgpp xfgb waba'

data = pd.read_csv('birthdays.csv')
now = dt.datetime.now()
day = now.day
month = now.month
letter_filenames = ['./letter_templates/letter_1.txt', './letter_templates/letter_2.txt', './letter_templates/letter_3.txt']

for row in data.itertuples():
    if row[4] == month and row[5] == day:
        with open(random.choice(letter_filenames), 'r') as f:
            msg = f.read().replace('[NAME]', row[1])
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row[2],
                msg=f'Subject:Happy Birthday {row[1]}\n\n{msg}'
            )




