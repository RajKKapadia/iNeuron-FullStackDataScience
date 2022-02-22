def check_prime_number(num):

    if num == 0:
        pass
    elif num == 1:
        print(num)
    elif num % 2 == 0 or num % 3 == 0:
        pass
    else:
        i = 5
        while i ** 2 <= num:
            if num % i == 0 or num % (i+2) == 0:
                pass
            i += 6
        print(num)

for i in range(1, 10000):
    check_prime_number(i)
