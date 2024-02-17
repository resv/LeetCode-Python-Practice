################################# QUESTION ########################################################

283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1



################################# MY SOLUTION ########################################################

``` My Python Solution (Funny I saw that I did this in 2018 in Java, I included it below my python solution)

class Solution(object):
    def moveZeroes(self, nums):
        length = len(nums)
        index = 0

        while index < length:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
                length -= 1
            else:
                index += 1

 

################################# MY SOLUTION ########################################################
# my Java Solution in 2018

 class Solution {
    public void moveZeroes(int[] nums) {
        
         for(int i = 0; i < nums.length; i++){
            for(int k = i+1; k < nums.length; k++){
                if (nums[i] == 0 && nums[k] != 0){
                    int temp = nums[i];
                    nums[i] = nums[k];
                    nums[k] = temp;
                }
            }
        }
        System.out.println(Arrays.toString(nums));
        
    }
}