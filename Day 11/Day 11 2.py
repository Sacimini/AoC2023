import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

solarSystem = readInputFile('input.txt')
galaxyMap =[]

emptyRows = []
emptyColumns = []

for rowIndex, rowData in enumerate(solarSystem.strip().split()):
  for columnIndex, columnData in enumerate(rowData):
    if columnData == '#':
      galaxyMap.append((columnIndex, rowIndex))


maximumColumn = max(galaxyMap, key=lambda coordinates: coordinates[0])[0]
maximumRow = max(galaxyMap, key=lambda coordinates: coordinates[1])[1]

for row in range(maximumRow + 1):
  if not any([row == galaxy[1] for galaxy in galaxyMap]):
     emptyRows.append(row) 

for column in range(maximumColumn + 1):
  if not any([column == galaxy[0] for galaxy in galaxyMap]):
     emptyColumns.append(column) 

universeMultipler = 1000000
expandedUniverse = [(galaxy[0] +(len([x for x in emptyColumns if x < galaxy[0]]) * (universeMultipler - 1)), galaxy[1] + len([y for y in emptyRows if y < galaxy[1]]) * (universeMultipler - 1)) for galaxy in galaxyMap]

shortestDistanceBetweenGalaxies = {}
for i in expandedUniverse:
    for j in expandedUniverse:
        if i != j and (j, i) not in shortestDistanceBetweenGalaxies:
            shortestDistanceBetweenGalaxies[(i, j)] = abs(i[0] - j[0]) + abs(i[1] - j[1])
            
print('Shortest Distance Between Galaxies is ',sum(shortestDistanceBetweenGalaxies.values()))
