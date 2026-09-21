# tests/test_validator.py
def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False

def test_validate_phone():
    assert validate_phone("+79991234567") == True
    assert validate_phone("89991234567") == False
    assert validate_phone("+7999123") == False

def test_validate_snils():
    """Валидные СНИЛС (рассчитаны по алгоритму)"""
    assert validate_snils("11223344595") == True
    assert validate_snils("001-001-999 32") == True
    
    """Невалидные: неверный формат"""
    assert validate_snils("123") == False
    assert validate_snils("123456789012") == False
    assert validate_snils("abcdefghijk") == False
    
    """Невалидные: неверная контрольная сумма"""
    assert validate_snils("11223344500") == False
>>>>>>> upstream/feature/instructor-change
