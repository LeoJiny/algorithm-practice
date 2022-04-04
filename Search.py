'''
Sequential Search
Traversal all elements in the list
if the target element exists, return the index of it
if not, return 'not exist'
If the list is unordered
O(n) the times (n) decides the complexity
If it's an ordered list
as long as the element is bigger than target
we can exit in advance
'''
def sequentialSearch(alist,target): # for unordered list
    pos = 0
    while pos < len(alist):
        if alist[pos] == target:
            return pos
        else:
            pos += 1
    return 'not exist'


testlist = [1,2,32,8,17,19,42,13,0]
#print(sequentialSearch(testlist,3))
#print(sequentialSearch(testlist,13))



def sequentialSearch_ordered(orderedlist,target):
    pos = 0
    stop = False
    while pos <len(orderedlist) and not stop:
        if orderedlist[pos]==target:
            return pos
        elif orderedlist[pos] > target:
            stop = True
        else:
            pos += 1
    return 'not exist'
# testlist = [0,1,2,8,13,17,19,32,42]
# print(sequentialSearch_ordered(testlist,3))
# print(sequentialSearch_ordered(testlist,13))




'''
Binary Search
Priority: The list is ordered
'''
def binarySearch(orderedlist,target):
    start = 0
    stop = len(orderedlist)-1
    found = False
    while start <= stop and  not found:
        mid = int((start + stop) / 2)
        if orderedlist[mid] < target:
            start = mid-1
        elif orderedlist[mid] < target:
            stop = mid +1
        else:
            found = True
            return  mid
    return 'not exist'

# testlist = [0,1,2,8,13,17,19,32,42]
# print(sequentialSearch_ordered(testlist,3))
# print(sequentialSearch_ordered(testlist,19))
