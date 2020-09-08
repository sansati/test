'''
. Bubble sort
  . Number of passes = total length of list - 1
  . In outer loop, start with pass_num, and go till 0, decrease 1 every time
  . In inner loop, run from 0 till pass_num, increase 1 every time
  . In every run of inner loop, if the element that is in next index, is lesser than element in current index, then swap them
  . COmplexity of bubble sort program-O (n2)
  . Subsequent elements are compared (element at index 1 with element at index 2, element at index 2 with element at index 3 ...)
 '''
def bubblesort(nlist): # function name bubblesort
    for passnum in range(len(nlist)-1,0,-1): # for loop in reverse order from len-1 till 0
        for i in range(passnum):
            if nlist[i]>nlist[i+1]: # comparing
                temp=nlist[i] # swap using temp
                nlist[i]=nlist[i+1]
                nlist[i+1]=temp
#nlist=[14,46,43,27,57,41,45,21,70] 
nlist=[int(x) for x in input().split()] # list cpmrehension to define a space separeted list
bubblesort(nlist) # calling the function
print(nlist) # printing the sorted list
