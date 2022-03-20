# Selection Sort
cnt=0
class SelectionSort():
    def selection_sort(self,lst):
        min=0
        for n,i in enumerate(lst):
            if i<lst[min]:
                min=n
        lst[0],lst[min]=lst[min],lst[0]
        print(lst)
        if len(lst)==1:
            return lst
        return [lst[0]]+self.selection_sort(lst[1:])

    def selection_sort_2(self,array,size):
        for step in range(size):
            min_idx = step

            for i in range(step + 1, size):
            
                # to sort in descending order, change > to < in this line
                # select the minimum element in each loop
                if array[i] < array[min_idx]:
                    min_idx = i
            
            # put min at the correct position
            (array[step], array[min_idx]) = (array[min_idx], array[step])

# time complexity = O(n^2)
# space complexity = O(1)

lst=[50,20,30,60,100,10,40]
print(lst)
s=SelectionSort()
s.selection_sort_2(lst,len(lst))
print("==========SOLUTION===========")
print(lst)