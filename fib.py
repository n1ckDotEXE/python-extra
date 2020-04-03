num = int(input('What is your number? '))

count = 1

fib1 = 0
fib2 = 1
fib3 = 0

print(fib1, end='')
print(fib2)

while count <= num:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    print(fib3)
    count += 1