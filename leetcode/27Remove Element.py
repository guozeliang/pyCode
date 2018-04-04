'''
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

'''

def removeElement(nums,val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    curlen = 0
    for i, tmpVal in enumerate(nums):
        if (tmpVal != val):
            nums[curlen] = tmpVal
            curlen += 1
    return curlen

# removeElement([3,2,2,3],3)

def removeElement2(nums,val):

    for tmpVal in  nums:
        print(tmpVal)
        # if tmpVal == val:
            # nums.remove(tmpVal)
    print(nums)
    return len(nums)

print(removeElement2([3,3],3))









