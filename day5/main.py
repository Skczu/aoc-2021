with open('input.txt') as f:
  vents = [[[int(y) for y in x.split(',')] for x in line.rstrip().split(' -> ')] for line in f.readlines()]

temp_set = set()
end_set = set()

def get_incr(start, end):
  if start[0] < end[0]:
    x = 1
  elif start[0] > end[0]:
    x = -1
  else:
    x = 0
  if start[1] < end[1]:
    y = 1
  elif start[1] > end[1]:
    y = -1
  else:
    y = 0
  return [x, y]

def update_sets(vent):
  if vent in end_set:
    return 0
  elif vent in temp_set:
    temp_set.remove(vent)
    end_set.add(vent)
    return 1
  else:
    temp_set.add(vent)
    return 0

def map_line(coords):
  count = 0
  start = coords[0]
  end = coords[1]
  (x, y) = get_incr(start, end)

  first = tuple(start)
  count += update_sets(first)
  while start != end:
    start[0] += x
    start[1] += y
    vent = (start[0], start[1])
    count += update_sets(vent)
  return count


overlapping = 0
for vent in vents:
  overlapping += map_line(vent)
print(overlapping)