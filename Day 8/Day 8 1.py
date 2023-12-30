import os
import re

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    with open(filePath + '\\' + fileName, 'r') as file:
      fileData = file.readlines()
  except:
    fileData = [];
    
  return fileData

mapCoordinates = readInputFile('input.txt')

coordinateMap = {}
stepsToDestination = []
finalDestinationKey = 'ZZZ'
nextStep = ''

for mapCoordinate in mapCoordinates:
  if mapCoordinate.strip():
    if re.findall('(=)', mapCoordinate):
        directions = re.findall('(?<=\=).*', mapCoordinate) 
        for direction in directions:
          coordinates = direction.replace('(', '').replace(')','').split(', ')        
          coordinateMap[mapCoordinate[0:mapCoordinate.index('=')-1]] = {'Left': coordinates[0].replace(' ',''), 'Right': coordinates[1].replace(' ','')}
          if nextStep == '': 
            # nextStep = mapCoordinate[0:mapCoordinate.index('=')-1]
            nextStep = 'AAA'
            stepsToDestination.append(nextStep)
    elif re.findall('^[^=]+$', mapCoordinate):
        steps = mapCoordinate.replace('\n', '')

stepCounter = 0
print(f'Starting at {nextStep}')
while finalDestinationKey != nextStep:
  if steps[stepCounter] == 'L':
    nextStep = coordinateMap[nextStep]['Left']
    print(f'Going Left to {nextStep}')
  elif steps[stepCounter] == 'R':  
    nextStep = coordinateMap[nextStep]['Right']
    print(f'Going Right to {nextStep}')

  if nextStep != finalDestinationKey: 
    stepsToDestination.append(nextStep)
    print(f'Next Step {nextStep}')
    stepCounter += 1
  if stepCounter >= len(steps): stepCounter = 0

print(f'The number of steps to reach {finalDestinationKey} is {len(stepsToDestination)} via {stepsToDestination}')