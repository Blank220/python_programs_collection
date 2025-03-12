numbers = []

while True:
    value = input('')
    try:
        num = int(value)
        numbers.append(num)
    except ValueError:
        print('Invalid input...Exiting..')
        break
highest_duplicate = max(set(numbers), key=numbers.count)
print('Highest duplicate is: ', highest_duplicate)