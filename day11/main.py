directions = [
  (-1, -1),
  (1, 1),
  (0, 1),
  (1, 0),
  (0, -1),
  (-1, 0),
  (-1, 1),
  (1, -1)
]

def octoStep(matrix, x, y):
  if matrix[x][y] == -1:
    return
  matrix[x][y] += 1
  rightBound = len(matrix[0])
  bottomBound = len(matrix)
  if matrix[x][y] == 10:
    matrix[x][y] = -1
    for a, b in directions:
      newX = x + a
      newY = y + b
      if newX < bottomBound and newX >= 0 and newY < rightBound and newY >= 0:
        octoStep(matrix, newX, newY)

def part1(octos):
  matrix = [row[:] for row in octos]
  score = 0
  for x in range(100):
    for i in range(len(matrix)):
      for k in range(len(matrix[0])):
        octoStep(matrix, i, k)
    for i in range(len(matrix)):
      for k in range(len(matrix[0])):
        if matrix[i][k] == -1:
          score += 1
          matrix[i][k] = 0
  return score

def part2(octos):
  matrix = [row[:] for row in octos]
  step = 0
  while True:
    score = 0
    for i in range(len(matrix)):
      for k in range(len(matrix[0])):
        octoStep(matrix, i, k)
    for i in range(len(matrix)):
      for k in range(len(matrix[0])):
        if matrix[i][k] == -1:
          score += 1
          matrix[i][k] = 0
    step += 1
    if score == 100:
      return step

def main():
  with open('input.txt') as f:
    octos = [[int(x) for x in line.strip()] for line in f.readlines()]
  print(f"Answer to part 1: {part1(octos)}")
  print(f"Answer to part 2: {part2(octos)}")

if __name__ == '__main__':
  main()