'''
Input 4 numbers
calculate whether they can get 24
if can print the calculation process
if can't print( not feasible)
'''


def input_fournumber(a,b,c,d): #a,b,c,d are 4 input number
    four_D =[a,b,c,d]
    return four_D
a=int(input('Input A'))
b=int(input('Input B'))
c=int(input('Input C'))
d=int(input('Input D'))
four_D=input_fournumber(a,b,c,d)
print(four_D)
# Randomly pick out 2 elements from fournum, create 3-D lists
all_3_D_results = list()
all_3_D_process = list()
symbol=['+','-','*','/','--','//'] # show the calculation process a--b = b-a ,a//b=b/a
symbol1 = ['+','-','*','--']
for i in range(0,4): # i is index of four_D
    if i != 3: # 2 is the biggest of i list[2]and list[3] is the last combination
        for j in range(i+1,4):
            left_element = four_D.copy()
            del left_element[j]
            del left_element[i]
            #print(left_element)
            #calculate results of 2 elements
            if four_D[i]==0 or four_D[j]==0:
                three_D_results = [four_D[i] + four_D[j], four_D[i] - four_D[j],
                                   four_D[i] * four_D[j], four_D[j] - four_D[i]]
                three_D_process = list()
                for sym in symbol1:
                    three_D_process.append('(' + str(four_D[i]) + sym + str(four_D[j]) + ')')
            else:
                three_D_results = [four_D[i]+four_D[j],four_D[i]-four_D[j],four_D[i]*four_D[j],
                               four_D[i]/four_D[j],four_D[j]-four_D[i],four_D[j]/four_D[i]]
                three_D_process = list()
                for sym in symbol:
                    three_D_process.append('('+str(four_D[i])+sym+str(four_D[j])+')')
            #print(three_D_process)
            # generate 3-D results + left  elements
            for k in range(0,len(three_D_results)):
                single_3D = left_element.copy()
                single_3D.insert(0,three_D_results[k])#results
                all_3_D_results.append(single_3D) #3_D results used to calculate
                process_3D = left_element.copy()
                process_3D.insert(0,three_D_process[k])
                all_3_D_process.append(process_3D)

#print(all_3_D_results)
#print(all_3_D_process)
#print(len(all_3_Dlist))
#repeat the step of 4D to 3D , make 3D list to 2D
all_2_D_results = list()
all_2_D_process = list()
for a in range(0,len(all_3_D_results)):
    threeDlist = all_3_D_results[a]
    #print(threeDlist)
    threeDprocess = all_3_D_process[a]
    for i in range(0, 3):
        if i != 2:
            for j in range(i + 1, 3):
                # remain_element = all_element-picked_element
                left_process = threeDprocess.copy()
                del left_process[j]
                del left_process[i]
                #print(left_element)
                left_element = threeDlist.copy()
                del left_element[j]
                del left_element[i]
                # calculate results of 2 elements
                if 0 in threeDlist:
                    two_D_results = [threeDlist[i] + threeDlist[j], threeDlist[i] - threeDlist[j],
                                     threeDlist[i] * threeDlist[j], threeDlist[j] - threeDlist[i]]
                    two_D_process = list()
                    for sym in symbol1:
                        two_D_process.append('(' + str(threeDprocess[i]) + sym + str(threeDprocess[j]) + ')')
                    #print(two_D_process)
                else:
                    two_D_results = [threeDlist[i] + threeDlist[j], threeDlist[i] - threeDlist[j],
                                     threeDlist[i] * threeDlist[j], threeDlist[i]/threeDlist[j],
                                     threeDlist[j] - threeDlist[i], threeDlist[j] / threeDlist[i]]
                    two_D_process = list()
                    for sym in symbol:
                        two_D_process.append('('+str(threeDprocess[i]) + sym + str(threeDprocess[j])+')')
                    #print(two_D_process)
                # print(three_D_process)
                # generate 3-D results + left  elements
                for k in range(0, len(two_D_results)):
                    single_2D = left_element.copy()
                    single_2D.insert(0, two_D_results[k])  # results
                    all_2_D_results.append(single_2D)  # 3_D results used to calculate
                    process_2D = left_process.copy()
                    process_2D.insert(0, two_D_process[k])
                    all_2_D_process.append(process_2D)
#print(len(all_2_D_process))
#print(all_2_D_results)
#print(all_2_D_process)
'''
repeat process again , 2D to 1D ,this time calculate the result, check which result equals to 24
'''
final_results=list()
final_process=list()

for i in range(0,len(all_2_D_process)):
    one_D_result = all_2_D_results[i]
    one_D_process = all_2_D_process[i]
    a = one_D_result[0]
    b = one_D_result[1]
    pa = one_D_process[0]
    pb = one_D_process[1]
    if 0 in one_D_result:
        final_results.append(a+b)
        final_process.append('('+str(pa)+'+'+str(pb)+')')
        final_results.append(a-b)
        final_process.append('(' + str(pa) + '-' + str(pb) + ')')
        final_results.append(a*b)
        final_process.append('(' + str(pa) + '*' + str(pb) + ')')
        final_results.append(b-a)
        final_process.append('(' + str(pb) + '-' + str(pa) + ')')
    else:
        final_results.append(a + b)
        final_process.append('(' + str(pa) + '+' + str(pb) + ')')
        final_results.append(a - b)
        final_process.append('(' + str(pa) + '-' + str(pb) + ')')
        final_results.append(a * b)
        final_process.append('(' + str(pa) + '*' + str(pb) + ')')
        final_results.append(b - a)
        final_process.append('(' + str(pb) + '-' + str(pa) + ')')
        final_results.append(a/b)
        final_process.append('(' + str(pa) + '/' + str(pb) + ')')
        final_results.append(b - a)
        final_process.append('(' + str(pb) + '/' + str(pa) + ')')
#print(len(final_process))

if 24 not in final_results:
    print('No answer!')
else:
    for a in range(0,len(final_process)):
        if final_results[a]==24:
            print(final_process[a]+'=24')
