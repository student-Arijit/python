def bubble_sort(nums):
    for i in range(n := len(nums)):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break

arr = [4, 7, 8, 3, 9, 2]
bubble_sort(arr)
print(arr)
