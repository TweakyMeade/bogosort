import random, time

import matplotlib.pyplot as plt


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
while True:
    '''i know this looks awful, i will fix it but i barely got some sleep last night'''
    plotFlag = input('Do you want a graph? (Y/N):').upper()
    if plotFlag == 'Y':
       plotFlag = True
       break
    if plotFlag == 'N':
       plotFlag = False
       break
    print('not valid selection!')


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
bestOrder = 0
startTime = time.time()
while True:
    index = 0
    for number in testArray:
        if compairTest(number,testArray[index+1])== False:
            if index > bestOrder:
                bestOrder = index
                print("Our best run at run " + str(run) + " with " + str(bestOrder) + " numbers in order in " + str(round(time.time()-startTime, 5), ) + " secondss")
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
if plotFlag == True:
    plt.title("Numbers in order against the Run", fontsize=20)
    plt.xlabel('Run Number', fontsize=10)
    plt.ylabel('Numbers in order', fontsize=10)
    plt.scatter(indexArray, runArray, s=50)

    plt.show()

