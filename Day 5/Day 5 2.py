import os
import re
import sys
from re import sub

def camelCase(string):
  string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
  return string[0].lower() + string[1:]

def getMapValue(name, map, value):
  key = value
  for values in map:
    mapValues = values.replace('\n', '').split(' ')
    if len(mapValues) > 1:
      sourceValueStart = int(mapValues[0])
      sourceKeyStart = int(mapValues[1])
      rangeLength = int(mapValues[2])
      #print(f'Looking for {key} in {name} Between {sourceValueStart} and {sourceValueStart + rangeLength}')
      if int(key) >= sourceValueStart and int(key) <= (sourceValueStart + rangeLength):
        #print(f'Calculating Key = {sourceKeyStart} + ({key - sourceValueStart})')
        key = sourceKeyStart + (key - sourceValueStart)
        break

  
  #print(f'Returning {key}')
  return int(key)

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    with open(filePath + '\\' + fileName, 'r') as file:
      fileData = file.readlines()
  except:
    fileData = [];
    
  return fileData

almanacData = readInputFile('input.txt')

seeds = []
seedToSoilMap = []
soilToFertilizerMap = []
fertilizerToWaterMap = []
waterToLightMap = []
lightToTemperatureMap = []
temperatureToHumidityMap = []
humidityToLocationMap = []

for lineData in almanacData:
  match = re.match('^:?([^:(0-9)\n]+)', lineData)
  if match != None:
    collection = camelCase(match[0])
    if not 'map' in match[0]:
      values = re.search('(?<=seeds:\s).*', lineData)
      if values:
        parsedValues = values[0].split(' ')
        for index in range(0, len(parsedValues)-1, 2):
          seeds.append({'rangeStart' : int(parsedValues[index]), 'rangeEnd': int(parsedValues[index]) + int(parsedValues[index+1])})
  else:
    mapValues = lineData.replace('\n', '').split(' ')
    if len(mapValues) > 1:
      globals()[f'{collection}'].append(lineData)

closestLocation = sys.maxsize

for location in range(0, closestLocation):
  humidity = getMapValue('humidityToLocationMap', humidityToLocationMap, location)  
  temperature = getMapValue('temperatureToHumidityMap', temperatureToHumidityMap, humidity)
  light = getMapValue('lightToTemperatureMap', lightToTemperatureMap, temperature)
  water = getMapValue('waterToLightMap', waterToLightMap, light)
  fertilizer = getMapValue('fertilizerToWaterMap', fertilizerToWaterMap, water)
  soil = getMapValue('soilToFertilizerMap', soilToFertilizerMap, fertilizer)
  seed = getMapValue('seedToSoilMap', seedToSoilMap, soil)
  #print(f'Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}')
  for seedValue in seeds:
    if seed >= seedValue['rangeStart'] and seed <= seedValue['rangeEnd']:
      closestLocation = min(closestLocation, location)
      print(f'The Closest Seed Location is {closestLocation}')
      exit()