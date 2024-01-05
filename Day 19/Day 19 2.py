import os
from copy import deepcopy

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []

directionMap = {'U': [-1, 0], 'D': [1,0], 'L': [0, -1], 'R': [0, 1]}

partsList = readInputFile('input.txt').strip().split('\n\n')

workflows = {}
for parts in partsList[0].split('\n'):
  workflowName, workflowRules = parts.split("{")
  workflowRules = workflowRules[:-1].split(",")
  workflows[workflowName] = workflowRules

partRatings = partsList[1].split("\n")

def calculateRatingCombinations(rating):
    ratingCombinations = 1
    for values in rating.values():
        ratingCombinations *= values[1] - values[0] + 1
    return ratingCombinations

def executeFlow(rating, part):
  ratingCombinations = 0

  while True: 
    for workFlow in workflows[part]:
      if ':' in workFlow:
        condition, action = workFlow.split(':')
        if '>' in condition:
          partName, partNumber = condition.split('>')
          newRating = deepcopy(rating)
          if newRating[partName][1] > int(partNumber):
            newRating[partName][0] = max(newRating[partName][0], int(partNumber) + 1)
            if action == 'A':
              ratingCombinations += calculateRatingCombinations(newRating)
            elif action != 'R':
              ratingCombinations += executeFlow(newRating, action)
            rating[partName][1] = min(rating[partName][1], int(partNumber))
        if '<' in condition:
          partName, partNumber = condition.split('<')
          newRating = deepcopy(rating)
          if newRating[partName][0] < int(partNumber):
            newRating[partName][1] = min(newRating[partName][1], int(partNumber)-1)
            if action == "A":
                ratingCombinations += calculateRatingCombinations(newRating)
            elif action != "R":
                ratingCombinations += executeFlow(newRating, action)
            rating[partName][0] = max(rating[partName][0], int(partNumber))      
      else:        
        if workFlow == 'A':
          ratingCombinations += calculateRatingCombinations(rating)
        elif workFlow != 'R':
          ratingCombinations += executeFlow(rating, workFlow)
   
    return ratingCombinations

print(f'The Number of All Distinct Accepted Ratings Combinations is {executeFlow({"x":[1,4000], "m":[1,4000], "a":[1,4000], "s":[1,4000]}, "in")}')