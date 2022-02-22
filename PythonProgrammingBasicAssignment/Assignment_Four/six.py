def get_sum_of_numbers(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

num = int(input('Enter a number: '))
print(get_sum_of_numbers(num))