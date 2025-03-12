displayed_numbers = set()

while True:
    value = input('')
    
    try:
        number = int(value)
        if number in displayed_numbers:
            print('Duplicate')
        else:
            print('Unique')
            displayed_numbers.add(number)
    except ValueError:
        print('Invalid input.....Exit')
        break
