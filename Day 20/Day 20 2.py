import os
import math
def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []
  
moduleConfigurations = readInputFile('input.txt').strip().split('\n')

moduleDestinations = {}
for moduleConfiguration in moduleConfigurations:
  source, target = moduleConfiguration.split(' -> ')
  moduleDestinations[source] = target.split(', ')

pulseResults = []

for module in moduleDestinations['broadcaster']:
    moduleName = module
    binaryValue = ''

    while moduleName:
      flipFlopModule = moduleDestinations['%' + moduleName]
      if len(flipFlopModule) == 2 or '%' + flipFlopModule[0] not in moduleDestinations:
         binaryValue = '1' + binaryValue
      else: 
         binaryValue = '0' + binaryValue
      nextModule = [value for value in moduleDestinations['%' + moduleName] if '%' + value in moduleDestinations]

      if len(nextModule) == 0:
        break      
      moduleName = nextModule[0]
    pulseResults += [int(binaryValue, 2)]

print(math.lcm(*pulseResults))