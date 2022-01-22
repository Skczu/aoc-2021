data = []
with open('input.txt', 'r') as f:
  for line in f:
    data.append(int(line))

c = sum(x < y for x, y in zip(data, data[3:]))
print(c)