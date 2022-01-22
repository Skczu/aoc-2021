with open('input.txt') as f:
  drawn = f.readline().strip().split(',')
  lines = (line.rstrip() for line in f)
  lines = list(line for line in lines if line)

tables = []
z = 0
for i in range(int(len(lines) / 5)):
  table = []
  for j in range(z, z+5):
    row = [x.strip() for x in lines[j].split()]
    table.append(row)
  tables.append(table)
  z += 5

def update_board(board, n):
  for i in range(5):
    for j in range(5):
      if board[i][j] == n:
        board[i][j] = 'g'

def check_board(board):
  for i in range(5):
    x = 0
    y = 0
    for j in range(5):
      if board[i][j] == 'g':
        x += 1
      if board[j][i] == 'g':
        y += 1
      if x == 5 or y == 5:
        return True
  return False

def calc_score(board):
  score = 0
  for i in range(5):
    for j in range(5):
      if board[i][j] != 'g':
        score += int(board[i][j])
  return score

for i in range(len(drawn)):
  for j in range(len(tables)):
    if tables[j] != 'w':
      update_board(tables[j], drawn[i])
      if check_board(tables[j]):
        score = calc_score(tables[j])
        print(score * int(drawn[i]))
        tables[j] = 'w'