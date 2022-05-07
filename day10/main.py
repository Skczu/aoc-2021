braces = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}

def part1(matrix):
  incomplete_lines = [row[:] for row in matrix]
  values = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
  }
  score = 0
  for line in matrix:
    open_chunks = []
    for char in line:
      if char in braces.keys():
        open_chunks.append(char)
      elif braces.get(open_chunks.pop()) != char:
        score += values.get(char)
        incomplete_lines.remove(line)
        break
  return (score, incomplete_lines)

def part2(matrix):
  values = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
  }
  scores = []
  for line in matrix:
    open_chunks = []
    score = 0
    for char in line:
      if char in braces.keys():
        open_chunks.append(char)
      elif braces.get(open_chunks[-1]) == char:
        open_chunks.pop()
    for char in reversed(open_chunks):
      score = (score * 5) + values.get(char)
    scores.append(score)
  scores = sorted(scores)
  return scores[len(scores)//2]

def main():
  with open("input.txt") as f:
    subsystem = [[x for x in line.strip()] for line in f.readlines()]
  part1_results = part1(subsystem)
  incomplete_lines = part1_results[1]
  print(f"Answer to part 1: {part1_results[0]}")
  print(f"Answer to part 2: {part2(incomplete_lines)}")
  

if __name__ == "__main__":
  main()