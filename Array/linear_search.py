class Solution:
    def linearSearch(self, nums, target):
        # Traverse the array
        # TC: O(n)
        # SC: O(1)
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1


def main():
    # Read array size
    # TC: O(1)
    n = int(input("Enter array size: "))

    # Read array elements
    # TC: O(n)
    nums = list(map(int, input("Enter array elements: ").split()))

    # Read target element
    # TC: O(1)
    target = int(input("Enter target element: "))

    # Create object
    # TC: O(1)
    sol = Solution()

    # Function call
    # TC: O(n)
    # SC: O(1)
    index = sol.linearSearch(nums, target)

    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()