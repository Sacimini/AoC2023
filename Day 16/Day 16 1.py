import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

gridLayout = readInputFile('practice.txt').strip().split('\n')

directionMap = {'up': [-1, 0], 'down': [1,0], 'left': [0, -1], 'right': [0, 1]}   

def moveBeam(coordinates, direction, energizedTiles):
  if (coordinates, direction) not in energizedTiles:
    energizedTiles.add((coordinates, direction))
    print(f'Moving {direction} to {coordinates} tile {gridLayout[coordinates[0]][coordinates[1]]}')

  while True:
    direction = updateDirection(gridLayout[coordinates[0]][coordinates[1]], coordinates, direction, energizedTiles)
    nextMovement = directionMap[direction]
    dx, dy = nextMovement
    coordinates = (coordinates[0] + dx, coordinates[1] + dy)
    if( coordinates, direction) in energizedTiles or coordinates[0] < 0 or coordinates[0] >= len(gridLayout[0]) or coordinates[1] < 0 or coordinates[1] >= len(gridLayout):
      break
    else:
      energizedTiles.add((coordinates, direction))
      print(f'Moving {direction} to {coordinates} tile {gridLayout[coordinates[0]][coordinates[1]]}')

  return energizedTiles


def updateDirection(currentTile, coordinates, direction, energizedTiles):
  if currentTile == '.':
    return direction
  elif currentTile == '/':
    if direction == 'right':
        direction = 'up'
    elif direction == 'left':
        direction = 'down'
    elif direction == 'up':
        direction = 'right'
    elif direction == 'down':
        direction = 'left'
  elif currentTile == '\\':
    if direction == 'right':
        direction = 'down'
    elif direction == 'left':
        direction = 'up'
    elif direction == 'up':
        direction = 'left'
    elif direction == 'down':
        direction = 'right'
  elif currentTile == '|':
    if direction == 'right' or direction == 'left':
      energizedTiles = moveBeam(coordinates, 'up', energizedTiles)
      direction = 'down'
    elif direction == 'up' or direction == 'down':
      return direction
  elif currentTile == '-':
    if direction == 'right' or direction == 'left':
      return direction
    elif direction == 'up' or direction == 'down':
      energizedTiles = moveBeam(coordinates, 'left', energizedTiles)
      direction = 'right'

  return direction

energizedTiles = moveBeam((0,4), 'left', set())
print(f'The number of energized tiles is {len(set([tiles[0] for tiles in energizedTiles]))}')
