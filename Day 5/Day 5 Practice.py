import os
import re
from re import sub

def camelCase(string):
  string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
  return string[0].lower() + string[1:]

def getMapValue(map, key):
  value = key
  try:
    value = map[int(key)]
  finally:
    return int(value)

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    with open(filePath + '\\' + fileName, 'r') as file:
      fileData = file.readlines()
  except:
    fileData = [];
    
  return fileData

almanacData = readInputFile('input.txt')

seeds = {}
seedToSoilMap = {}
soilToFertilizerMap = {}
fertilizerToWaterMap = {}
waterToLightMap = {}
lightToTemperatureMap = {}
temperatureToHumidityMap = {}
humidityToLocationMap = {}

for lineData in almanacData:
  match = re.match('^:?([^:(0-9)\n]+)', lineData)
  if match != None:
    collection = camelCase(match[0])
    if not 'map' in match[0]:
      values = re.search('(?<=:\s).*', lineData)
      if values:
        for value in values[0].split(' '):
          globals()[f'{collection}'][value] = value
    print(f'Building {collection}')
  else:
    mapValues = lineData.replace('\n', '').split(' ')
    if len(mapValues) > 1:
      sourceValueStart = mapValues[0]
      sourceKeyStart = mapValues[1]
      rangeLength = int(mapValues[2])
      for rangeCount in range(0, rangeLength):
        globals()[f'{collection}'][int(sourceKeyStart) + rangeCount] = int(sourceValueStart) + rangeCount

closestLocation = 100
for seed in seeds:
  soil = getMapValue(seedToSoilMap, seed)
  fertilizer = getMapValue(soilToFertilizerMap, soil)
  water = getMapValue(fertilizerToWaterMap, fertilizer)
  light = getMapValue(waterToLightMap, water)
  temperature = getMapValue(lightToTemperatureMap, light)
  humidity = getMapValue(temperatureToHumidityMap, temperature)
  location = getMapValue(humidityToLocationMap, humidity)
  #print(f'Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}')
  closestLocation = min(closestLocation, location)

print(f'The Closest Seed Location is {closestLocation}')