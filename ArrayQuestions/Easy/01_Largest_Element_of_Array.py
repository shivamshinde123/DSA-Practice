class Solution:
    def largestElement(self, nums):

        # Approach 1: sort the array in ascending order and then get the last element

        # Approach 2
        largest = nums[0]
        for i in range(1, len(nums)):
            if arr[i] > largest:
                largest = arr[i]

        return largest
        
        # Approach 3: Using one of the step from bubble sort
        # n = len(nums)
        # for i in range(n-1):
        #     if nums[i] > nums[i+1]:
        #         nums[i], nums[i+1] = nums[i+1], nums[i]

        # return nums[-1]
    

# Example usage
if __name__ == "__main__":
    arr = [10, 20, 9, 17, 35, 2, 25]
    s = Solution()
    print(s.largestElement(arr))
