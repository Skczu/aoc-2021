x = 0
y = 0
aim = 0
with open('input.txt') as f:
  for line in f:
    d = line.split()
    if d[0] == 'forward':
      x += int(d[1])
      y += int(d[1]) * aim
    elif d[0] == 'up':
      aim -= int(d[1])
    else:
      aim += int(d[1])

result = x * y
print(result)