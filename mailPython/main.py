import random
import smtplib
import datetime as dt
import pandas as pd
# 1. Update the birthdays.csv
email = "*********"
password="************"
now = dt.datetime.now()
month = now.month
day = now.day

today = (month, day)
df = pd.read_csv("birthdays.csv")

b_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in df.iterrows()}

if today in b_dict:
    b_person = b_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", b_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=email, password=password)
        conn.sendmail(
            from_addr=email,
            to_addrs=b_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}")
        conn.close()




