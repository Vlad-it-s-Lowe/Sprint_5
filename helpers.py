import random
import string

def create_random_email():
    random_letters = ''.join((random.choice(string.ascii_letters) for x in range(4)))
    random_email = f'kristina_bragina_5_{random_letters}_{random.randint(100, 999)}@yandex.ru'
    return random_email

def create_random_password():
    random_letters = ''.join((random.choice(string.ascii_letters) for x in range(2)))
    random_password = f'qwerty_{random_letters}_{random.randint(10, 99)}'
    return random_password

def create_email_base():
    random_letters = ''.join((random.choice(string.ascii_letters) for x in range(4)))
    email_base = f'kristina_bragina_5_{random_letters}_{random.randint(100, 999)}'
    return email_base