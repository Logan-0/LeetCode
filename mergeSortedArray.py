class Solution:
    def mergeSortedArray(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:

        nums1lastValue = m-1
        nums2lastValue = n-1
        nums1lastIndex = m+n-1


    # While there are elements left to be merged continue merging.
        while nums2lastValue >= 0:

        # if the last value for nums1 is larger move it up. other wise move up the val from nums2
            if nums1lastValue >= 0 and nums1[nums1lastValue] > nums2[nums2lastValue]:
                nums1[nums1lastIndex] = nums1[nums1lastValue]
                nums1lastValue -= 1
            else:
                nums1[nums1lastIndex] = nums2[nums2lastValue]
                nums2lastValue -= 1

        # Update the index regardless as we now made a placement in nums1 for the final output
            nums1lastIndex -= 1

        return nums1


def main() -> None:
    solution = Solution().mergeSortedArray([1, 3, 4, 5, 0, 0, 0], 4, [2, 4, 7], 3)
    print(solution)

if __name__ == "__main__":
    main()