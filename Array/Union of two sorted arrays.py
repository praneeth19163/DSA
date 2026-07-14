class Solution:
    def unionArray(self, nums1, nums2):
        i = 0
        j = 0
        nums3 = []

        # TC: O(n + m)
        # SC: O(n + m) (output array)
        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                if len(nums3) == 0 or nums3[-1] != nums1[i]:
                    nums3.append(nums1[i])
                i += 1

            elif nums1[i] > nums2[j]:
                if len(nums3) == 0 or nums3[-1] != nums2[j]:
                    nums3.append(nums2[j])
                j += 1

            else:
                # Equal elements
                if len(nums3) == 0 or nums3[-1] != nums1[i]:
                    nums3.append(nums1[i])
                i += 1
                j += 1

        # Add remaining elements from nums1
        # TC: O(n)
        while i < len(nums1):
            if len(nums3) == 0 or nums3[-1] != nums1[i]:
                nums3.append(nums1[i])
            i += 1

        # Add remaining elements from nums2
        # TC: O(m)
        while j < len(nums2):
            if len(nums3) == 0 or nums3[-1] != nums2[j]:
                nums3.append(nums2[j])
            j += 1

        return nums3


def main():
    # Read first array
    # TC: O(n)
    n1 = int(input("Enter size of first array: "))
    nums1 = list(map(int, input("Enter first sorted array: ").split()))

    # Read second array
    # TC: O(m)
    n2 = int(input("Enter size of second array: "))
    nums2 = list(map(int, input("Enter second sorted array: ").split()))

    # Create object
    # TC: O(1)
    sol = Solution()

    # Function call
    # TC: O(n + m)
    # SC: O(n + m)
    result = sol.unionArray(nums1, nums2)

    print("Union:", result)


if __name__ == "__main__":
    main()