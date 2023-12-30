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

def checkSurroundingsForSymbol(coordinates, engineMap):
  parsedCoordinates = coordinates.split(',')
  coordinateRow = int(parsedCoordinates[0])
  coordinateColumn = int(parsedCoordinates[1])

  for x,y in [(coordinateRow+i,coordinateColumn+j) for i in (-1,0,1) for j in (-1,0,1) if i != 0 or j != 0]:
    try:
      coordinate = str(x) + ',' + str(y)
      if engineMap[coordinate] == '*':
        #print(f'Sybmol {engineMap[coordinate]} found at {coordinate}')
        return coordinate 
    except:
      continue
  return None

def CalculateGearRatio(gearNumber, SymbolLocation):
  gearRatio = 0
  try:
    adjacentGearNumber = gearMap[symbolLocation]
    gearRatio = adjacentGearNumber * gearNumber
    print(f'Found Gear Ratio of {adjacentGearNumber} * {gearNumber} = {gearRatio}')
  except:
    gearMap[symbolLocation] = int(gearNumber)

  return gearRatio

engineSchematic = readInputFile('input.txt')
engineMap = {}
gearMap = {}
partNumbers = []
gearRatios = []

mapRow = 0
mapColumn = 0

for components in engineSchematic:
  mapRow += 1
  mapColumn = 0
  for character in components:
    mapColumn += 1
    mapCoordinates = str(mapRow) + ',' + str(mapColumn) 
    engineMap[mapCoordinates] = character

mapRow = 0
mapColumn = 0
partNumber = ''
partNumbers = []
foundSymbol = False

for coordinate in engineMap:
  character = engineMap[coordinate]
  if character.isnumeric():
    #print(f'number found at {coordinate}')
    if not foundSymbol:
      symbolLocation = checkSurroundingsForSymbol(coordinate, engineMap)
      foundSymbol = symbolLocation != None
    partNumber += character
  else:
    if len(partNumber) > 0 and foundSymbol:
      print(f'Adding Gear Number {partNumber} with a Symbol Location of {symbolLocation}')
      partNumbers.append(int(partNumber))
      gearRatios.append(CalculateGearRatio(int(partNumber), symbolLocation))
    partNumber = ''
    foundSymbol = False

print(f'The Number of Gears are {len(gearRatios)} and the Sum of Their Ratios are {sum(gearRatios)}')