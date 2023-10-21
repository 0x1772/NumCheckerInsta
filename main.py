import re
import requests

def is_valid_phone_number(phone_number):
    # Use regular expression to check if phone number is valid
    pattern = re.compile(r'^\+?\d{10,12}$')
    return pattern.match(phone_number)

