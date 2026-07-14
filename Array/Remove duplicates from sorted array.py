class Solution:
    #2 pointer approach o(n)
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1
# we have another approach which needs to use sets like extra space and extra time o(nlogn)+o(n)


def main():
    # Read number of elements
    n = int(input("Enter the number of elements: "))

    # Read array elements
    nums = list(map(int, input(f"Enter {n} sorted elements separated by space: ").split()))

    # Validate input length
    if len(nums) != n:
        print("Error: Number of elements entered does not match n.")
        return

    solution = Solution()
    k = solution.removeDuplicates(nums)

    print("\nNumber of unique elements:", k)
    print("Array after removing duplicates:", nums[:k])


if __name__ == "__main__":
    main()