import os
from collections import deque

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

moduleConfigurations = readInputFile('input.txt').strip().split('\n')

configurations = {}
conjuctionModules = []
flipFlopModules = []
moduleStates = {}
moduleSources = {}
moduleDestinations = {}

pulseCounter = [0, 0]
for moduleConfiguration in moduleConfigurations:
  source, targets = moduleConfiguration.split(' -> ')
  type = '' if source[0].isalnum() else source[0]
  source = source if source[0].isalnum() else source[1:]

  moduleDestinations[source] = targets.split(', ')
  moduleStates[source] = 0

  if type == '%':
    flipFlopModules.append(source) 
  elif type == '&':
    conjuctionModules.append(source) 

  for target in moduleDestinations[source]:
    if target not in moduleSources.keys():
      moduleSources[target] = []
    moduleSources[target].append(source if source[0].isalnum() else source[1:])      

for counter in range(1000):
  pulseCounter[0] += 1
  queue = deque([(moduleName, 0) for moduleName in moduleDestinations['broadcaster']])
  while queue:
    moduleName, moduleState = queue.pop()
    pulseCounter[moduleState] += 1
    if moduleName in flipFlopModules:
      if moduleState:
        continue
      moduleStates[moduleName] ^= 1
    elif moduleName in conjuctionModules:
      moduleStates[moduleName] = not all(moduleStates[y] for y in moduleSources[moduleName])
    for x in moduleDestinations.get(moduleName, []):
      queue.appendleft((x, moduleStates[moduleName]))

print(f'The total number of low pulses({pulseCounter[1]}) multiplied by the total number of high pulses({pulseCounter[0]}) is {pulseCounter[0] * pulseCounter[1]}')
