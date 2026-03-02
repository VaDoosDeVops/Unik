file = open("logs.txt", "r", encoding="utf-8")

total_size = 0

for line in file:
    parts = line.split()
    size = parts[-2]

    if size.isdigit():
        total_size += int(size)

file.close()

print("Общий размер ответов:")
print(total_size, "байт")
