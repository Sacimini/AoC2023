import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []
  
def tiltPlatform(platform, direction):
  roundRock = 'O'
  cubeRock = '#'
  emptySpace = '.'

  if direction == 'north':
    for row in range(len(platform)):
      for column in range(len(platform[0])):
        if platform[row][column] == roundRock:
          for surroundingRow in range(row - 1, -1, -1):
            if platform[surroundingRow][column] == cubeRock:
              break
            elif platform[surroundingRow][column] == emptySpace:
              platform[surroundingRow][column] = roundRock
              platform[surroundingRow + 1][column] = emptySpace
          else:
            platform[0][column] = emptySpace
  elif direction == 'west':
  elif direction == 'south':
  elif direction == 'east':
    

  return platform

platformMap = readInputFile('input.txt')
platform = []

roundRock = 'O'
cubeRock = '#'
emptySpace = '.'
totalLoad = 0

for item in platformMap.strip().split('\n'):
  platform.append(list(item))

platform.insert(0, ['#']*len(platform[0]))  
platform = tiltPlatform(platform, 'north')

for index, row in enumerate(platform[::-1]):
  for item in row:
    if item == roundRock:
      totalLoad += 1*(index+1)

print(f'The total load caused by all of the rounded rocks is {totalLoad}')