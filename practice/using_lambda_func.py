# Lambda fonksiyonları ile çift ve tek sayıları ayıran algoritma

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

print(f"Orijinal liste: {numbers}")
print(f"Çift sayılar: {even_numbers}")
print(f"Tek sayılar: {odd_numbers}")

# ------------------------------------------------------------------

users = [
    ("Ali", 25),
    ("Ayşe", 30),
    ("Mehmet", 17),
    ("Zeynep", 22),
    ("Fatma", 35),
    ("Ahmet", 16)
]

adult_users = list(filter(lambda user: user[1] >= 18, users))

print("Yetişkin kullanıcılar:")
for user in adult_users:
    print(user)

# ------------------------------------------------------------------

# Gönderi listesi (gönderi_id, beğeni_sayısı)
posts = [
    (1, 150),
    (2, 300),
    (3, 50),
    (4, 400),
    (5, 200)
]

# Gönderileri beğeni sayısına göre azalan sırada sıralama
sorted_posts = sorted(posts, key=lambda post: post[1], reverse=True)

print("Beğeni sayısına göre sıralanmış gönderiler:")
for post in sorted_posts:
    print(post)

# ------------------------------------------------------------------

# Kullanıcı adlarını büyük harfe çevir
uppercase_usernames = list(map(lambda username: username[0].upper(), users))

print("Büyük harfli kullanıcı adları:")
print(uppercase_usernames)

# ------------------------------------------------------------------

# Gönderi listesi (gönderi_id, etiketler)
posts = [
    (1, ["spor", "sağlık"]),
    (2, ["teknoloji", "bilim"]),
    (3, ["yemek", "gezi"]),
    (4, ["spor", "teknoloji"]),
    (5, ["moda", "güzellik"])
]

# "spor" etiketine sahip gönderileri filtrele
sports_posts = list(filter(lambda post: "spor" in post[1], posts))

print("Spor etiketi içeren gönderiler:")
for post in sports_posts:
    print(post)

# ------------------------------------------------------------------

from datetime import datetime

# Kullanıcı listesi (isim, son giriş tarihi)
user_lists = [
    ("Ali", "2025-03-01"),
    ("Ayşe", "2025-03-15"),
    ("Mehmet", "2024-12-25"),
    ("Zeynep", "2025-03-10"),
    ("Fatma", "2025-02-28")
]

# Bugünün tarihi
today = datetime.strptime("2025-03-20", "%Y-%m-%d")

# Son 30 gün içinde giriş yapan kullanıcıları filtrele
active_users = list(filter(lambda user: (today - datetime.strptime(user[1], "%Y-%m-%d")).days <= 30, user_lists))

print("Son 30 gün içinde aktif olan kullanıcılar:")
for user in active_users:
    print(user)

# ------------------------------------------------------------------

messages = [
    "Merhaba!",
    "Bugün hava çok güzel.",
    "Nasılsınız?",
    "Sosyal medya uygulamamıza hoş geldiniz!",
    "Teşekkürler!"
]

# Mesajları uzunluklarına göre sıralama
sorted_messages = sorted(messages, key=lambda msg: len(msg))

print("Uzunluklarına göre sıralanmış mesajlar:")
for message in sorted_messages:
    print(message)