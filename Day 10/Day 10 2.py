import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    with open(filePath + '\\' + fileName, 'r') as file:
      fileData = file.readlines()
  except:
    fileData = [];
    
  return fileData

def checkSurroundings(map, row, column):
  for x,y in [(row+i,column+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
    try:
      coordinate = str(x) + ',' + str(y)
      if map[coordinate] == '.':
        if (x >= mazeBoundry['top'] and x <= mazeBoundry['bottom']) and (y >= mazeBoundry['left'] and y <= mazeBoundry['right']):
          map[coordinate] = 'I'
          enclosedTiles.append(coordinate)
        else:
          map[coordinate] = 'O'
    except:
      continue

def checkForLeaks(map):
  leakCounter = 1
  while leakCounter > 0:
    leakCounter = 0
    for coordinates in reversed(map):
      try:
        parsedCoordinates = coordinates.split(',')
        coordinateRow = int(parsedCoordinates[0])
        coordinateColumn = int(parsedCoordinates[1])
      
        if map[coordinates] == 'I':
          for x,y in [(coordinateRow+i,coordinateColumn+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
            if map[str(x) + ',' + str(y)] == 'O':
              map[coordinates] = 'O'
              leakCounter += 1
              enclosedTiles.remove(coordinates)
      except:
        continue

def setMazeBoundries(mazeBoundary, row, column):
  mazeBoundary['top'] = min(mazeBoundary['top'], row)
  mazeBoundary['bottom'] = max(mazeBoundary['bottom'], row)
  mazeBoundary['left'] = min(mazeBoundary['left'], column)
  mazeBoundary['right'] = max(mazeBoundary['right'], column)

def moveCursor(direction, map, row, column, movementCounter):
  chasingAnimal = True
  
  while chasingAnimal:
    nextMovement = directionMap[direction]
    dx, dy = nextMovement
    row = row + dx
    column = column + dy
    nextPipe = map[str(row) + ',' + str(column)]
    movementCounter += 1
    #print(f'Moving from {direction} to {nextMovement} to {row}, {column} to {nextPipe}')
    direction = updateDirection(nextPipe, direction)
    checkSurroundings(map, row, column)
    if nextPipe == 'S':
      #print(f'Starting at [{row},{column}]')
      #print(f'The number of moves is {int(movementCounter/2)}')
      chasingAnimal = False
  return enclosedTiles

def updateDirection(nextPipe, direction):
  if nextPipe == 'L':
    if direction == 'down':
      return 'right'
    elif direction == 'left':
      return 'up'
  elif nextPipe == 'J':
    if direction == 'down':
      return 'left'
    elif direction == 'right':
      return 'up'
  elif nextPipe ==  '7':
    if direction == 'right':
      return 'down'
    elif direction == 'up':
      return 'left'
  elif nextPipe == 'F':
    if direction == 'up':
      return 'right'
    elif direction == 'left':
      return 'down'
  
  return direction

	for r, row in enumerate(grid):
		inside = False

		for c, cell in enumerate(row):
			if (r, c) not in main_loop:
				area += inside
			else:
				inside = inside ^ (cell in '|F7')

	return area
landscapeMap = readInputFile('practice.txt')
pipeMap = {}

mapRow = 0
mapColumn = 0
startingPoint = ''
directionMap = {'up': [-1, 0], 'down': [1, 0], 'left': [0, -1], 'right': [0, 1]}
mazeBoundry = {'top': 999, 'bottom': 0, 'left': 999, 'right': 0}
movementCounter = 1
enclosedTiles = []

for parcel in landscapeMap:
  mapRow += 1
  mapColumn = 0
  for character in parcel:
    mapColumn += 1 
    pipeMap[str(mapRow) + ',' + str(mapColumn)] = character
    if character != '.' and character != '\n':
      setMazeBoundries(mazeBoundry, mapRow, mapColumn)
    if character == 'S':
      startingPoint = {'coordinates' : [mapRow, mapColumn]}

mapRow, mapColumn = startingPoint['coordinates']
currentDirection = 'right'
#print(f'Starting at [{mapRow},{mapColumn}]')
moveCursor(currentDirection, pipeMap, mapRow, mapColumn, movementCounter)
checkForLeaks(pipeMap)
print(f'The number of enclosed tiles is {len(enclosedTiles)}')
