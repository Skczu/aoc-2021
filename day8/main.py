# a, b - 1
# a, b, c - 7
# a, b, c, d - 4
# a, b, c, d, e - 2, 3, 5
# a, b, c, d, e, f - 0, 6, 9
# a, b, c, d, e, f, g - 8
def part1(outputs):
  count = 0

  for output in outputs:
    for digit in output:
      if len(digit) in {2, 3, 4, 7}:
        count += 1

  return count


def part2(patterns, outputs):
  totalCount = 0
  for i in range(len(patterns)):
    digitMap = {}

    # 1, 4, 7, 8
    for digit in patterns[i]:
      if len(digit) == 2:
        digitMap[1] = digit
      elif len(digit) == 3:
        digitMap[7] = digit
      elif len(digit) == 4:
        digitMap[4] = digit
      elif len(digit) == 7:
        digitMap[8] = digit

    # 0, 6, 9
    for digit in patterns[i]:
      if len(digit) == 6:
        if set(digitMap[4]).issubset(set(digit)):
          digitMap[9] = digit
        elif set(digitMap[1]).issubset(set(digit)):
          digitMap[0] = digit
        else:
          digitMap[6] = digit

    # 2, 3, 5
    for digit in patterns[i]:
      if len(digit) == 5:
        if set(digitMap[1]).issubset(set(digit)):
          digitMap[3] = digit
        elif set(digit).issubset(set(digitMap[6])):
          digitMap[5] = digit
        else:
          digitMap[2] = digit

    num = []
    for digit in outputs[i]:
      for k, v in digitMap.items():
        if set(v) == set(digit):
          num.append(str(k))
    num = int(''.join(num))
    totalCount += num

  return totalCount


def main():
  patterns = []
  outputs = []
  with open("input.txt") as f:
    for line in f:
      display = [x.strip().split(" ") for x in line.split("|")]
      patterns.append(display[0])
      outputs.append(display[1])

  print(f"Answer to part 1: {part1(outputs)}")
  print(f"Answer to part 2: {part2(patterns, outputs)}")


if __name__ == "__main__":
  main()