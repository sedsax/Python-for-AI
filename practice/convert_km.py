# answer 1
# Kullanıcıdan kilometre değerini al
km = float(input("Kilometreyi girin: "))

# Mil dönüşümünü yap
miles = km * 0.6214

# Sonucu ekrana yazdır
print(f"{km} kilometre, {miles} mile eşittir.")


# answer 2 -----------------------------------------------------------------------------
def km_to_miles(km):
    """Kilometreyi mile çeviren fonksiyon"""
    return km * 0.6214

# Kullanıcıdan giriş al
try:
    km = float(input("Kilometreyi girin: "))
    print(f"{km} kilometre, {km_to_miles(km):.2f} mile eşittir.")
except ValueError:
    print("Lütfen geçerli bir sayı girin!")


# answer 3 -----------------------------------------------------------------------------
def km_to_miles():
    """Kullanıcıdan kilometre alıp mile çeviren fonksiyon"""
    while True:
        try:
            user_input = input("Kilometreyi girin (Çıkmak için 'q' yazın): ")
            if user_input.lower() == 'q':  # Kullanıcı 'q' yazarsa döngüyü kır
                print("Programdan çıkılıyor...")
                break
            km = float(user_input)  # Kullanıcıdan alınan değeri float'a çevir
            miles = km * 0.6214
            print(f"{km} kilometre, {miles:.2f} mile eşittir.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin veya çıkmak için 'q' yazın.")
        except KeyboardInterrupt:
            print("\nİşlem sonlandırıldı.")
            break

# Programı başlat
if __name__ == "__main__":
    km_to_miles()


