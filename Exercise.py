import LinearList
from LinearList import Stack
from LinearList import Queue
from LinearList import Deque
from LinearList import Node
from LinearList import UnorderedList
from LinearList import OrderedList
'''
Solve Hotpotato  Problem with QUEUE
所有小孩围成一圈，传num次，最后谁手里有土豆谁就死
使用队列，第一个拿土豆的放在队首，传一次土豆就拿出去一个人再放进队尾
传num次之后，队首的人就是手里有土豆的人
打印出来他的名字叫即可
'''

def Hotpotato(name,num):
    sequence = Queue()
    for names in name:
        sequence.enqueue(names)
    for i in range(0,num+1):
        a = sequence.dequeue()
        sequence.enqueue(a)
    deadman = sequence.dequeue()
    return deadman

'''
回文词判断
'''

def palchecker(string):
    s = Deque()
    for letters in string:
        s.addFront(letters)
    stillEqual = 1
    while s.size() >1 and stillEqual == 1:
        first = s.removeFront()
        last = s.removeRear()
        if first == last:
            stillEqual = 1
        else:
            return False
        # if first != last:
        #     stillEqual = False
    return True
# print(palchecker('lsdkjfskf'))
# print(palchecker('上海自来水来自海上'))

'''
Unordered list by linked list
'''
mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.check()
mylist.insert(55,1)
mylist.check()

'''
Ordered List by linked list
'''
mylist1 = OrderedList()
mylist1.add(31)
mylist1.add(77)
mylist1.add(17)
mylist1.add(93)
mylist1.add(26)
mylist1.add(54)
mylist1.check()