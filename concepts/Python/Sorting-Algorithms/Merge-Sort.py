class MergeSort():
    def merge_sort(self,lst):
        
        if len(lst)>1:
            h=len(lst)//2
            L=lst[:h] # [] 2 1 1
            R=lst[h:] # 5 2 1 1
            # print(L,"L Pre")
            # print(R,"R Pre")
            
            self.merge_sort(L)
            # print(L,"L Post")
            self.merge_sort(R)
            # print(R,"R Post")
            # i=[1,2,3,4]
            # j=[100,200,300]
            i=j=k=0
            while(i<len(L)) and  (j<len(R)):
                if L[i]<R[j]:
                    lst[k]=L[i]
                    i+=1
                else:
                    lst[k]=R[j]
                    j+=1
                k+=1
            while i<len(L):
                lst[k]=L[i]
                i+=1
                k+=1
            while j<len(R):
                lst[k]=R[j]
                j+=1
                k+=1

# time complexity = O(n log(n))
# space complexity = O(n)

lst=[50,20,30,60,100,10,40]
print(lst)
m=MergeSort()
m.merge_sort(lst)
print("==========SOLUTION===========")
print(lst)