def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def goldbach_check(limit=100):
    print(f"验证哥德巴赫猜想在{limit}以内的正确性：")
    for even in range(4, limit + 1, 2):
        found = False
        for i in range(2, even):
            if is_prime(i) and is_prime(even - i):
                print(f"{even} = {i} + {even - i}")
                found = True
                break  
        
        if not found:
            print(f"错误！{even}不能表示为两个素数之和")
            return False
    
    print("验证成功！")
    return True

goldbach_check(100)