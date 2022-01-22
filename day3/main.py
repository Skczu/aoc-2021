with open('input.txt') as f:
  data = [line.strip() for line in f.readlines()]

def r(n):
  input = data
  i = 0
  n2 = 0 if n else 1

  while(len(input) > 1):
    column = [int(x[i]) for x in input]
    d = n if sum(column) >= len(column) / 2 else n2
    input = [x for x in input if x[i] == str(d)]
    i += 1
    
  return input[0]

o2 = int(r(1), 2)
co2 = int(r(0), 2)
print(o2 * co2)