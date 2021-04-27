import random, time

def shufflerFunc(a, b, c, d, e):
    if a > b:
        random.shuffle(e)
        d.append(c)
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
            print("Desired array:\n" + str(array))
            print("we start with:\n" + str(array))
            return array
        except:
            print("integers only please")

def graphIt(x,y):
    while True:
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

def indexBreaker(a,b,c):
    if a == b-1:
        c.append(b)
        return True

def bestOrderFunc(a,b,c,d):
    if a > b:
        print("Our best run at run " + str(d) + " with " + str(a) + " numbers in order in " + str(timeTaken(c, time.time())) + " seconds")
        return a
    return b


testArray = arraySizeCreator()

runArray = []
indexArray = []
bestOrder = 0
index = 0
run = 0
lengthArray= len(testArray)
startTime = time.time()
while index != lengthArray-1:
    run+=1
    runArray.append(run)
    for number in testArray:
        if shufflerFunc(number, testArray[index + 1], index, indexArray, testArray):
            index = 0
            break
        bestOrder=bestOrderFunc(index,bestOrder,startTime,run)
        index+=1
        if indexBreaker(index,lengthArray,indexArray): #right, i know this looks, the reason i'm breaking and also using fucntion for the while is because the for loop needs to complete before "while False" gets recognised form the interprater, Break exits the for loop to get back to the while.
            break

print('it took '+str(run)+' runs to sort 1 to ' + str(lengthArray) + ' using Random shuffles of the numbers, this took ' + str(timeTaken(startTime,time.time())) + ' seconds')
print('proof:\n' + str(testArray))
graphIt(indexArray, runArray)
