def part1(heigthMap):
  totalRiskLevel = 0
  for i in range(len(heigthMap)):
    for j in range(len(heigthMap[0])):
      if heigthMap[i][j] == 9:
        continue
      if i != len(heigthMap) - 1 and heigthMap[i+1][j] < heigthMap[i][j]:
        continue
      if i != 0 and heigthMap[i-1][j] < heigthMap[i][j]:
        continue
      if j != len(heigthMap[0]) - 1 and heigthMap[i][j+1] < heigthMap[i][j]:
        continue
      if j != 0 and heigthMap[i][j-1] < heigthMap[i][j]:
        continue
      totalRiskLevel += heigthMap[i][j] + 1
  return totalRiskLevel


def main():
  with open("input.txt") as f:
    heigthMap = [[int(x) for x in line.strip()] for line in f]
  print(f"Answer to part 1: {part1(heigthMap)}")

if __name__ == "__main__":
  main()