i = 1
j = 1

results = ["1", "1"]

for _ in range(18):
    i, j = j, i + j
    results.append(str(j))

print(", ".join(results))
