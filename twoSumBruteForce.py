class Solution:
    def twoSumBruteForce(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


def main() -> None:
    result = Solution().twoSum([4, 5, 3, 67, 13, 42, 15], 45)
    print(result)


if __name__ == "__main__":
    main()
