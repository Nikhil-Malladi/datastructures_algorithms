# Bubble Sort
class BubbleSort():
    def bubble_sort(self,lst):
        check=False
        for n,i in enumerate(lst):
            if n==0:
                continue
            if lst[n-1]>lst[n]:
                lst[n-1],lst[n]=lst[n],lst[n-1]
                check=True
        print(lst)
        if not check:
            return lst
        self.bubble_sort(lst)

# time complexity = O(n^2)
# space complexity = O(1)

lst=[50,20,30,60,100,10,40]
print(lst)
b=BubbleSort()
bubble_sort_sol=b.bubble_sort(lst)
print("==========SOLUTION===========")
print(bubble_sort_sol)