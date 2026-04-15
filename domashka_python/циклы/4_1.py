for x in range(41):
    n = x**2 + x + 41
    prime = True
    for i in range(2,  int(n**0.5) +1):
        if n % i == 0:
            prime = False
            break
        if prime:
            print(f"x = {x}, {n} - простое число")
        else:
            print(f"x = {x}, {n} - не простое число")