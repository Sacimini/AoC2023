import os
import re
import itertools
from sys import maxsize
def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

def moveBrickDown(brick):
  brickID = brick[0]
  brickCubes = brick[1]
  brickMinimumZValue = brick[2]  

  return (brickID, [(x, y, z - 1) for x, y, z in brickCubes], brickMinimumZValue - 1)

def canBrickBeLowered(spaceOccupied, brick):
  brickCubes = brick[1]
  brickMinimumZValue = brick[2]  

  if brickMinimumZValue > 1 and not spaceOccupied & set((x, y, z - 1) for x, y, z in brickCubes):
    return True
  else:
    return False   

def evaluateBricks(bricks):
  newBricks = {}
  spaceOccupied = set()
  for brick in bricks:
    while canBrickBeLowered(spaceOccupied, brick):
      brick = moveBrickDown(brick)
    spaceOccupied |= set(x for x in brick[1])
    newBricks[brick[0]] = brick

  return newBricks

brickLayoutMap = readInputFile('input.txt').strip().split('\n')
bricks = []

for brickCounter, brickLayout in enumerate(brickLayoutMap):
  x1, y1, z1, x2, y2, z2 = map(int, re.findall(r'\d+', brickLayout))
  cubes = []
  minimumZValue = maxsize
  for dx in range(min(x1, x2), max(x1, x2) + 1):
    for dy in range(min(y1, y2), max(y1, y2) + 1):
      for dz in range(min(z1, z2), max(z1, z2) + 1):
        cubes.append((dx, dy, dz))
        minimumZValue = min(minimumZValue, dz)
  bricks.append([brickCounter, cubes, minimumZValue])

bricks = sorted(bricks, key=lambda brick: brick[2])

relaxed_bricks = evaluateBricks(bricks)

disintegratedBricks = 0
for index in itertools.combinations(relaxed_bricks.values(), len(relaxed_bricks) - 1):
  tempBricks = evaluateBricks(index)
  disintegratedBricks += all(brick[2] == relaxed_bricks[id][2] for id, brick in tempBricks.items())

print(f'The number of blocks which are safely disintegrated is {disintegratedBricks}')
