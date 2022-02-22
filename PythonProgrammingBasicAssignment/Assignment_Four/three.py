def fibonacci_sequence(num) -> None:
    a = 0
    b = 1
    c = 0
    print(a)
    print(b)
    while c <= num:
        c = a + b
        print(c)
        a = b
        b = c

num = int(input('Enter a number: '))
fibonacci_sequence(num)
    