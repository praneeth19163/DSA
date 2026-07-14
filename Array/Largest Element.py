class Solution:
    def largestElement(self, nums):
        # Assume the first element is the largest
        largestElement = nums[0]

        # Traverse the array to find the largest element
        for i in nums:
            if largestElement < i:
                largestElement = i

        return largestElement


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
    result = solution.largestElement(nums)

    print("\nLargest Element:", result)


if __name__ == "__main__":
    main()