import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

initializationSteps = readInputFile('input.txt').split(',')
results = []

for initializationStep in initializationSteps:
  currentValue = 0
  for character in initializationStep:
    currentValue += ord(character)
    currentValue *= 17
    currentValue %= 256
  results.append(currentValue)

print(f'The sum of the initialization sequence is {sum(results)}')