numbers = []
for num in range(10):
    numbers.append(int(input()))

result = numbers[0]
for num in range(1,10):
    result -= numbers[num]
print(result)
