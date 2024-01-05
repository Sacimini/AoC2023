import os

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

directionMap = {'U': [-1, 0], 'D': [1,0], 'L': [0, -1], 'R': [0, 1]}
directionDecode = ['R', 'D', 'L', 'U']

trenchMap = readInputFile('input.txt').strip().split('\n')
diggingTrench = []
trenchSteps = []

for trenchRow in trenchMap:
  hexCode = trenchRow.split(' ')[-1]
  hexCode = hexCode.replace('(', '').replace(')', '').replace('#', '')
  direction = directionDecode[int(hexCode[-1])]
  steps = int(hexCode[-7:-1], 16)
  trenchSteps.append((direction, int(steps)))

x = 0
y = 0
trenchArea = 0
trenchPerimeter = 0
for trenchStep in trenchSteps:
  direction, steps = trenchStep
  dy, dx = directionMap[direction]
  dy, dx = dy * steps, dx * steps
  y, x = y + dy, x + dx
  trenchPerimeter += steps
  trenchArea += x * dy

print(f'The Total Area of the Trench is {trenchArea} with a Perimeter of {trenchPerimeter} and a Total Area of {trenchArea + int(trenchPerimeter / 2) + 1}')
