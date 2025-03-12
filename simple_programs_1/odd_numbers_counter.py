counter = 0

for num in range(10):
    value = int(input())
    if value % 2 != 0:
        counter += 1
print(counter)