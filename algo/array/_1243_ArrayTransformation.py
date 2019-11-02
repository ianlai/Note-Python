class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        if arr is None or len(arr) == 0 :
            return []
        
        ans = [0] * len(arr)
        
        while True:
            ans[0] = arr[0]
            for i in range(1, len(arr)-1):
                if arr[i-1] > arr[i] < arr[i+1]:
                    ans[i] = arr[i] + 1
                elif arr[i-1] < arr[i] > arr[i+1]:
                    ans[i] = arr[i] - 1
                else:
                    ans[i] = arr[i]
            ans[-1] = arr[-1]
            #print("arr1:", arr)
            #print("arr2:", ans)
            if ans == arr:
                return ans
            # reset 
            arr = ans 
            ans = [0] * len(arr)