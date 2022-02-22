def get_factorial(num):
    if num == 0:
        return 1
    else:
        sum = 1
        for i in range(1, num+1):
            sum *= i
        return sum

num = int(input('Enter a number: '))
print(get_factorial(num))
