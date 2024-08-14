'''day 2 of data structures and algorithms
nums = [1,2,3,4,5]
print (nums[0])
print (nums[-5])
print (nums[len(nums) - 1])
print(nums[::-1])

print ("------------------------------------------------------------------")
def addtwo(arr, tar):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i]+arr[j]) == tar:
                return [arr[i], arr[j]]        '''

            
def bestpract(arr):
    
    mapx = {}
    for i in range(len(arr)):
        mapx[arr[i]] = i
        for i in range(len(arr)):
            y = tar - arr[i]
            if y in mapx and mapx[y] != i:
                print("ting")
                return (mapx[y] , i)
            
            
    
    


arr = [2,3,4,5,6,7]
tar = 7
print(bestpract(arr))
