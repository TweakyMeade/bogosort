def compairTest(a, b):
    if a < b:
        return True
    else:
        return False
import random

testArray = [1,2,3,4]
run = 1
index = 0
lengthArray= len(testArray)
forFlag = True
random.shuffle(testArray)
while True:
    index = 0
    for number in testArray:
        if compairTest(number,testArray[index+1])== False:
            random.shuffle(testArray)
            break
        index += 1
        if index == lengthArray-1:
            forFlag = False
            break
    if forFlag == False:
        break
    run+=1
print('it took '+str(run)+' runs to sort 1 to ' + str(lengthArray) + ' using Random shuffles of the numbers')
print('proof:' + str(testArray))
