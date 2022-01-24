'''
abcde x a = eeeeee
find all numbers  meeting conditions above
Since abcde is a five-digit number, eeeeee is a six-digit number,
a can't be 0, 1, e can't be 0
a,b,c,d,e are five different numbers
'''

import time
#method 1 list all numbers
start = time.time()

for abcde in range(10000,100000): # abcde is a five-digit number
   a = abcde//10000 #first digit
   e = abcde%10 # last  digit
   eeeeee = e + 10*e +100*e +1000*e +10000*e +100000*e
   if abcde * a == eeeeee and len(set(str(abcde))) ==5: # meeting 2 conditions
       print('abcde equals to {}'.format(abcde))

end = time.time()

print('Running time of method 1 : %s'%(end-start))

#method 2 mathematical method maybe save time
start = time.time()

for i in range(10000,99999): # a b c d e are 5 different numbers, ignore 99999 is reasonable
    for j in range(2,10): # j is a, can't be 0 1
        if i * j % 111111==0 and len(set(str(i))) == 5: # eeeeee must be a multiple of 111111
            if str(j) == str(i)[0]: # first digit should be the multiplier
                print('abcde equals to {}'.format(i))
end = time.time()
print('Running time of method 2 : %s'%(end-start))


# Turns out first method is faster