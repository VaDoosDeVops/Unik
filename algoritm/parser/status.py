file = open("logs.txt", "r", encoding="utf-8")

status_count = {}
total_requests = 0

for line in file:
    total_requests += 1
    parts = line.split()
    status = parts[-3]

    if status in status_count:
        status_count[status] += 1
    else:
        status_count[status] = 1

file.close()

print("Статус-коды:")

for status, count in status_count.items():
    percent = (count / total_requests) * 100
    print(f"{status} - {count} запросов ({percent:.1f}%)")
