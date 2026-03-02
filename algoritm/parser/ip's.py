file = open("logs.txt", "r", encoding="utf-8")

ip_count = {}
total_requests = 0

for line in file:
    total_requests += 1
    parts = line.split()
    ip = parts[0]

    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1

file.close()

sorted_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)

print("Топ-5 IP-адресов:")
for ip, count in sorted_ips[:5]:
    percent = (count / total_requests) * 100
    print(f"{ip} - {count} запросов ({percent:.1f}%)")
