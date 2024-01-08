import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []
  
trailMap = readInputFile('input.txt').strip().split('\n')
directionMap = {'N': [-1, 0], 'S': [1, 0], 'W': [0, -1], 'E': [0, 1]}

pathTile = '.'
forestTile = '#'
slopeUpTile = '^'
slopeRightTile = '>'
slopeDownTile = 'v'
slopeLeftTile = '<'

hikeRoute = {}
for parcelIndex, parcel in enumerate(trailMap):
  for characterIndex, character in enumerate(parcel):
    if character in [pathTile, slopeRightTile, slopeDownTile]:
      for direction in 'NEWS':
        nextMovement = directionMap[direction]
        dx, dy = nextMovement
        row = parcelIndex + dx
        column = characterIndex + dy
        if not (0 <= row < len(trailMap) and 0 <= column < len(parcel)):
           continue

        if trailMap[row][column] in [pathTile, slopeRightTile, slopeDownTile]:
           hikeRoute.setdefault((parcelIndex, characterIndex), set()).add((row, column, 1))
           hikeRoute.setdefault((row, column), set()).add((parcelIndex, characterIndex, 1))

while True:
  for coordinates, routePoints in hikeRoute.items():
    if len(routePoints) == 2:
      dataSetA, dataSetB = routePoints
      hikeRoute[dataSetA[:2]].remove(coordinates + (dataSetA[2],))
      hikeRoute[dataSetB[:2]].remove(coordinates + (dataSetB[2],))
      hikeRoute[dataSetA[:2]].add((dataSetB[0], dataSetB[1], dataSetA[2] + dataSetB[2]))
      hikeRoute[dataSetB[:2]].add((dataSetA[0], dataSetA[1], dataSetA[2] + dataSetB[2]))

      del hikeRoute[coordinates]
      break
  else:
    break
         
trailMapLength = len(trailMap)
trailRowLength = len(trailMap[0])

visitedTiles = set()
longestHikeDistance = 0

queue = [(0, 1, 0)]

while queue:
  row, column, distance = queue.pop()
  if distance == -1:
     visitedTiles.remove((row, column))
     continue
  if (row, column) == (trailMapLength - 1, trailRowLength - 2):
    longestHikeDistance = max(longestHikeDistance, distance)
    continue
  if (row, column) in visitedTiles:
    continue

  visitedTiles.add((row, column))
  queue.append((row, column, -1))

  for dx, dy, dz in hikeRoute[(row, column)]:
     queue.append((dx, dy, distance + dz))

print(F'The most steps taken on a hike is {longestHikeDistance}')