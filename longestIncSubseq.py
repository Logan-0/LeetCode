class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if len(set(nums)) == 1:
            return 1

        if len(nums) == 1:
            return 1

        # Make an array of 1 the length of the original list
        dp = [1] * len(nums)

        # loop from the 1 elemnt to the end
        for i in range(1, len(nums)):

            # loop again to i?
            for j in range(i):

                if nums[i] > nums[j]:
                    
                    dp[i] = max(dp[i], dp[j] + 1)

                    print("i",i)
                    print("j",j)

        return max(dp)

def main() -> None:
    solution = Solution().lengthOfLIS([1,4,2,6,3,13,20])
    print(solution)

if __name__ == "__main__":
    main()