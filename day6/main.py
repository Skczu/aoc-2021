# Brutal solution, make a coffee or build a house while waiting
# for j in range(256):
#   new_fish = []
#   for i in range(len(fish)):
#     if fish[i] == 0:
#       fish[i] = 6
#       new_fish.append(8)
#     else:
#       fish[i] -= 1
#   fish += new_fish

def calc_growth(initial_state, days):
  new_state = {}
  if days > 0:
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 0]:
      if i == 0 and initial_state.get(i):
        new_state[8] = initial_state[i]
        if new_state.get(6):
          new_state[6] += initial_state[i]
        else:
          new_state[6] = initial_state[i]
      elif i > 0 and initial_state.get(i):
        new_state[i - 1] = initial_state[i]
    return calc_growth(new_state, days - 1)
  else:
    return initial_state


def main():
  days = 256
  initial_state = {}
  result_state = {}
  with open('input.txt') as f:
    fish = [int(x) for x in f.readline().strip().split(',')]
  for item in fish:
    if initial_state.get(item):
      initial_state[item] += 1
    else:
      initial_state[item] = 1
  qty = 0
  result_state = calc_growth(initial_state, days)
  for key in result_state:
    qty += result_state[key]
  print(qty)

if __name__ == "__main__":
  main()