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
    for row in range(len(platform)):
      for column in range(len(platform[0])):
        if platform[row][column] == roundRock:
          for surroundingRow in range(column - 1, -1, -1):
            if platform[row][surroundingRow] == cubeRock:
              break
            elif platform[row][surroundingRow] == emptySpace:
              platform[row][surroundingRow] = roundRock
              platform[row][surroundingRow + 1] = emptySpace
          else:
            platform[row][0] = emptySpace    
  elif direction == 'south':
    for row in range(len(platform) - 1, -1, -1):
      for column in range(len(platform[0])):
        if platform[row][column] == roundRock:
          for surroundingRow in range(row + 1, len(platform)):
            if platform[surroundingRow][column] == cubeRock:
              break
            elif platform[surroundingRow][column] == emptySpace:
              platform[surroundingRow][column] = roundRock
              platform[surroundingRow - 1][column] = emptySpace
          else:
            platform[-1][column] = emptySpace  
  elif direction == 'east':
    for row in range(len(platform)):
      for column in range(len(platform[0]) - 1, -1, -1):
        if platform[row][column] == roundRock:
          for surroundingRow in range(column + 1, len(platform[0])):
            if platform[row][surroundingRow] == cubeRock:
              break
            elif platform[row][surroundingRow] == emptySpace:
              platform[row][surroundingRow] = roundRock
              platform[row][surroundingRow - 1] = emptySpace
          else:
            platform[row][-1] = emptySpace  
    
  return platform

def convertPlatformToString(platforn):
  return 'y'.join(['x'.join(x) for x in platform])

def convertStringToPlatform(string):
  return [x.split('x') for x in string.split('y')]

platformMap = [['#'] + list(row) + ['#'] for row in readInputFile('input.txt').strip().split('\n')]
platformMap.insert(0, ['#'] * len(platformMap[0]))
platformMap.append(['#'] * len(platformMap[0]))
platform = []

roundRock = 'O'
cubeRock = '#'
emptySpace = '.'
numberOfCycles = 1000000000
totalLoad = 0

for item in platformMap:
  platform.append(list(item))


savedPlatforms = [convertPlatformToString(platform)]
while True:
  platform = tiltPlatform(platform, 'north')
  platform = tiltPlatform(platform, 'west')
  platform = tiltPlatform(platform, 'south')
  platform = tiltPlatform(platform, 'east')
  if convertPlatformToString(platform) in savedPlatforms:
    break
  savedPlatforms.append(convertPlatformToString(platform))

firstMatch = savedPlatforms.index(convertPlatformToString(platform))
cycles = len(savedPlatforms) - firstMatch
platform = convertStringToPlatform(savedPlatforms[(numberOfCycles - firstMatch) % cycles + firstMatch])

for index, row in enumerate(platform[::-1]):
  for item in row:
    if item == roundRock:
      totalLoad += 1 * index

print(f'The total load on the north support beam caused by all of the rounded rocks is {totalLoad} after {numberOfCycles} Cycles')
