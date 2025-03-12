numbers = []

while True:
    value = input('')
    try:
        value = int(value)
        numbers.append(value)
        if numbers.count(value) >= 2:
            numbers.append(value)
    except ValueError:
        print('m')
        break
print(numbers)