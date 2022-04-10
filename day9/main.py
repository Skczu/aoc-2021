def isLow(heightMap, i, j):
  if heightMap[i][j] == 9 or heightMap[i][j] == -1:
    return False
  if i != len(heightMap) - 1 and heightMap[i+1][j] < heightMap[i][j]:
    return False
  if i != 0 and heightMap[i-1][j] < heightMap[i][j]:
    return False
  if j != len(heightMap[0]) - 1 and heightMap[i][j+1] < heightMap[i][j]:
    return False
  if j != 0 and heightMap[i][j-1] < heightMap[i][j]:
    return False
  return True

def part1(heightMap):
  totalRiskLevel = 0
  for i in range(len(heightMap)):
    for j in range(len(heightMap[0])):
      if isLow(heightMap, i, j):
        totalRiskLevel += heightMap[i][j] + 1
  return totalRiskLevel

def checkPoint(heightMap, x, y):
  size = 0
  rightBound = len(heightMap[0])
  bottomBound = len(heightMap)
  if (heightMap[x][y] == 9 or heightMap[x][y] == -1):
    return size
  heightMap[x][y] = -1
  size += 1
  if x+1 < bottomBound:
    size += checkPoint(heightMap, x+1, y)
  if x-1 >= 0:
    size += checkPoint(heightMap, x-1, y)
  if y+1 < rightBound:
    size += checkPoint(heightMap, x, y+1)
  if y-1 >= 0:
    size += checkPoint(heightMap, x, y-1)
  return size

def part2(heightMap):
  basins = []
  for i in range(len(heightMap)):
    for j in range(len(heightMap[0])):
      if isLow(heightMap, i, j):
        basins.append(checkPoint(heightMap, i, j))
  sortedBasins = sorted(basins, reverse=True)
  return sortedBasins[0] * sortedBasins[1] * sortedBasins[2]

def main():
  with open("input.txt") as f:
    heightMap = [[int(x) for x in line.strip()] for line in f]
  print(f"Answer to part 1: {part1(heightMap)}")
  print(f"Answer to part 2: {part2(heightMap)}")

if __name__ == "__main__":
  main()