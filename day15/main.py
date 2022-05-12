import heapq
from collections import defaultdict

def part1(grid):
  N = len(grid)
  M = len(grid[0])

  cost = defaultdict(int)

  pq = [(0, 0, 0)]
  heapq.heapify(pq)
  visited = set()

  while len(pq) > 0:
    c, row, col = heapq.heappop(pq)

    if (row, col) in visited:
      continue
    visited.add((row, col))

    cost[(row, col)] = c

    if row == N - 1 and col == M - 1:
      break

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      rr = row + dr
      cc = col + dc
      if not (0 <= rr < N and 0 <= cc < M):
        continue

      heapq.heappush(pq, (c + grid[rr][cc], rr, cc))

  return cost[(N - 1, M - 1)]

def part2(grid):
  N = len(grid)
  M = len(grid[0])

  rows = N * 5
  cols = M * 5

  def get(r, c):
    x = (grid[r % N][c % M] +
          (r // N) + (c // M))
    return (x - 1) % 9 + 1

  cost = defaultdict(int)

  pq = [(0, 0, 0)]
  heapq.heapify(pq)
  visited = set()

  while len(pq) > 0:
    c, row, col = heapq.heappop(pq)

    if (row, col) in visited:
      continue
    visited.add((row, col))

    cost[(row, col)] = c

    if row == rows - 1 and col == cols - 1:
      break

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      rr = row + dr
      cc = col + dc
      if not (0 <= rr < rows and 0 <= cc < cols):
        continue

      heapq.heappush(pq, (c + get(rr, cc), rr, cc))

  return cost[(rows - 1, cols - 1)]

with open('input.txt') as f:
  raw_input = f.read().strip()
grid = [[int(x) for x in line] for line in raw_input.split('\n')]

print(f'Answer to part 1: {part1(grid)}')
print(f'Answer to part 2: {part2(grid)}')