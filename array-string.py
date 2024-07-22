# day 2 of data structures and algorithms
nums = [1,2,3,4,5]
print (nums[0])
print (nums[-5])
print (nums[len(nums) - 1])
print(nums[::-1])

print ("----------------------------------------------")
def addtwo(arr, tar):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i]+arr[j]) == tar:
                return [arr[i], arr[j]]
    


arr = [1,2,3,4,5,6,7]
tar = 7
print(addtwo(arr, tar))
