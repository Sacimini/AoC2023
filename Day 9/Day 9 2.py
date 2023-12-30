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

def historicalValueInSeries(series):
  if len(set(series)) == 1:
     return series[0]
  subSeries = [series[index] - series[index-1] for index in range(1, len(series))]
  return series[0] - historicalValueInSeries(subSeries)

oasisReportData = readInputFile('input.txt')

extrapolatedValues = []

for oasisReportSequence in oasisReportData: 
  oasisSeries = list(map(int, oasisReportSequence.replace('\n', '').split(' ')))
  extrolpolatedValue = historicalValueInSeries(oasisSeries)
  extrapolatedValues.append(extrolpolatedValue)
  oasisSeries.insert(0, extrolpolatedValue)
  print(oasisSeries)

print(f'For the {len(oasisReportData)} oasis readings the total number of extrapolated values is {sum(extrapolatedValues)}')