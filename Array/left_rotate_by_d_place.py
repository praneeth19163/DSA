# #brute force
# n = int(input("Enter the number of elements: "))
# nums = list(map(int, input(f"Enter {n} sorted elements separated by space: ").split()))
# d=int(input("enter the number of places to shift: "))
# d=d%(len(nums))
# temp=[]
# for i in range(0,d):
#     temp.append(nums[i])
#     #tc for these is o(d) because we are doing d shifts
# #shift the remaining elements in nums to their repective position
# for i in range(d,len(nums)):
#     nums[i-d]=nums[i]
#     #tc for these is o(n-d)
# for i in range(0,d):
#     nums[d+i+1]=temp[i]
#     #tc for these is o(d)
# print(nums)
# #totak tc is o(d)+o(n-d)+o(d)=o(n+d)
# #sc is o(d)


#optimal approach-reversing the array
class Solution:
    def rotateArray(self, nums, k: int) -> None:
        # TC: O(1)
        # SC: O(1)
        k = k % len(nums)

        # Reverse first k elements
        # TC: O(k)
        self.reverse(nums, 0, k - 1)

        # Reverse remaining (n-k) elements
        # TC: O(n-k)
        self.reverse(nums, k, len(nums) - 1)

        # Reverse entire array
        # TC: O(n)
        self.reverse(nums, 0, len(nums) - 1)

        # Overall Time Complexity:
        # O(k) + O(n-k) + O(n)
        # = O(2n)
        # = O(n)

        # Overall Space Complexity:
        # O(1)

    def reverse(self, nums, left, right) -> None:
        # Reverses elements from left to right using two pointers

        # TC: O(right - left + 1)
        # Worst Case: O(n)
        # SC: O(1)

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


def main():
    # TC: O(1)
    n = int(input("Enter array size: "))

    # Reading n elements
    # TC: O(n)
    nums = list(map(int, input("Enter array elements: ").split()))

    # TC: O(1)
    k = int(input("Enter k: "))

    print("\nOriginal Array:", nums)

    # Creating object
    # TC: O(1)
    sol = Solution()

    # Function call
    # TC: O(n)
    # SC: O(1)
    sol.rotateArray(nums, k)

    print("Array after Left Rotation:", nums)


if __name__ == "__main__":
    main()
