#Question: The following formula can be used to determine the distance an object falls due to gravity in a specific time period: d = 0.5 * g * t^2
#where d is the distance in meters, g is 9.8, and t is the time in seconds that the object has been falling. Write a function named falling_distance that accepts an object’s falling time (in seconds) as an argument. 
# The function should return the distance in meters that the object has fallen during that time period. Write a program that calls the function in a loop that passes the values 1 through 10 as arguments and displays the return value.

#answer 1 -----------------------------------------------------------------------------
def falling_distance(t):
    g = 9.8
    d = 0.5 * g * (t ** 2)
    return d

# 1'den 10'a kadar olan süreler için mesafeyi hesapla
for time in range(1, 11):
    print(f"{time} saniye → {falling_distance(time):.2f} metre")

#answer 2 -----------------------------------------------------------------------------
def falling_distance(t, g=9.8):
    return 0.5 * g * (t ** 2)

try:
    max_time = int(input("Kaç saniyeye kadar hesaplamak istiyorsunuz? "))
    for time in range(1, max_time + 1):
        print(f"{time} saniye → {falling_distance(time):.2f} metre")
except ValueError:
    print("Lütfen geçerli bir tam sayı girin!")