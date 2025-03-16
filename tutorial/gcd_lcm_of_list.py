def custom_gcd(a, b):
    min_num = min(a, b)
    for i in range(min_num, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def custom_lcm(a, b):
    return a * b // custom_gcd(a, b)

def gcd_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = custom_gcd(result, num)
    return result

def lcm_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = custom_lcm(result, num)
    return result


numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print(f"GCD of the list is {gcd_of_list(numbers)}")
print(f"LCM of the list is {lcm_of_list(numbers)}")