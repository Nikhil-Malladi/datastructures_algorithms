class ShellSort():
    def shellSort(lst, n):

        # Rearrange elements at each n/2, n/4, n/8, ... intervals
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                key = lst[i]
                j = i
                while j >= interval and lst[j - interval] > key:
                    lst[j] = lst[j - interval]
                    j -= interval

                lst[j] = key
            interval //= 2

# time complexity = O(n(log(n))^2)
# space complexity = O(1)

lst=[50,20,30,60,100,10,40]
print(lst)
m=ShellSort()
m.shell_sort(lst,len(lst))
print("==========SOLUTION===========")
print(lst)