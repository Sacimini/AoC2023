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
      if not engineMap[coordinate].isalnum() and engineMap[coordinate] != '.' and engineMap[coordinate] != '\n':
        #print(f'Sybmol {engineMap[coordinate]} found at {coordinate}')
        return True 
    except:
      continue
  return False


engineSchematic = readInputFile('input.txt')
engineMap = {}
partNumbers = []

mapRow = 0
mapColumn = 0

for components in engineSchematic:
  mapRow += 1
  mapColumn = 0
  #components = components.replace('\n', '')
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
      foundSymbol = checkSurroundingsForSymbol(coordinate, engineMap)
    partNumber += character
  else:
    if len(partNumber) > 0 and foundSymbol:
      print(f'Adding Part Number {partNumber}')
      partNumbers.append(int(partNumber))
    partNumber = ''
    foundSymbol = False

print(f'The Number of Part Numbers are {len(partNumbers)} and the Sum of Their Parts is {sum(partNumbers)}')