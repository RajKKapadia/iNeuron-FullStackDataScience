def get_armstrong_numbers(num):
    a_num = []
    for i in range(1, num+1):
        orig_num = i
        result = 0
        while i > 0:
            r = i % 10
            result += r * r * r
            i = int(i / 10)

        if result == orig_num:
            a_num.append(orig_num)
    return a_num

num = int(input('Enter a number: '))
print(get_armstrong_numbers(num))