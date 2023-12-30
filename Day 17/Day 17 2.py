import heapq
import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

blockData = readInputFile('input.txt').strip().split('\n')
boardMap = {(rowIndex, columnIndex): int(column) for rowIndex, row in enumerate(blockData) for columnIndex, column in enumerate(row.strip())}

def leastAmountofHeatLoss(beginCoordinates, endCoordinates, minSteps, maxSteps):
  blockQueue = [(0, *beginCoordinates, 0, 0)]
  visitedBlocks = set()

  while blockQueue:
    heat, x, y, px, py = heapq.heappop(blockQueue)
    if x == '13':
      print(x,y)
    if (x,y) == endCoordinates: 
       return heat
    if (x ,y, px, py) in visitedBlocks: 
       continue
    visitedBlocks.add((x, y, px, py))
    for row, column in {(1,0),(0,1),(-1,0),(0,-1)}-{(px,py),(-px,-py)}:
      a, b, h = x, y, heat
      for index in range(1, maxSteps + 1):
        a = int(a + row)
        b = int(b + column)
        if (a,b) in boardMap:
          h += boardMap[a,b]
          if index >= minSteps:
            heapq.heappush(blockQueue, (h, a, b, row, column))  

print(f'The Least Amount of Heat Loss is {leastAmountofHeatLoss((0,0),max(boardMap), 4, 10)}')