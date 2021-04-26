import random, time

def compairTest(a, b):
    if a > b:
        return True
    else:
        return False

def arraySizeCreator():
    while True:
        try:
            array = []
            sizeArray = int(input('how big of array to test?:'))
            for number in range(int(sizeArray)):
                array.append(int(number)+1)
            return array
        except:
            print("integers only please")

def graphIt(x,y):
    while True:
        '''i know this looks awful, i will fix it but i barely got some sleep last night'''
        flag = input('Do you want a graph? (Y/N):')
        if flag.upper() == 'Y':
            import matplotlib.pyplot as plt
            plt.title("Numbers in order against the Run", fontsize=20)
            plt.xlabel('Run Number', fontsize=10)
            plt.ylabel('Numbers in order', fontsize=10)
            plt.scatter(x,y, s=50)
            plt.show()
            return

        if flag.upper() == 'N':
            return
        print('not valid selection!')

def timeTaken(a,b):
    return round(b - a, 5)

def indexBreaker(a,b):
    return a == b-1

def bestOrderFunc(a,b,c,d):
    if a > b:
        print("Our best run at run " + str(d) + " with " + str(a) + " numbers in order in " + str(
            timeTaken(c, time.time())) + " secondss")
        return a
    return b

runArray = []

testArray = arraySizeCreator()

indexArray = []
print("Desired array:\n"+str(testArray))
run = 0
lengthArray= len(testArray)
forFlag = True
random.shuffle(testArray)
print("we start with:\n"  +str(testArray))
bestOrder = 0
startTime = time.time()
index = 0
while indexBreaker(index,lengthArray) == False:
    run+=1
    for number in testArray:
        if compairTest(number,testArray[index+1])== False:
            bestOrder=bestOrderFunc(index,bestOrder,startTime,run)
            random.shuffle(testArray)
            indexArray.append(run)
            runArray.append(index + 1)
            index = 0
            break
        index += 1
        if indexBreaker(index,lengthArray):
            break

print('it took '+str(run)+' runs to sort 1 to ' + str(lengthArray) + ' using Random shuffles of the numbers, this took ' + str(timeTaken(startTime,time.time())) + ' seconds')
print('proof:' + str(testArray))
graphIt(indexArray, runArray)
