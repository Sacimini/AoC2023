import os
import re

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    with open(filePath + '\\' + fileName, 'r') as file:
      fileData = file.readlines()
  except:
    fileData = [];
    
  return fileData

boatRaces = readInputFile('input.txt')
winningRaces = []
Time = []
Distance = []

for boatRace in boatRaces:
  matches = re.findall('(\w+:*)', boatRace)
  for match in matches:
    if match.replace(':', '').isalpha():
      category = match.replace(':', '')
    elif match.isnumeric():
      globals()[f'{category}'].append(int(match))

raceNumber = 0
for raceDuration in Time:
  raceWins = 0
  for buttonPressDuration in range(1, raceDuration):
    boatSpeed = buttonPressDuration
    boatDistance = boatSpeed * (raceDuration - buttonPressDuration)
    #print(f'Boat Speed {boatSpeed}mm Traveling {boatDistance}mm')
    if boatDistance > Distance[raceNumber]:
      raceWins += 1
  print(f'Race #{raceNumber + 1} Results in {raceWins} Wins!')
  raceNumber += 1
  winningRaces.append(raceWins)

marginOfError = 1
for numOfWinners in winningRaces:
    marginOfError *= numOfWinners

print(f'The Margin of Error for the {len(winningRaces)} races is {marginOfError}')
  