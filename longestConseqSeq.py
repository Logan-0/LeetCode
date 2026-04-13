class Solution:

    def longestConsecSeq(self, nums: list[int]) -> list[int]:

        # Init Count
        count = 1
        highestCount = 1

        # Remove duplicates
        nums = list(set(nums))

        # Sort
        nums.sort()

        print(nums)

        for i in range(0, len(nums)-1, 1):

            print(nums[i])

            if nums[i+1] - nums[i] == 1:

                count +=1

                if count > highestCount:
                    highestCount = count
            
            else:

                count = 1

        return highestCount

def main() -> None:
    solution = Solution().longestConsecSeq([100,4,200,1,3,2])
    print(solution)

if __name__ == "__main__":
    main()

