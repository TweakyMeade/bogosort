def compairTest(a, b):
    if a < b:
        return True
    else:
        return False
import random
sizeArray = input('how big of array to test?:')
testArray = []
for number in range(int(sizeArray)):
    testArray.append(int(number)+1)

print(testArray)
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
