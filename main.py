import re
import requests

def is_valid_phone_number(phone_number):
    # Use regular expression to check if phone number is valid
    pattern = re.compile(r'^\+?\d{10,12}$')
    return pattern.match(phone_number)

def send_password_reset_email(email_address):
    # Use requests library to send password reset email
    response = requests.post('https://api.instagram.com/v1/accounts/password/reset/', data={'email': email_address})
    if response.status_code == 200:
        print('Password reset email sent successfully!')
    else:
        print('Error sending password reset email:', response.status_code)

def main():
    # Prompt user for Instagram username and phone number
    username = input('Enter your Instagram username: ')
    phone_number = input('Enter your phone number: ')

    # Check if phone number is valid
    if is_valid_phone_number(phone_number):
        # Send password reset email to user's email address
        email_address = f'{phone_number}@sms.instagram.com'
        send_password_reset_email(email_address)
    else:
        print('Invalid phone number. Please enter a valid phone number.')

if __name__ == '__main__':
    main()
    
    