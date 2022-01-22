with open('input.txt') as f:
  vents = [[[int(y) for y in x.split(',')] for x in line.rstrip().split(' -> ')] for line in f.readlines()]

temp_set = set()
end_set = set()

def map_line(coords):
  start = coords[0]
  end = coords[1]
  count = 0
  if start[0] == end[0]:
    isX = start[0]
  elif start[1] == end[1]:
    isY = start[1]
    isX = False
  else:
    return 0

  start_i = min(start[1], end[1]) if isX else min(start[0], end[0])
  end_i = max(start[1], end[1]) if isX else max(start[0], end[0])
  for i in range(start_i, end_i+1):
    if isX:
      vent = (isX, i)
    else:
      vent = (i, isY)
    if vent in end_set:
      continue
    elif vent in temp_set:
      count += 1
      temp_set.remove(vent)
      end_set.add(vent)
    else:
      temp_set.add(vent)
  return count

overlapping = 0
for vent in vents:
  overlapping += map_line(vent)
print(overlapping)