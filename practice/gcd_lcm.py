def gcd_iterative(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


# LCM(a, b) = (a * b) / GCD(a, b)
def lcm(a, b):
    return a * b // gcd_iterative(a, b)

if __name__ == "__main__":
    a = 48
    b = 18
    
    print(f"GCD({a}, {b}) = {gcd_iterative(a, b)}")
    print(f"GCD Recursive({a}, {b}) = {gcd_recursive(a, b)}")
    print(f"LCM({a}, {b}) = {lcm(a, b)}")
