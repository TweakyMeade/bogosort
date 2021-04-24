def compairTest(a, b):
    if a < b:
        return True
    else:
        return False

testArray = [4,3,2,1,2]
run = 1
index = 0
lengthArray= len(testArray)
flag = True
while flag:
    index = 0
    for number in testArray:
        print(number)
        index += 1
        if index == lengthArray-2:
            print('break')
            flag = False
            break
    print('back to the start')

print('breakworked')
