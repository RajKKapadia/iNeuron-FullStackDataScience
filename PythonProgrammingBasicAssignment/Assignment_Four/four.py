def check_armstrong_number(num):
    result = 0
    orig_num = num
    while num > 0:
        r = num % 10
        result += r * r * r
        num = int(num / 10)

    if result == orig_num:
        print(f'{orig_num} is a Armstrong number.')
    else:
        print(f'{orig_num} is not a Armstrong number.')
    
num = int(input('Enter a number: '))
check_armstrong_number(num)