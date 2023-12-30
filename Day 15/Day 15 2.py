import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

initializationSteps = readInputFile('input.txt').split(',')
boxes = [[] for x in range(0,256)]

addLensOperation = '='
removeLensOperation = '-'

results = []

for initializationStep in initializationSteps:
  lensLabel = ''
  lensAction = ''
  lensFocalLength = ''
  for character in initializationStep:
    if character.isalpha():
      lensLabel += character
    elif not character.isalnum():
      lensAction += character
    elif character.isdigit():
      lensFocalLength += character

  newLens = (lensLabel, lensFocalLength)
  currentValue = 0

  for character in lensLabel:
    currentValue += ord(character)
    currentValue *= 17
    currentValue %= 256

  if lensAction == addLensOperation:
    if lensLabel not in [box[0] for box in boxes[currentValue]]:
      boxes[currentValue].append(newLens)
    else:
      lensIndex = [box[0] for box in boxes[currentValue]].index(lensLabel)
      boxes[currentValue].pop(lensIndex)
      boxes[currentValue].insert(lensIndex, newLens)
  elif lensAction == removeLensOperation:
    if lensLabel in [box[0] for box in boxes[currentValue]]:
        boxes[currentValue].pop([box[0] for box in boxes[currentValue]].index(lensLabel)) 


focusingPower = 0
for boxIndex, box in enumerate(boxes):
  for lensIndex, lensLabel in enumerate(box):
    focusingPower += (boxIndex + 1) * (lensIndex + 1) * int(lensLabel[1])

print(f'The Focusing Power is {focusingPower}')