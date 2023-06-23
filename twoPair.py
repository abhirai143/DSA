arr=[1,2,3,4,2,4,5,2]
def pairs(array,target):
   for i in range(len(array)):
       for j in range(i+1,len(array)):
           if array[i] == array[j]:
               continue
           elif array[i]+array[j] == target:
               print(f"{i} {j}")
pairs(arr,6)