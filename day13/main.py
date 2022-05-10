def print_points(points):
  max_x = max(x for x, _ in points)
  max_y = max(y for _, y in points)
  min_x = min(x for x, _ in points)
  min_y = min(y for _, y in points)
  for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
      if (x, y) in points:
        print('#', end='')
      else:
        print(' ', end='')
    print()

def fold(points, folds):
  for axis, n in folds:
    if axis == 'x':
      points = {
        (
          x if x < n else n - (x - n),
          y
        ) for x, y in points
      }
    elif axis == 'y':
      points = {
        (
          x,
          y if y < n else n - (y - n)
        ) for x, y in points
      }
    else:
      raise AssertionError(f"unexpected axis {axis}")
  return points

def main():
  with open('input.txt') as f:
    points_s, instructions = f.read().split('\n\n')

  sheet = set()
  for line in points_s.splitlines():
    x_s, y_s = line.strip().split(',')
    sheet.add((int(x_s), int(y_s)))
  folds = []
  for line in instructions.splitlines():
    instruction_s, n_s = line.split('=')
    folds.append((instruction_s[-1], int(n_s)))
  
  new_points = fold(sheet, folds)
  print_points(new_points)
  print(len(new_points))

if __name__ == '__main__':
  main()