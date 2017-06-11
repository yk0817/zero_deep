array_test = [1,2,3,4,5,6,7,8]

for test in array_test:
    print(test)
    
for test in enumerate(array_test):
    print(test) #タプル型で戻る
    

for index,value in enumerate(array_test):
    print(index,value)