numbers = []
for num in range(10):
    value = int(input())
    numbers.append(value)

duplicate_numbers = []
for num in set(numbers):
    if numbers.count(num) > 1:
        duplicate_numbers.append(num)
print(duplicate_numbers)