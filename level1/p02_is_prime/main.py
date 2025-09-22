n = int(input("请输入一个正整数: "))

if n <= 1:
    print(f"{n} 不是素数")
elif n == 2:
    print(f"{n} 是素数")
elif n % 2 == 0:
    print(f"{n} 不是素数")
else:
    is_prime = True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} 是素数")
    else:
        print(f"{n} 不是素数")