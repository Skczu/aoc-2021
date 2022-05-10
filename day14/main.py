from collections import Counter

def polymerization(polymer, rules):
  pair_counts = Counter()
  for i in range(len(polymer)-1):
    pair_counts[polymer[i:i+2]] += 1

  for _ in range(40):
    new_counts = Counter()
    char_counts = Counter()
    for k, v in pair_counts.items():
      new_counts[f'{k[0]}{rules[k]}'] += v
      new_counts[f'{rules[k]}{k[1]}'] += v

      char_counts[k[0]] += v
      char_counts[rules[k]] += v
    
    pair_counts = new_counts
  
  char_counts[polymer[-1]] += 1

  return max(char_counts.values()) - min(char_counts.values())

def main():
  with open('input.txt') as f:
    template, insertion_rules_s = f.read().split('\n\n')
  insertion_rules = {}
  for line in insertion_rules_s.splitlines():
    pair, result = line.split(' -> ')
    insertion_rules[pair] = result

  print(polymerization(template, insertion_rules))

if __name__ == '__main__':
  main()