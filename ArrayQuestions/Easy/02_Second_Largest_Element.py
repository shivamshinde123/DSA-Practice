
# find second largest element else, return -1.

class Solution:
    def secondLargestElement(self, nums):
        
        # Brute force: sort the array and then find the second largest element : O(NlogN + N)
        # sort the array
        # n = len(nums)
        # largest = nums[n-1]
        # second_largest = nums[n-2]
        # for i in range(n-2, -1, -1):
        #     if nums[i] < largest:
        #         second_largest = nums[i]
        #         break

        # better approach: update largest and second largest one after another: O(2N)
        # largest = nums[0]
        # for i in range(len(nums)):
        #     if nums[i] > largest:
        #         largest = nums[i]
                
        # second_largest = -10000
        # for i in range(len(nums)):
        #     if nums[i] > second_largest and nums[i] != largest:
        #         second_largest = nums[i]

        # if largest == second_largest:
        #     return -1
        
        # return second_largest

        # optimal approach: update largest, and second largest at the same time : O(N)
        largest = nums[0]
        second_largest = float('-inf')

        for i in range(len(nums)):
            if nums[i] > largest:
                second_largest = largest
                largest = nums[i]
            elif nums[i] > second_largest:
                second_largest = nums[i]

    
        if second_largest == float('-inf'):
            return -1
        
        return second_largest


    
# Example usage
if __name__ == "__main__":
    # arr = [10, 20, 9, 17, 35, 2, 25]
    arr1 = [10, 10, 10]
    s = Solution()
    print(s.secondLargestElement(arr1))