import os
import re

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))

    return open(filePath + '\\' + fileName).read()
  except:
    return []


def countVariations(row, springCounts, grouping):
  if not row:
    return not springCounts and not grouping

  variationResults = 0

  if row[0] == '?':
     possibleCombinations = ['.', '#']
  else:
     possibleCombinations = row[0]
  
  for possibleCombination in possibleCombinations:
    if possibleCombination == '#':
      variationResults += countVariations(row[1:], springCounts, grouping + 1)
    else:
       if grouping > 0:
         if springCounts and springCounts[0] == grouping:
           variationResults += countVariations(row[1:], springCounts[1:], 0)
       else:
         variationResults = variationResults + countVariations(row[1:], springCounts, 0)
           
    return variationResults

springMap = readInputFile('practice.txt')
parsedSprings = []
springs = []

possibleCombinations = []

for spring in springMap.strip().split('\n'):
  parsedSprings.append(spring.split())

for spring in parsedSprings:
  damagedSpringsCounts = spring[1].split(',')
  damagedSpringsCounts = [int(damagedSpring) for damagedSpring in spring[1].split(',')]
  spring = [spring[0], tuple(map(int, spring[1].split(',')))]
  springs.append(('?'.join([spring[0]] * 5), spring[1] * 5))


for spring in springs:
  possibleCombinations.append(countVariations(spring[0], spring[1], 0))

print(f'The Sum of Possible Arrangements is {sum(possibleCombinations)}')
