numbers = []
while True:
    value = input('')

    try:
        num = int(value)
        numbers.append(num)
    except ValueError:
        print("Invalid input....Exiting.")
        break

if numbers:
    print('Lowest number is', min(numbers))
else:
    print('No valid numbers were entered')