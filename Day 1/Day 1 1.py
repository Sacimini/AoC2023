import os

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
  CalibrationValues = [];
  for character in calibrationEntry:
    if character.isnumeric():
      CalibrationValues.append(character)

  if len(CalibrationValues) > 0:
    print(int(CalibrationValues[0] + CalibrationValues[len(CalibrationValues)-1]))
    totalCalibrationValue += int(CalibrationValues[0] + CalibrationValues[len(CalibrationValues)-1])


print(f'Processed {len(calibrationDocument)} Calibration Documents with a Total Calibration Value of {totalCalibrationValue}')   