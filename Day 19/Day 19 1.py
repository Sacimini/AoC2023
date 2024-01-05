import os

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

def executeFlow(part):
  currentWorkflow = 'in'

  while True: 
    for workFlow in workflows[currentWorkflow]:
      if ':' in workFlow:
        condition, action = workFlow.split(':')
        if '>' in condition:
          partName, partNumber = condition.split('>')
          if part[partName] > int(partNumber):
             if action == 'A':
               return True
             elif action == 'R':
               return False
             currentWorkflow = action
             break
        if '<' in condition:
          partName, partNumber = condition.split('<')
          if part[partName] < int(partNumber):
             if action == 'A':
               return True
             elif action == 'R':
               return False
             currentWorkflow = action
             break
      if workFlow == 'A':
        return True
      elif workFlow == 'R':
        return False
    
      currentWorkflow = workFlow

acceptedRatings = 0
for partRating in partRatings:
  part = {}
  for parts in partRating[1:-1].split(","):
    key, value = parts.split("=")
    part[key] = int(value)
  if executeFlow(part):
   acceptedRatings += sum(part.values())
   #print(sum(part.values()))

print(f'The Sum of all Accepted Ratings is {acceptedRatings}')
