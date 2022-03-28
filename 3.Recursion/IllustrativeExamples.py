'''
Application 1
factorial problem
n!=n*(n-1)!
'''

def factorial(n):
    if n == 0:
        return 1
    elif n >=1:
        return n *factorial(n-1)  # here we apply the function itself  recursion

#print(factorial(5))

'''
Application 2
Draw English Ruler
'''



def draw_line(tick_length,tick_label=''): # tick_length = 3 then print '---'
    '''tick label shoud be str. AT EACH INCH there would be a sign  eg ----0,---1 '''
    line = '-'*tick_length
    if tick_label:
        line +=' '+tick_label
    print(line)


def draw_interval(center_length):
    '''draw tick interval based upon a central tick length'''
    if center_length>0:
        draw_interval(center_length-1) # recursion
        draw_line(center_length)
        draw_interval(center_length-1)

def draw_ruler(num_inches,major_length):
    '''num of inches decide how many time the draw interval function would repeat'''
    draw_line(major_length,'0')
    for i in range(1,1+num_inches):
        draw_interval(major_length)
        draw_line(major_length,str(i))

'''
Application 3
Binary Search
'''
def Binary_search(sorted_sequence,target_number,low,high):
    '''
    :param sorted_sequence: for binary search , the data must be sorted
    :param low,high: each search, compare low,high to the target number and upgrade one of the 2 parameters
    If the target equals data[mid], then we have found the item we are looking for,and the search terminates successfully.
    • If target < data[mid], then we recur on the first half of the sequence, that is,
                 on the interval of indices from low to mid − 1.
    • If target > data[mid], then we recur on the second half of the sequence, that is,
                 on the interval of indices from mid + 1 to high.
    '''
    if low > high:
        return False
    else:
        mid = (low+high)//2
        if sorted_sequence[mid] == target_number:
            return mid
        elif sorted_sequence[mid] < target_number:
            low = mid +1
            '''
            low = mid works as well, here low = mid + 1 just makes the code quicker
            '''
            return Binary_search(sorted_sequence,target_number,low,high)
        else:
            high = mid -1
            return  Binary_search(sorted_sequence,target_number,low,high)

#Test
# data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
# a = Binary_search(data,19,0,len(data)-1)
# print(data[a]==19)


'''
Application 4
computing the total disk usage for all
files and directories nested within a particular directory.
In this application, we would use Python's os module
os.path.getsize(path) returns the immediate disk usage for the file or directory
os.path.isdir(path) return True if entry designated by string path is a directory
os.listdir(path) return names oaf all entries within a directory
os.path.join(path,filename) compose the path string and filename string using '/' for Unix/Linux
'''
import os
def Disk_Usage(path):
    '''return the number of bytes used by a file/folder and any descendents'''
    total = os.path.getsize(path)
    if os.path.isdir(path) == True:
        for filename in os.listdir(path):
            childpath = os.path.join(path,filename)
            total += Disk_Usage(childpath)
    return total

#print(Disk_Usage('/Users/leojin/Desktop/CODE')*10e-7)
