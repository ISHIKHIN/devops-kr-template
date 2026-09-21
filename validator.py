# validator.py
def validate_phone(phone: str) -> bool:
    """Валидация российского телефона"""
    import re
    pattren = r'^\+?7\d{10}$'
    return bool(re.match(pattren, phone.replace('-', '').replace(' ', '')))



def validate_inn(inn: str) -> bool:
    """TODO: Валидация ИНН."""
    pass


def validate_email(email: str) -> bool:
    """Валидация email-адреса."""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))
