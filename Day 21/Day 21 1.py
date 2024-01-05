import os
from collections import deque

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

farmMap = readInputFile('input.txt').strip().split('\n')
gardenPlots = {}
mapRow = 0
mapColumn = 0
startingPoint = ''
directionMap = {'N': [-1, 0], 'S': [1, 0], 'W': [0, -1], 'E': [0, 1]}

def walkAroundGarden(numberOfSteps):
  walkingPath = set()
  walkingPath.add(startingPoint)

  for _ in range(numberOfSteps):
    walkingPath = nextSteps(walkingPath)    

  return len(walkingPath)
    
def nextSteps(previousMovements):
  nextSteps = set()
  for position in previousMovements:
    for direction in 'NWES':
      row, column = position
      nextMovement = directionMap[direction]
      dx, dy = nextMovement
      row = row + dx
      column = column + dy
      newPosition = (row, column)
      #print(f'Moving {direction} {nextMovement} from {position} to {newPosition}')
      if newPosition not in gardenPlots or gardenPlots[newPosition] == '#':
        continue
      nextSteps.add(newPosition)

  return nextSteps 


for parcel in farmMap:
  mapColumn = 0
  for character in parcel:
    gardenPlots[(mapRow, mapColumn)] = character
    if character == 'S':
      startingPoint = (mapRow, mapColumn)
    mapColumn += 1 
  mapRow += 1

print(f'The number of garden plots reached is {walkAroundGarden(64)}')