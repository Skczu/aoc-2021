from collections import defaultdict
from collections import deque

# current: BFS (using deque)
# comments represent DFS

def part1(edges):
  all_paths = set()
  todo = deque([('start',)])
  # todo = [('start',)]
  while todo:
    path = todo.popleft()
    # path = todo.pop()

    if path[-1] == 'end':
      all_paths.add(path)
      continue

    for cand in edges[path[-1]]:
      if not cand.islower() or cand not in path:
        todo.append((*path, cand))

  return len(all_paths)

def part2(edges):
  all_paths = set()
  todo = deque([(('start',), False)])
  # todo = [(('start',), False)]
  while todo:
    path, double_small = todo.popleft()
    # path, double_small = todo.pop()

    if path[-1] == 'end':
      all_paths.add(path)
      continue

    for cand in edges[path[-1]]:
      if cand == 'start':
        continue
      elif cand.isupper() or cand not in path:
        todo.append(((*path, cand), double_small))
      elif not double_small:
        todo.append(((*path, cand), True))

  return len(all_paths)

def main():
  input = defaultdict(set)
  with open('input.txt') as f:
    for line in f.readlines():
      a, b = line.strip().split('-')
      input[a].add(b)
      input[b].add(a)
  print(f"Answer to part 1: {part1(input)}")
  print(f"Answer to part 2: {part2(input)}")

if __name__ == '__main__':
  main()