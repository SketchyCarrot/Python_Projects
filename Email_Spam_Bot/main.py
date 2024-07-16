import smtplib
import pandas as pd

df = pd.read_csv("C:\\Users\\91909\\Downloads\\Student List.csv")

emails = df["Email-Id"]

print(emails)

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login("quizclubjnu@gmail.com", "")

for email in emails:
        server.sendmail("quizclubjnu@gmail.com", "email")