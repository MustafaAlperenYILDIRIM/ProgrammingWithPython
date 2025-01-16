def toplama(a, b):
    """
    Bu fonksiyon iki sayıyı toplar ve sonucu döndürür.
    Parametreler:
    a (int veya float): İlk sayı.
    b (int veya float): İkinci sayı.
    Dönüş:
    int veya float: Toplam sonucu.
    """
    return a + b


#print(toplama.__doc__)


def bolme(a, b):
    """
    İki sayıyı böler.

    Args:
        a (float): Bölünen sayı.
        b (float): Bölen sayı.

    Returns:
        float: Bölme sonucu.

    Raises:
        ZeroDivisionError: Eğer `b` sıfırsa hata fırlatılır.
    """
    if b == 0:
        raise ZeroDivisionError("Bölen sıfır olamaz.")
    return a / b

print(bolme.__doc__)