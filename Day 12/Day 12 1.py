import os
import re
from itertools import product

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

springMap = readInputFile('practice.txt')
parsedSpringSections = []
springs = []

possibleCombinations = []

for spring in springMap.strip().split('\n'):
  parsedSpringSections.append(spring.split())

for spring in parsedSpringSections:
  damagedSpringCounts = spring[1].split(',')
  damagedSpringCounts = [int(damagedSpring) for damagedSpring in spring[1].split(',')]
  springs.append([spring[0], damagedSpringCounts])

def countVariations(row):
  variationResults = set()

  for item, counts in row:
    combinations = []
    for value in item:
      if value == '?':
        combinations.append(['#', '.'])
      else:
        combinations.append([value])

    for combo in product(*combinations):
      possibleCombination = ''.join(combo)
      matches = re.findall('#+', possibleCombination)
      matchLengths = [len(match) for match in matches]
      if matchLengths == counts:
        variationResults.add(possibleCombination)
  return len(variationResults)

for spring in springs:
  possibleCombinations.append(countVariations([spring]))

print(f'The Sum of Possible Arrangements is {sum(possibleCombinations)}')
