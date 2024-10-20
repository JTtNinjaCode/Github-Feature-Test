import smtplib
from email.mime.text import MIMEText
import argparse

# 設置命令列參數
def get_args():
    parser = argparse.ArgumentParser(description="Send an email using Gmail SMTP")

    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--body', required=True, help='Body of the email')
    parser.add_argument('--sender', required=True, help='Sender email address')
    parser.add_argument('--password', required=True, help='Sender email password')
    parser.add_argument('--recipients', required=True, nargs='+', help='List of recipient email addresses')

    return parser.parse_args()

# 發送郵件的函數
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print("Message sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# 主函數
if __name__ == "__main__":
    args = get_args()
    send_email(args.subject, args.body, args.sender, args.recipients, args.password)
