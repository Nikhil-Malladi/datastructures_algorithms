class InsertionSort():
    # def insertion_sort(self,lst):
    #     b=True
    #     for i in range(1,len(lst)):
    #         print(lst)
    #         if lst[i-1]>lst[i]:
    #             lst[i-1],lst[i]=lst[i],lst[i-1]
    #             b=False
    #     if not b:
    #         self.insertion_sort(lst)

    def insertion_sort_2(lst):
        for step in range(1, len(lst)):
            key = lst[step]
            j = step - 1

            # Compare key with each element on the left of it until an element smaller than it is found
            # For descending order, change key<array[j] to key>array[j].        
            while j >= 0 and key < lst[j]:
                lst[j + 1] = lst[j]
                j = j - 1
            
            # Place key at after the element just smaller than it.
            lst[j + 1] = key

# time complexity = O(n^2)
# space complexity = O(1)

lst=[50,20,30,60,100,10,40]
print(lst)
m=InsertionSort()
m.insertion_sort_2(lst)
print("==========SOLUTION===========")
print(lst)