class Solution:
    def isSorted(self, nums):
        # Check if the array is sorted in non-decreasing order
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True


def main():
    # Read number of elements
    n = int(input("Enter the number of elements: "))

    # Read array elements
    nums = list(map(int, input(f"Enter {n} elements separated by space: ").split()))

    # Validate input length
    if len(nums) != n:
        print("Error: Number of elements entered does not match n.")
        return

    solution = Solution()
    result = solution.isSorted(nums)

    if result:
        print("\nThe array is sorted.")
    else:
        print("\nThe array is not sorted.")


if __name__ == "__main__":
    main()