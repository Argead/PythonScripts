#!/usr/bin/python3
"""
Generates a secure password based on the number of bytes specific in CLI args. Defaults to 36 bytes currently.
"""
import argparse
import secrets
import string

DEFAULT_BYTES = 36
ALPHABET = string.ascii_letters + string.digits + string.punctuation

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--bytes', help='Specify the number of bytes to use to generate the password', type=int, default=DEFAULT_BYTES)

args = parser.parse_args()
NUMBER_OF_BYTES = args.bytes

password = ''.join(secrets.choice(ALPHABET) for i in range(NUMBER_OF_BYTES))
print(password)


"""
Script can be improved in several ways:
1. allow user to restrict the ALPHABET used to generate the password
2. allow the user to suppress the print statement at the end of the script
3. allow the user to specify a file arg for the print statement to send it to a file or another script
"""
