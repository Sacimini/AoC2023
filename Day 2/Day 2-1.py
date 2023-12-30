import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    with open(filePath + '\\' + fileName, 'r') as file:
      fileData = file.readlines()
  except:
    fileData = [];
    
  return fileData

totalAvailableGameCubes = {
  'red': 12,
  'green': 13,
  'blue': 14
}

totalGamesPlayed = readInputFile('input.txt')
possibleGameIDs = list(range(1, len(totalGamesPlayed)+1))

for gamePlayed in totalGamesPlayed:
  parsedGame = gamePlayed.split(':')
  if len(parsedGame) > 0:
    gameID = int(parsedGame[0].replace('Game', '').replace(' ', ''))
    gameResults = parsedGame[1].split(';')
    for gameResult in gameResults:
      gameCubes = gameResult.split(',')
      for gameCube in gameCubes:
        if gameID not in possibleGameIDs:
          break
        gameCubeValue = ''
        gameCubeColor = ''
        for character in gameCube:
          if character.isnumeric():
            gameCubeValue += character
          elif character.isalpha():  
            gameCubeColor += character
        if int(gameCubeValue) > totalAvailableGameCubes[gameCubeColor]:
          possibleGameIDs.remove(gameID)

print(f'The Number of Possible Games are {possibleGameIDs} and the Sum of Their IDs is {sum(possibleGameIDs)}')

