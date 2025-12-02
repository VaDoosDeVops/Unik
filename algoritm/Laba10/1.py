table = []
i = 1
while i <= 10:
    row = []
    j = 1
    while j <= 10:
        row.append(i * j)
        j += 1
    table.append(row)
    i += 1

row_idx = 0
while row_idx < len(table):
    line = ""
    col_idx = 0
    while col_idx < len(table[row_idx]):
        num = table[row_idx][col_idx]
        line += f"{num:>3}"
        col_idx += 1
    print(line)
    row_idx += 1
