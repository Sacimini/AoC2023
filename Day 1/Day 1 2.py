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

totalCalibrationValue = 0;

calibrationDocument = readInputFile('input.txt')

for calibrationEntry in calibrationDocument:
  CalibrationValues = []

  searchWords = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
  wordsToNumbers = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
  pattern = r'(?:' + '|'.join(map(re.escape, searchWords)) + r')'
  matchesExist = True
  while matchesExist:
    match = re.search(pattern, calibrationEntry)
    if match != None:
      #calibrationEntry = calibrationEntry.replace(match[0], str(wordsToNumbers[match[0]]))   
      calibrationEntry = calibrationEntry[:match.start()] + str(wordsToNumbers[match[0]]) + calibrationEntry[match.start()+1:]
    else:
      matchesExist = False
  #print(calibrationEntry.replace('\n', ''))
  for character in calibrationEntry: 
    if character.isnumeric():
      CalibrationValues.append(character)   
  if len(CalibrationValues) > 0:
    #print(f'{calibrationEntry} Total {int(CalibrationValues[0] + CalibrationValues[len(CalibrationValues)-1])}')
    #print(int(CalibrationValues[0] + CalibrationValues[len(CalibrationValues)-1]))
    totalCalibrationValue += int(CalibrationValues[0] + CalibrationValues[len(CalibrationValues)-1])


print(f'Processed {len(calibrationDocument)} Calibration Documents with a Total Calibration Value of {totalCalibrationValue}')   