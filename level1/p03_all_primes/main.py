import time
import math

def find_primes_optimized(n):
    """
    埃拉托斯特尼筛法
    """
    if n < 2:
        return []
    
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            # 从i的平方开始标记，因为更小的倍数已经被之前的素数标记过了
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    # 收集所有素数
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

def find_primes_optimized_v2(n):
    """
    跳过偶数优化版
    """
    if n < 2:
        return []
    if n == 2:
        return [2]
    
    primes = [2]
    is_prime = [True] * ((n + 1) // 2) 
    
    #步长为2，只看技术
    for i in range(1, int(math.sqrt(n)) // 2 + 1):
        if is_prime[i]:
            current_odd = 2 * i + 1
            start = (current_odd * current_odd - 1) // 2
            step = current_odd
            for j in range(start, len(is_prime), step):
                is_prime[j] = False
    primes.extend(2 * i + 1 for i in range(1, len(is_prime)) if is_prime[i])
    return primes

def main():
    print("计算2-1000以内的所有素数：")
    print("=" * 50)
    start_time = time.time()
    primes1 = find_primes_optimized(1000)
    end_time = time.time()
    time1 = end_time - start_time
    print(f"方法1 - 优化筛法:")
    print(f"素数个数: {len(primes1)}")
    print(f"计算时间: {time1:.6f}秒")
    print(f"前10个素数: {primes1[:10]}")
    print(f"后10个素数: {primes1[-10:]}")
    print()
    
    start_time = time.time()
    primes2 = find_primes_optimized_v2(1000)
    end_time = time.time()
    time2 = end_time - start_time
    print(f"方法2 - 跳过偶数的优化筛法:")
    print(f"素数个数: {len(primes2)}")
    print(f"计算时间: {time2:.6f}秒")
    print(f"前10个素数: {primes2[:10]}")
    print(f"后10个素数: {primes2[-10:]}")
    print()
    
    # 打印
    print("所有素数:")
    print("-" * 50)
    for i in range(0, len(primes1), 10):
        print(" ".join(f"{prime:4d}" for prime in primes1[i:i+10]))
    
    print(f"\n总计找到 {len(primes1)} 个素数")
    print(f"最优算法计算时间: {min(time1, time2):.6f}秒")

if __name__ == "__main__":
    main()