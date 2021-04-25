import random, time

def compairTest(a, b):
    if a < b:
        return True
    else:
        return False

while True:
    try:
        sizeArray = int(input('how big of array to test?:'))
        break
    except:
        print("integers only please")

testArray = []
runArray = []
indexArray = []
for number in range(int(sizeArray)):
    testArray.append(int(number)+1)

print(testArray)
run = 1
lengthArray= len(testArray)
forFlag = True
random.shuffle(testArray)
print("we start with:" + str(testArray))
startTime = time.time()
while True:
    index = 0
    for number in testArray:
        if compairTest(number,testArray[index+1])== False:
            random.shuffle(testArray)
            indexArray.append(run)
            runArray.append(index+1)
            break
        index += 1

        if index == lengthArray-1:
            endTime = time.time()
            forFlag = False
            break
    if forFlag == False:
        break

    run+=1
timeTotal= round(endTime - startTime, 5)
print('it took '+str(run)+' runs to sort 1 to ' + str(lengthArray) + ' using Random shuffles of the numbers, this took ' + str(timeTotal) + ' seconds')
print('proof:' + str(testArray))
#print(indexArray)
#print(runArray)