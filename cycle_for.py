numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

#задачу можно решить с помощью множеств
for num in numbers:
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            flag = 0
            not_primes.append(num)
            break
        flag = 1
    if flag or num == 2:
        primes.append(num)

print("Primes:", primes)
print("Not primes:", not_primes)
