import os
from collections import defaultdict, deque

def readInputFile(fileName):

  try:
    filePath = os.path.dirname(os.path.abspath(__file__))
    return open(filePath + '\\' + fileName).read()
  except:
    return []
    
wiringDiagram = readInputFile('input.txt').strip().split('\n')

schematic = defaultdict(list)
groupings = set()
for component in wiringDiagram:
  name, connections = component.split(':')
  for node in connections.split():
    schematic[name].append(node)
    schematic[node].append(name)
    groupings.add(tuple(sorted((name, node))))

groupSpans = defaultdict(int)
for node in schematic:
  visitedNodes = set([node])
  queue = deque([(node, [])])
  while queue:
    for index in range(0, len(queue)):
      currentNode, nodePath = queue.popleft()
      for boundary in nodePath:
         groupSpans[boundary] += 1
      for nextNode in schematic[currentNode]:
        if nextNode not in visitedNodes:
          visitedNodes.add(nextNode)
          queue.append((nextNode, nodePath + [tuple(sorted((nextNode, currentNode)))]))

mostCommonBoundaries = sorted(groupSpans, key=groupSpans.get)[-3:]
for nodeA, nodeB in mostCommonBoundaries:
  schematic[nodeA].remove(nodeB)
  schematic[nodeB].remove(nodeA)

visitedNodes = set([node])
queue = [node]
while queue:
  currentNode = queue.pop()
  for nextNode in schematic[currentNode]:  
    if nextNode not in visitedNodes:
      visitedNodes.add(nextNode)
      queue.append(nextNode)

  
print(f'The product of multiplying the size of the seperated groups is {len(visitedNodes) * (len(schematic) - len(visitedNodes))}')