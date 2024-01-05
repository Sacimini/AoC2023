import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []
  
gridLayout = []
gridMap = readInputFile('input.txt').strip()
for gridRow in gridMap.strip().split('\n'):
   gridLayout.append(list(gridRow))

directionMap = {'up': [-1, 0], 'down': [1,0], 'left': [0, -1], 'right': [0, 1]}   

def moveBeam(coordinates, direction, visitedTiles):
  if (coordinates, direction) not in visitedTiles:
      visitedTiles.add((coordinates, direction))

  while True:

    currentTile = gridLayout[coordinates[1]][coordinates[0]]
    if currentTile == '.':
      pass
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
      if direction == 'right':
        visited_coords = moveBeam(coordinates, 'up', visitedTiles)
        direction = 'down'
      elif direction == 'left':
        visited_coords = moveBeam(coordinates, 'up', visitedTiles)
        direction = 'down'
      elif direction == 'up':
        pass
      elif direction == 'down':
        pass
    elif currentTile == '-':
      if direction == 'right':
        pass
      elif direction == 'left':
        pass
      elif direction == 'up':
        visitedTiles = moveBeam(coordinates, 'left', visitedTiles)
        direction = 'right'
      elif direction == 'down':
        visitedTiles = moveBeam(coordinates, 'left', visitedTiles)
        direction = 'right'
    
    nextMovement = directionMap[direction]
    dx, dy = nextMovement
    coordinates = (coordinates[0] + dy, coordinates[1] + dx)

    if (coordinates, direction) in visitedTiles or coordinates[0] < 0 or coordinates[0] >= len(gridLayout[0]) or coordinates[1] < 0 or coordinates[1] >= len(gridLayout):
      break
    else:
      visitedTiles.add((coordinates, direction))

  return visitedTiles

mostEnergizedTiles = 0

for x in range(len(gridLayout[0])):
    visitedTiles = moveBeam((x,0), 'down', set())
    energizedTiles = set([x[0] for x in visitedTiles])
    mostEnergizedTiles = len(energizedTiles) if len(energizedTiles) > mostEnergizedTiles else mostEnergizedTiles

for x in range(len(gridLayout[0])):
    visitedTiles = moveBeam((x,len(gridLayout)-1), 'up', set())
    energizedTiles = set([x[0] for x in visitedTiles])
    mostEnergizedTiles = len(energizedTiles) if len(energizedTiles) > mostEnergizedTiles else mostEnergizedTiles

for y in range(len(gridLayout)):
    visitedTiles = moveBeam((0,y), 'right', set())
    energizedTiles = set([x[0] for x in visitedTiles])
    mostEnergizedTiles = len(energizedTiles) if len(energizedTiles) > mostEnergizedTiles else mostEnergizedTiles

for y in range(len(gridLayout)):
    visitedTiles = moveBeam((len(gridLayout[0])-1,y), 'left', set())
    energizedTiles = set([x[0] for x in visitedTiles])
    mostEnergizedTiles = len(energizedTiles) if len(energizedTiles) > mostEnergizedTiles else mostEnergizedTiles    

print(f'The most energized tiles are {mostEnergizedTiles}')

