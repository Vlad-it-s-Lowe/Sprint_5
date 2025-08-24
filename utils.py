import random
import string

def generate_email():
    """Генерирует уникальный email в формате testXXX@ya.ru"""
    rand_num = random.randint(100, 9999)
    return f"test{rand_num}@ya.ru"

def generate_password(length=6):
    """Генерирует пароль с минимум 6 символов"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))