import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    with open(filePath + '\\' + fileName, 'r') as file:
      fileData = file.readlines()
  except:
    fileData = [];
    
  return fileData

def moveCursor(direction, map, row, column, movementCounter):
  chasingAnimal = True
  
  while chasingAnimal:
    nextMovement = directionMap[direction]
    dx, dy = nextMovement
    row = row + dx
    column = column + dy
    nextPipe = map[str(row) + ',' + str(column)]
    movementCounter += 1
    print(f'Moving from {direction} to {nextMovement} to {row}, {column} to {nextPipe}')
    direction = updateDirection(nextPipe, direction)
    if nextPipe == 'S':
      print(f'The number of moves is {int(movementCounter/2)}')
      chasingAnimal = False


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
 
landscapeMap = readInputFile('input.txt')
pipeMap = {}

mapRow = 0
mapColumn = 0
startingPoint = ''
directionMap = {'up': [-1, 0], 'down': [1,0], 'left': [0, -1], 'right': [0, 1]}

movementCounter = 1

for parcel in landscapeMap:
  mapRow += 1
  mapColumn = 0
  for character in parcel:
    mapColumn += 1 
    pipeMap[str(mapRow) + ',' + str(mapColumn)] = character
    if character == 'S':
      startingPoint = {'coordinates' : [mapRow, mapColumn]}

mapRow, mapColumn = startingPoint['coordinates']
currentDirection = 'right'
print(f'Starting at [{mapRow},{mapColumn}]')
moveCursor(currentDirection, pipeMap, mapRow, mapColumn, movementCounter)