def custom_gcd(a, b):
    min_num = min(a, b)
    for i in range(min_num, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def custom_lcm(a, b):
    return a * b // custom_gcd(a, b)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"GCD of {num1} and {num2} is {custom_gcd(num1, num2)}")
print(f"LCM of {num1} and {num2} is {custom_lcm(num1, num2)}")

print(f"GCD of {num1} and {num2} is {gcd(num1, num2)}")
print(f"LCM of {num1} and {num2} is {lcm(num1, num2)}")