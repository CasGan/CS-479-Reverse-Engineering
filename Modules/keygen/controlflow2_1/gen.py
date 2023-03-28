import string
# import random 
# import numpy as np

import secrets

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

pwd_length = 16
pwd = ''

for i in range(pwd_length):
    if i==0:
        pwd += ''.join(secrets.choice('A'))
    elif i==1:
        pwd += ''.join(secrets.choice('6'))
    elif i==3:
        pwd += ''.join(secrets.choice('2'))
    elif i==7:
        pwd += ''.join(secrets.choice('%'))
    elif i == 15:
        pwd += ''.join(secrets.choice('*'))
    else:
        pwd += ''.join(secrets.choice(alphabet))

print(pwd)
