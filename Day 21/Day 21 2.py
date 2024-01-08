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

  return walkingPath
    
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
      x, y = newPosition
      a = x % len(farmMap[0])
      b = y % len(farmMap)
      if gardenPlots[(a,b)] == '#':
        continue
      nextSteps.add(newPosition)

  return nextSteps 

def calculateArea(visitedParcels):
  minX, minY, maxX, maxY = 0, 0, 0, 0
  for dx, dy in visitedParcels:
    minX = min(minX, dx)
    minY = min(minY, dy)
    maxX = max(maxX, dx)
    maxY = max(maxY, dy)
  area = int((maxX - minX + 1) / len(farmMap[0]))

  parcelTotals = []
  dx = minX
  dy = minY
  for rowIndex in range(area):
    row = []
    for columnIndex in range(area):
      parcels = 0
      for x1 in range(dx, dx + len(farmMap[0])):
        for y1 in range(dy, dy + len(farmMap)):
          if (x1, y1) in visitedParcels:
            parcels += 1
      row.append(parcels)
      dx += len(farmMap[0])
    parcelTotals.append(row)
    dx = minX
    dy += len(farmMap)

  return parcelTotals

def calculateParcels(area):
    parcels = 0

    oddParcels = area[2][2]
    evenParcels = area[2][1]
    s1 = area[0][1] + area[0][3] + area[4][1] + area[4][3]
    s2 = area[0][2] + area[2][0] + area[2][4] + area[4][2]
    s3 = area[1][1] + area[1][3] + area[3][1] + area[3][3]

    parcels = (s1 * n) + s2 + (s3 * (n-1)) + (evenParcels * n**2) + (oddParcels * (n-1)**2)
    return parcels

for parcel in farmMap:
  mapColumn = 0
  for character in parcel:
    gardenPlots[(mapRow, mapColumn)] = character
    if character == 'S':
      startingPoint = (mapRow, mapColumn)
    mapColumn += 1 
  mapRow += 1

visitedParcels = walkAroundGarden(int((len(farmMap[0]) - 1) / 2 + len(farmMap[0]) * 2))
area = calculateArea(visitedParcels)

stepsRequired = 26501365
n = int((stepsRequired - (len(farmMap[0]) - 1) / 2) / len(farmMap[0]))

print(f'The number of garden plots reached is {calculateParcels(area)}')