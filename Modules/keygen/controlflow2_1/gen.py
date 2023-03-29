import string
import secrets

letters = string.ascii_letters
digits = string.digits

alphabet = letters + digits
pwd_length = 16
pwd = ''

for i in range(pwd_length):
    if i==6:
        pwd += ''.join(secrets.choice('Y'))
    elif i==8:
        pwd += ''.join(secrets.choice('#'))
    elif i==10:
        pwd += ''.join(secrets.choice('A'))
    elif i==11:
        pwd += ''.join(secrets.choice('*'))
    elif i == 13:
        pwd += ''.join(secrets.choice('6'))
    else:
        pwd += ''.join(secrets.choice(alphabet))

print(pwd)
