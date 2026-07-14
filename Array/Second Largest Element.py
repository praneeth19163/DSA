class Solution:
    def secondLargestElement(self, nums):
        # Assume the first element is the largest
        largestElement = nums[0]
        secondLargestElement = float('-inf')

        for i in nums:
            # Update largest and second largest
            if largestElement < i:
                secondLargestElement = largestElement
                largestElement = i

            # Update second largest if current element is between
            # secondLargestElement and largestElement
            if i > secondLargestElement and i != largestElement:
                secondLargestElement = i

        # Return -1 if no second largest element exists
        return -1 if secondLargestElement == float('-inf') else secondLargestElement


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
    result = solution.secondLargestElement(nums)

    print("\nSecond Largest Element:", result)


if __name__ == "__main__":
    main()