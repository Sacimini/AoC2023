import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

def findMyReflection(mirrorMap):
  for mapColumn in range(1, len(mirrorMap[0])):
    nextColumn = min(mapColumn, len(mirrorMap[0])-mapColumn)
    isReflection = True
    for mapRow in mirrorMap:
       if mapRow[mapColumn-nextColumn:mapColumn] != mapRow[mapColumn:mapColumn+nextColumn][::-1] :
         isReflection = False
         break
    if isReflection:
       return mapColumn

mirrors = readInputFile('input.txt')

patterns = []
rowData = []

mirrorMaps = [[list(row) for row in mirror] for mirror in [mirror.split('\n') for mirror in mirrors.strip().split('\n\n')]]

mapColumns = 0
mapRows = 0

for mirrorMap in mirrorMaps:
  rowReflection = findMyReflection(mirrorMap)
  columnReflection = findMyReflection(list(zip(*mirrorMap)))
  if rowReflection:
    mapColumns += rowReflection
  else:
    mapColumns += 0

  if columnReflection:
    mapRows += columnReflection * 100     
  else:
    mapRows += 0

print('Number of Reflections is', mapColumns+mapRows)   