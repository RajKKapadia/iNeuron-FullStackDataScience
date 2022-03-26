def check_prime_number(num):

    if num == 0:
        return 'Input must be greater than zero.'
    elif num == 1:
        return '1 is a prime number.'
    elif num % 2 == 0 or num % 3 == 0:
        return f'{num} is not a prime number.'

    i = 5

    while i ** 2 <= num:

        if num % i == 0 or num % (i+2) == 0:
            return f'{num} is not a prime number.'

        i += 6
    return f'{num} is a prime number.'

a = int(input('Enter a number: '))
print(check_prime_number(a))
