# my_module.py -> another_file.py dosyasına başka bir modül olarak içe aktarılır.
def greet():
    print("Merhaba, dünya!")

def main():
    print("Bu dosya doğrudan çalıştırıldı.")
    greet()

if __name__ == "__main__":
    main()  # Bu dosya doğrudan çalıştırıldığında main() fonksiyonu çağrılır.
else:
    print("Bu dosya başka bir modül olarak içe aktarıldı.") 

"""
NOTE
Python'da ,f __name__ == "__main__" ifadesi, bir betiğin doğrudan çalıştırılıp çalıştırılmadığını veya başka bir betik tarafından modül olarak içe aktarılıp 
aktarılmadığını belirlemek için kullanılır. Bu ifade sayesinde, bir dosyanın içe aktarılması sırasında çalıştırılmasını istemediğiniz 
kodları kontrol edebilirsiniz. 

Bu, genellikle bir dosyanın hem modül olarak kullanılmasını hem de doğrudan çalıştırılmasını sağlamak için kullanılır.
__name__ değişkeni: Python her bir betiğe bir __name__ değişkeni atar. Eğer bir dosya doğrudan çalıştırılıyorsa, __name__  değişkeni "__main__" değerini alır. 
Eğer dosya bir modül olarak içe aktarılmışsa, __name__ değişkeni, dosyanın adı olur.
"""