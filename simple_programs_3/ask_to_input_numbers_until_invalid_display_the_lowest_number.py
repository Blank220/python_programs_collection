numbers = []
while True:
    try:
        value = int(input())
        numbers.append(value)
        print(min(numbers))
    except ValueError:
        print('Invalid input....Exiting.')
        break
