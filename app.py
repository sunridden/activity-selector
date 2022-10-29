import random

#Stores all user inputted activities
def addActivities():
    activityList = []
    loadedActivities = False
    print('Enter all activities below. Enter "stop" when finished.')

    while(loadedActivities != True):
        newActivity = input()
        if (newActivity.lower() == 'stop'):
            loadedActivities = True
            continue
        if (newActivity != '' and newActivity not in activityList):
            activityList.append(newActivity)
        print('Please enter the next activity or "stop" to finish.')
    
    findWinner(activityList)

#Pairs the activites to 'fight' one another in a random draw until one activity remains
def findWinner(activityList):
    foundWinner = False
    losers = []
    while(foundWinner != True):
        startIndex = 0

        if (len(activityList) == 1 or len(activityList) == 0):
            foundWinner = True
            continue
        if (len(activityList) % 2 != 0):
            startIndex = 1 
            
        for activityIndex in range(startIndex, len(activityList), 2): 
            first = activityList[activityIndex]
            second = activityList[activityIndex + 1]
            roundWinner = random.randint(0, 1)

            if (roundWinner == 0):
                loserIndex = startIndex + 1
                print(first + ' (winner) vs ' + second);
            else:
                loserIndex = startIndex
                print(first + ' vs ' + second + ' (winner)');

            startIndex += 2
            losers.append(activityList[loserIndex])

        for loser in losers:
            activityList.remove(loser)
        losers = []

    winner = ""
    winner = winner.join(activityList)
    print("Your chosen activity is " + winner)
    activityList.remove(winner)

def startProgram():
    programRunning = True

    while (programRunning == True):
        print('Type "0" to manually input activities or type "1" to stop the program')
        userInput = input()
        if (userInput.lower() == 'stop' or userInput == '1'):
            programRunning = False
            continue
        if (userInput == '0'):
            addActivities()
        elif (userInput != 0 or userInput != 1):
            print('The only allowed inputs are "0" or "1" for manual input')

startProgram()


