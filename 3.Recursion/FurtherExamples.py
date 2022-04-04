'''
Return the nth Fibonacci number
F0 = 0 F1 = 1
Fn = Fn-1 + Fn-2
'''

def Fibonacci(n):
    ''' return nth fibonacci number
        to reduce O(n), we invoke recursion only once during one call (Fn-1, Fn-2)
    '''
    if n <= 1:
        return (n,0)
    else:
        (a,b) = Fibonacci(n-1)
        return (a+b,a)

#print(Fibonacci(9)[0])
'''
sum the elements of a sequence recursively
'''
def linear_sum(data):
    if len(data) == 0 :
        return 0
    else:
        return data[len(data)-1]+linear_sum(data[0:len(data)-1])

# a = [4,3,6,2,8,9,3,2,8,5,1,7,2,8,3,7]
# print(linear_sum(a))
# b = [4,3,6,2,8]
# print(linear_sum(b))


'''
reverse a sequence with recursion
'''

def reverse_seq(sequence,start,stop):
    if len(sequence[start:stop]) != 1:
        print(start,stop)
        sequence[stop-1],sequence[start] = sequence[start],sequence[stop-1]
        reverse_seq(sequence,start+1,stop-1)
        return sequence

# a = [1,2,3,4,5]
# print(reverse_seq(a,start= 0,stop = len(a)))

'''
computing powers
x**n = x * x**(n-1)
'''

def compute_powers(x,n):
    if n == 0 :
        return 1
    else:
        x = x * compute_powers(x,n-1)
        return x

print(compute_powers(2,5))



