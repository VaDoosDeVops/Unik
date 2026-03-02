file = open("logs.txt", "r", encoding="utf-8")

path_count = {}

for line in file:
    request_part = line.split('"')[1]
    request_parts = request_part.split()
    path = request_parts[1]

    if path in path_count:
        path_count[path] += 1
    else:
        path_count[path] = 1

file.close()

sorted_paths = sorted(path_count.items(), key=lambda x: x[1], reverse=True)

print("Самые популярные пути:")

for path, count in sorted_paths[:3]:
    print(f"{path} - {count} запросов")
