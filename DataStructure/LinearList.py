'''
class Stack
define the last element in list is the top element in Stack
'''

class Stack(): # object Stack
    def __init__(self):  # use list as the storage of items
        self.items = list()

    def push(self,item):  # add items in stack
        self.items.append(item)

    def isempty(self): # check whether it's an empty stack
        return self.items == []

    def pop(self): # delete items in stack
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

'''
新数据项的添加总发生在一端(rear)
而现存数据项的移除总发生在另一端(front)
'''
class Queue():
    def __init__(self):
        self.items = list()

    def enqueue(self,item):
        self.items.insert(0,item) # 只能在队尾进入

    def dequeue(self): # 元素只能在队首移除
        return self.items.pop()

    def isempty(self):
        return self.items == []

    def size(self):
        return len(self.items)


'''
Deque 双端队列
数据项可以从两端移除或加入
不存在先进先出或者后进后出
'''

class Deque():
    def __init__(self):
        self.items = list()

    def addFront(self,item): # add from front
        self.items.append(item)

    def addRear(self,item): # add from rear
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

'''
链表 Linked list
数据项之间没有位置规则，只是通过链接指向保持前后相对位置
链表的最基本元素叫做节点 每个节点要包含两个信息，数据项本身及其指向
'''
class Node():
    def __init__(self,data):  #初始化时不指向任何结点
        self.data = data
        self.next = None

    def setNewdata(self,newdata):
        self.data = newdata

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self,newnext):
        self.next = newnext #指向新结点

class UnorderedList():
    def __init__(self):
        self.head = None #一开始不指向任何结点  self.head 代表head指向的结点，而不是head结点本身，head是固定的

    def add(self,data): #由于是无序表，因此每次新加入的元素都可以加在开头 无序表的head始终指向第一个结点
        temp =Node(data) #创建结点
        temp.setNext(self.head) # 先指向原来的首结点
        self.head = temp # 再将head指向该结点

    def isEmpty(self):
        return self.head == None

    '''
    search size remove 均基于链表的遍历
    '''
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self,target): #只能返回有无该元素
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == target:
                return True
            else:
                current = current.getNext()
        return found

    def remove(self,target):
        current = self.head
        previous = None
        found = False
        '''
        找到元素后，需要将current前的结点指向此时current指向的结点，由于无法反向遍链表，因此设置一个previous来保存current的前项
        '''
        while not found:
            if current.getData() != target:
                previous = current
                current = current.getNext()
            else:
                found = True

        if previous == None: # If the target is the 1st node
            self.head = current.getNext()
        else:
            previous.setNext(current.next)

    def check(self): # print the whole unorderd list
        current = self.head
        print('head')
        final = False
        while not final:
            if current.getNext() != None:
                print(current.getData())
                current = current.getNext()
            else:
                print(current.getData())
                final = True

    def index(self,target): # 返回链表中某一值的位置索引
        current = self.head
        index = 0
        found = False
        while not found:
            if current.getData() == target:
                return index
            elif current.getNext() == None:
                return 'not found'
            else:
                current = current.getNext()
                index += 1
        return 'not found'

    def insert(self,target,pos):
        '''
        基本逻辑，找到指定位置索引(pos)的结点，其前一个结点(previous)指向新的node，node指向后一个结点(current)
        '''
        newdata = Node(target)
        current = self.head
        previous = None #储存前一个值
        count = 0
        while count < pos:
            previous = current
            current = current.getNext()
            count += 1
        if previous == None: #若插在0位
            self.head = newdata
        else:
            newdata.setNext(current)
            previous.setNext(newdata)


'''
Ordered List
Element are sorted by their property 
Realized by linked list
as long as we compare the data between 2 nodes
add(),search() are different from unorderedlist, the rest are the same
'''
class OrderedList():
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        '''
        search size remove 均基于链表的遍历
        '''
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count


    def add(self,data):
        '''
        need to find 2 nodes, one is smaller and the other is bigger
        '''
        newnode = Node(data)
        current = self.head
        previous = None
        stop = False
        '''
        find the insert position
        '''
        while not stop and current != None: #结点本身不是none，即如果有序表中有结点的话
            if current.getData() > data:
                stop = True
            else:
                previous = current
                current = current.getNext()
        '''
        start to insert
        '''
        if previous == None: # new data is the smallest
            newnode.setNext(current)
            self.head = newnode
        else:
            newnode.setNext(current)
            previous.setNext(newnode)

    def index(self,target): # 返回链表中某一值的位置索引
        current = self.head
        index = 0
        found = False
        while not found:
            if current.getData() == target:
                return index
            elif current.getNext() == None:
                return 'not found'
            else:
                current = current.getNext()
                index += 1
        return 'not found'

    def search(self,target):
        '''
        when the target doesn't exist in the ordered list
        no need to get all data , only need to find the one smaller and bigger than it
        '''
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == target:
                found = True
                return 'Found'
            else:
                if current.getData() > target:
                    stop = True
                else:
                    current = current.getNext()
        return 'not exist'

    def check(self):  # print the whole orderd list
        current = self.head
        print('head')
        final = False
        while not final:
            if current.getNext() != None:
                print(current.getData())
                current = current.getNext()
            else:
                print(current.getData())
                final = True
