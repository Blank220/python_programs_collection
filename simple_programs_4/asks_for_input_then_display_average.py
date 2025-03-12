numbers = []
while True:
    value = input('')
    try:
        num = int(value)
        numbers.append(num)
    except ValueError:
        print('Invalid input....Exiting..')
        break
average = sum(numbers) / len(numbers)
print('The Computed Average is: ', average)