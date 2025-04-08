import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'unknown') == "Bilinmeyen işlem."

'''
Görev: Şu anda, 3 adet birim test uygulanmıştır:
Toplama ve bölme işlemlerinin doğruluğu ile bilinmeyen işlem test edilmektedir.
Göreviniz, aşağıdaki işlemler için en az iki test eklemektir:
1. Çıkarma
2. Çarpma
Ek olarak, farklı senaryolar için ek testler geliştirip yazarsanız harika olur!
'''
