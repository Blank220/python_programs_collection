numbers = []
for num in range(10):
    value = int(input())
    if numbers.count(value) == 0:
        numbers.append(value)
print(numbers)