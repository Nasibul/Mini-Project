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