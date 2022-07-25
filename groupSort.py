#Given an array of numbers, this program prints out a list containing the numbers and their frequency. 
#This list should be sorted first by the frequency and then by the numbers.
#Example: arr=[5,67,5,3,3,2,2,2,6,3,5,5,5,1,3,8] should return
#[[5, 5], [3, 4], [2, 3], [1, 1], [6, 1], [8, 1], [67, 1]]

from collections import Counter
class Solution:
    def groupSort(self,arr):
        c=Counter(arr)
        list=[]
        for i in c:
            list.append([i,c[i]])
        i,j=0,1
        while i<len(list)-1:
            while j<len(list):
                if list[i][1]<list[j][1]:  
                    temp= list[i]
                    list[i]=list[j]
                    list[j]=temp
                if list[i][1]==list[j][1] and list[i][0]>list[j][0]:
                    temp= list[i]
                    list[i]=list[j]
                    list[j]=temp
                j+=1
            i+=1
            j=i+1
        return list
