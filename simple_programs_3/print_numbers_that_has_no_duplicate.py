numbers = []
for num in range(10):
    value = int(input())
    numbers.append(value)

unique_numbers = []
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)
print(unique_numbers)