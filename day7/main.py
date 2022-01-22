from statistics import mean, median


def part1(data):
  med = int(median(data))
  return sum(abs(med - pos) for pos in data)


def triangular_cost(steps):
  return (steps * (steps + 1) // 2)


def part2(data):
  meanPos = int(mean(data))
  return sum(triangular_cost(abs(meanPos - pos)) for pos in data)


def main():
  with open('input.txt') as f:
    data = [int(x) for x in f.readline().split(',')]
  print(f"Answer to part 1: {part1(data)}")
  print(f"Answer to part 2: {part2(data)}")


if __name__ == '__main__':
  main()