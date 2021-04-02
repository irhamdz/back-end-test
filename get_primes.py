def get_primes(num: int):
    result = []
    if num > 1:
        for n in range(2, num):
            for j in range(2, n):
                if n % j == 0:
                    break
            else:
                result.append(n)

    return result
