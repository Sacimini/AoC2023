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
    if character == pathTile:
      for direction in 'NEWS':
        nextMovement = directionMap[direction]
        dx, dy = nextMovement
        row = parcelIndex + dx
        column = characterIndex + dy
        #print(f'Moving from ({parcelIndex}, {characterIndex}) {direction} to ({row}, {column}) to {trailMap[row][column]})')

        if not (0 <= row < len(trailMap) and 0 <= column < len(parcel)):
           continue

        if trailMap[row][column] == pathTile:
           hikeRoute.setdefault((parcelIndex, characterIndex), set()).add((row, column))
           hikeRoute.setdefault((row, column), set()).add((parcelIndex, characterIndex))
    elif character == slopeRightTile:
      hikeRoute.setdefault((parcelIndex, characterIndex), set()).add((parcelIndex, characterIndex + 1))
      hikeRoute.setdefault((parcelIndex, characterIndex - 1), set()).add((parcelIndex, characterIndex))           
    elif character == slopeDownTile:
      hikeRoute.setdefault((parcelIndex, characterIndex), set()).add((parcelIndex + 1, characterIndex))
      hikeRoute.setdefault((parcelIndex - 1, characterIndex), set()).add((parcelIndex, characterIndex))           
         
trailMapLength = len(trailMap)
trailRowLength = len(trailMap[0])

visitedTiles = set()
longestHikeDistance = 0

queue =[(0, 1, 0)]

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

  for dx, dy in hikeRoute[(row, column)]:
     queue.append((dx, dy, distance + 1))

print(F'The most steps taken on a hike is {longestHikeDistance}')