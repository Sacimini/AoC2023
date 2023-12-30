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

scratchCards = readInputFile('input.txt')
cardValue = 0
ticketsWonMap = []
ticketValueMap = {}

for scratchCardGame in scratchCards:
  parsedScratchCardGame = scratchCardGame.split(': ')
  if len(parsedScratchCardGame) > 0:
    cardID = int(parsedScratchCardGame[0].replace('Card', '').replace(' ', ''))
    gameNumbers = parsedScratchCardGame[1].split(' | ')

    cardValue = 0
    if len(gameNumbers) > 0:
      cardNumbers = gameNumbers[0].replace('  ', ' ').split(' ')
      winningNumbers = gameNumbers[1].replace('  ', ' ').replace('\n', '').split(' ')
    for cardNumber in cardNumbers:
      if cardNumber in winningNumbers and cardNumber != '':
        #print(f'{cardNumber} present in card numbers {cardNumbers} and winning numbers {winningNumbers}')
        cardValue += 1
      else:
        #print(f'{cardNumber} not present card numbers {cardNumbers} and winning numbers {winningNumbers}')
        continue
    #print(f'Card #{cardID} contains {cardValue} winners worth {cardValue} free tickets')     
    if cardValue > 0:
      for newTicket in range(cardID + 1, cardID + cardValue + 1):
        ticketsWonMap.append(newTicket)
    ticketValueMap[cardID] = cardValue

for newTicket in ticketsWonMap:
  for freeTicket in range(newTicket + 1, newTicket + ticketValueMap[newTicket] + 1):
    ticketsWonMap.append(freeTicket)

print(f'Total Number of Tickets Bought are {len(scratchCards)} and Won are {len(ticketsWonMap)} For a Total of {len(ticketsWonMap)+ len(scratchCards)}')



