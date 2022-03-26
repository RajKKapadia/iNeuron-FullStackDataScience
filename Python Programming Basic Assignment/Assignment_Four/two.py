def display_table(num) -> None:

    for i in range(1, 11):

        print(f'{num} x {i} = {num*i}')

num = int(input('Enter a number: '))
display_table(num)