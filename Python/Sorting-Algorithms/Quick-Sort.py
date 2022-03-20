class QuickSort():
    def partition(self,array, low, high):

        # choose the rightmost element as pivot
        pivot = array[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if array[j] <= pivot:
                # if element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])

        # swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])

        # return the position from where partition is done
        return i + 1

    # function to perform quicksort
    def quickSort(self,array, low, high):
        # the minimum length of array is 2
        if low < high:
            # find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = self.partition(array, low, high)

            # recursive call on the left of pivot
            self.quickSort(array, low, pi - 1)

            # recursive call on the right of pivot
            self.quickSort(array, pi + 1, high)

# time complexity = O(n^2)
# space complexity = O(log(n))

# lst=[20,10]
# lst=[]
lst=[50,20,30,60,100,10,40]

print(lst)
m=QuickSort()
m.quickSort(lst,0,len(lst)-1)
print("==========SOLUTION===========")
print(lst)