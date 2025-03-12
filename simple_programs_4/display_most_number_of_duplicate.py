numbers = []

while True:
    value = input('')
    try:
        value = int(value)
        if value >= 2:
            numbers.append(value)
    except ValueError:
        print('m')
        break
print(numbers)