import random
import smtplib
from email.mime.text import MIMEText

# Generate OTP
def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[random.randint(0, 9)]
    return OTP

# Send OTP via Email
def send_otp_email(receiver_email, otp):
    sender_email = "your_email@gmail.com"  # Replace with your email address
    password = "your_password"  # Replace with your email password

    message = MIMEText(f"Your OTP is: {otp}")
    message['Subject'] = 'OTP Verification'
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("OTP sent successfully!")
        server.quit()
    except Exception as e:
        print("Failed to send OTP:", str(e))

# Main function
def main():
    receiver_email = input("Enter your email address: ")
    otp = generate_otp()
    send_otp_email(receiver_email, otp)
    user_input_otp = input("Enter the OTP you received: ")

    if user_input_otp == otp:
        print("OTP verification successful!")
    else:
        print("Invalid OTP!")

if __name__ == "__main__":
    main()
