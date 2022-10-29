import random

#Stores all user inputted activities
def addActivities(activityList):
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

#Pairs the activites to 'fight' one another in a random draw until one activity remains
def findWinner(activityList):
    foundWinner = False
    losers = []
    while(foundWinner != True):
        index = 0
        startingIndex = 0

        if (len(activityList) == 1 or len(activityList) == 0):
            foundWinner = True
            continue
        if (len(activityList) % 2 != 0):
            startingIndex = 1
            index = 1 
            
        for activity in range(startingIndex, len(activityList), 2): 
            first = activityList[index]
            second = activityList[index + 1]
            roundWinner = random.randint(0, 1)

            if (roundWinner == 0):
                loserIndex = index + 1
                print(first + ' (winner) vs ' + second);
            else:
                loserIndex = index
                print(first + ' vs ' + second + ' (winner)');

            index += 2
            losers.append(activityList[loserIndex])

        for x in losers:
            activityList.remove(x)
        losers = []

    winner = ""
    winner = winner.join(activityList)

    print("Your chosen activity is " + winner)

def startProgram():
    programRunning = True
    activityList = [] 

    while (programRunning == True):
        print('Type "0" to manually input activities or type "1" to stop the program')
        userInput = input()
        if (userInput.lower() == 'finish' or userInput == '1'):
            programRunning = False
            continue
        if (userInput == '0'):
            addActivities(activityList)
            findWinner(activityList)
        elif (userInput != 0 or userInput != 1):
            print('The only allowed inputs are "0" or "1" for manual input')

startProgram()


