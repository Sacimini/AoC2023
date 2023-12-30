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

camelCardGames = readInputFile('input.txt')
camelCardWinningHandDescriptions = ['ONE_PAIR', 'TWO_PAIR', 'THREE_OF_A_KIND', 'FULL_HOUSE', 'FOUR_OF_A_KIND', 'FIVE_OF_A_KIND']
camelCardWinningHands = {'HIGH_CARD' : 0}
camelCardGameResults = []
totalCamelCardWinnings = 0

for index, camelCardWinningHandDescription in enumerate(camelCardWinningHandDescriptions, start=1):
  camelCardWinningHands.update({camelCardWinningHandDescription : 2**(index-1)})
for index, camelCardGame in enumerate(camelCardGames, start = 1):
  gameParts = camelCardGame.split(' ')
  if len(gameParts) > 0:
    gameHand = gameParts[0]
    gameBid = int(gameParts[1])
  
    sortedGameHand = ''.join(sorted(gameHand))
#    print(f'Original Hand : {gameHand} Sorted : {sortedGameHand}')
    cardGameHistogram = dict((index, sortedGameHand.count(index)) for index in sortedGameHand)
    cardGameResult = 'HIGH_CARD'
    for cardCount in cardGameHistogram:
      if cardGameHistogram[cardCount] == 5:
        cardGameResult = 'FIVE_OF_A_KIND'
      elif cardGameHistogram[cardCount] == 4:
        cardGameResult = 'FOUR_OF_A_KIND'
      elif cardGameHistogram[cardCount] == 3:
        if cardGameResult == 'ONE_PAIR':
          cardGameResult = 'FULL_HOUSE'
        else:
          cardGameResult = 'THREE_OF_A_KIND'
      elif cardGameHistogram[cardCount] == 2:
        if cardGameResult == 'THREE_OF_A_KIND':
          cardGameResult = 'FULL_HOUSE'
        elif cardGameResult == 'ONE_PAIR':
          cardGameResult = 'TWO_PAIR'
        else:
          cardGameResult = 'ONE_PAIR'
        
    camelCardGameResults.append({'Game': index, 'Hand': gameHand, 'cardValue': gameHand.replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('J', 'B').replace('T', 'A'), 'Sorted': ''.join(sorted(gameHand)), 'Bid': gameBid, 'Result': cardGameResult, 'Rank': camelCardWinningHands[cardGameResult] })
#    print(f'Hand: {gameHand} Result: {cardGameResult} Total Winnings {totalCamelCardWinnings}')
camelCardGameResults = sorted(camelCardGameResults, key=lambda x:(x['Rank'], x['cardValue']), reverse=False)
for index, rankedGameResult in enumerate(camelCardGameResults, start = 1):
  totalCamelCardWinnings += rankedGameResult["Bid"] * index
  print(f'Hand {rankedGameResult["Hand"]} Sorted Hand {rankedGameResult["Sorted"]} Bid {rankedGameResult["Bid"]} Result {rankedGameResult["Result"]} Multipler {index} Total {rankedGameResult["Bid"]} * {index}  Result {rankedGameResult["Bid"] * index} Running_Total {totalCamelCardWinnings}')

print(f'The Total Winnings for {len(camelCardGames)} Camel Card Games is {totalCamelCardWinnings}')

        
    
