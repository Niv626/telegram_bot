import os
import csv
import yagmail
import time

USER = os.getenv('', 'vogoviga@gmail.com')
PASSWORD = os.getenv('', 'Test1111')
MAIL_DOMAIN = os.getenv('', '@gmail.com')
NUM_OF_MAILS = os.getenv('', '20')
INTERVAL = os.getenv('', '2')

contacts_file = 'contacts_file.csv'
subject = 'test subject'
contents = '<h1>test contents</h1>'
attachments = os.listdir('./files')


def parse_contacts():
    try:
        with open(contacts_file) as file:
            reader = csv.reader(file)
            return next(reader)
    except IOError as err:
        print(err)


def send_mail(contacts):
    try:
        for name in contacts:
            yag = yagmail.SMTP(user=USER, password=PASSWORD)
            for _ in range(int(NUM_OF_MAILS)):
                yag.send(to=f'{name}{MAIL_DOMAIN}', subject=subject, contents=contents, attachments=attachments)
                time.sleep(INTERVAL)
    except Exception as err:
        print(f"Error, email was not sent due to: {err}")


def main():
    contacts = parse_contacts()
    send_mail(contacts)


if __name__ == '__main__':
    main()
