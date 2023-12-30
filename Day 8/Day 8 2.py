import os
import re
import math

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
startingNodes = []
endingNodes = []
nextStep = ''
allPossibleRoutes = []

for mapCoordinate in mapCoordinates:
  if mapCoordinate.strip():
    if re.findall('(=)', mapCoordinate):
        directions = re.findall('(?<=\=).*', mapCoordinate) 
        for direction in directions:
          coordinates = direction.replace('(', '').replace(')','').split(', ')
          coordinateKey = mapCoordinate[0:mapCoordinate.index('=')-1]        
          coordinateMap[coordinateKey] = {'Left': coordinates[0].replace(' ',''), 'Right': coordinates[1].replace(' ','')}
          if coordinateKey[-1] == 'A':
            startingNodes.append(coordinateKey)
          elif coordinateKey[-1] == 'Z':
            endingNodes.append(coordinateKey)
    elif re.findall('^[^=]+$', mapCoordinate):
        steps = mapCoordinate.replace('\n', '')


for startingNode in startingNodes:
  nextStep = startingNode
  stepsToDestination.clear()
  stepsToDestination.append(nextStep)
  #print(f'Starting at {nextStep}')

  stepCounter = 0
  while not nextStep in endingNodes:
    if steps[stepCounter] == 'L':
      nextStep = coordinateMap[nextStep]['Left']
      #print(f'Going Left to {nextStep}')
    elif steps[stepCounter] == 'R':  
      nextStep = coordinateMap[nextStep]['Right']
      #print(f'Going Right to {nextStep}')

    if not nextStep in endingNodes: 
      stepsToDestination.append(nextStep)
      #print(f'Next Step {nextStep}')
      stepCounter += 1
    if stepCounter >= len(steps): stepCounter = 0
  #print(f'The number of steps to reach {nextStep} from {startingNode} is {len(stepsToDestination)} via {stepsToDestination}')
  print(f'The number of steps to reach {nextStep} from {startingNode} is {len(stepsToDestination)}')
  allPossibleRoutes.append(len(stepsToDestination))

print(f'The shortest route to all ending nodes is {math.lcm(*allPossibleRoutes)}')