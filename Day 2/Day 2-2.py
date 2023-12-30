import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    with open(filePath + '\\' + fileName, 'r') as file:
      fileData = file.readlines()
  except:
    fileData = [];
    
  return fileData

def multiplyGameCubeValues(gameCubes):
  result = 1
  for gameCubeColor in gameCubes.keys():
    result *= int(gameCubes[gameCubeColor])

  return result

totalGamesPlayed = readInputFile('input.txt')
gameCubeSetPowerSum = 0

for gamePlayed in totalGamesPlayed:
  parsedGame = gamePlayed.split(':')
  if len(parsedGame) > 0:
    gameID = int(parsedGame[0].replace('Game', '').replace(' ', ''))
    gameResults = parsedGame[1].split(';')
    minimumAmountofGameCubes = {'red': 0, 'green': 0, 'blue': 0}
    for gameResult in gameResults:
      gameCubes = gameResult.split(',')
      for gameCube in gameCubes:
        gameCubeValue = ''
        gameCubeColor = ''
        for character in gameCube:
          if character.isnumeric():
            gameCubeValue += character
          elif character.isalpha():  
            gameCubeColor += character
        if int(gameCubeValue) > minimumAmountofGameCubes[gameCubeColor]:
          minimumAmountofGameCubes[gameCubeColor] = int(gameCubeValue)
    gameCubeSetPower = multiplyGameCubeValues(minimumAmountofGameCubes)      
    gameCubeSetPowerSum += gameCubeSetPower
    print(f'Game {gameID} Minimum Amount of Game Cubes Needed {minimumAmountofGameCubes} with a Power of {gameCubeSetPower} Running Total is {gameCubeSetPowerSum}')
