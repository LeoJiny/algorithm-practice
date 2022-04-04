'''
Bubble Sort
Compare every close 2 elements, exchange their position if it's wrong
for a list contains n elements, every round would sort the biggest element
'''
def bubbleSort(alist):
    for n in range(len(alist)-1,0,-1): # the nth round
        for i in range(n): # the list has n-1 pairs of elements
            if alist[i] > alist[i+1]: # only when the latter is bigger than the former, exchange takes place
                alist[i+1],alist[i] = alist[i],alist[i+1]  #python allows exchanging at the same time
    return alist
'''
Selection Sort
Only exchange one element each round
'''
def selectionSort(alist):
    for n in range(len(alist)-1,0,-1): # take the subset
        maxposition = 0 # initialize
        for i in range(n):
            if alist[i] > alist[maxposition]: # select the biggest element during this round
                maxposition = i # record the position
            alist[i], alist[maxposition] = alist[maxposition],alist[i] # exchange
    return alist

'''
Insertion Sort
Divide the list into 2 parts: ordered and unordered
everytime, select one item from the unordered list, insert it into the ordered list
For a list containing n elements, after n-1 times, the sort would finish.
'''
def insertionSort(alist):
    for index in range(1,len(alist)): # index of elements to be selected
        currentvalue = alist[index] # selected element
        currentposition = index # the index of element to be compared from current position
        while currentposition > 0 and currentvalue < alist[currentposition-1]:
            '''
            If the compared element isn't the first element and the current value is bigger
            insert it before the selected compare element
            '''
            alist[currentposition],alist[currentposition-1] = alist[currentposition-1], currentvalue
            currentposition -= 1
    return alist



a = [54,26,93,17,77,31,44,55,20,20]
#print(bubbleSort(a))
#print(bubbleSort(a))
#print(selectionSort(a))
#print(insertionSort(a))

