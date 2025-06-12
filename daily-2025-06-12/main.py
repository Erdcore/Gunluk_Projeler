# asal_kontrol.py

# Asal sayı: Sadece 1 ve kendisine bölünebilen, 1'den büyük doğal sayılardır.
# Örnek: 2, 3, 5, 7, 11, 13...

def asal_mi(sayi):
    """
    Verilen sayının asal olup olmadığını kontrol eder.
    :param sayi: Kontrol edilecek tamsayı
    :return: True (asal), False (asal değil)
    """
    if sayi <= 1:
        return False  # 1 ve daha küçük sayılar asal değildir
    if sayi == 2:
        return True  # 2 özel olarak asaldır
    if sayi % 2 == 0:
        return False  # 2 hariç çift sayılar asal değildir

    # 3'ten başlayarak sayının kareköküne kadar kontrol ederiz
    for i in range(3, int(sayi ** 0.5) + 1, 2):
        if sayi % i == 0:
            return False  # Bölünebiliyorsa asal değildir

    return True  # Hiçbir böleni yoksa asal kabul edilir


def main():
    try:
        # Kullanıcıdan bir sayı alınır
        girilen_sayi = int(input("Asal sayı kontrolü için bir tamsayı girin: "))

        # Kontrol ve çıktı
        if asal_mi(girilen_sayi):
            print(f"{girilen_sayi} bir asal sayıdır.")
        else:
            print(f"{girilen_sayi} bir asal sayı değildir.")
    except ValueError:
        print("Lütfen geçerli bir tamsayı girin!")


# Programın doğrudan çalıştırılıp çalıştırılmadığını kontrol eder
if __name__ == "__main__":
    main()
