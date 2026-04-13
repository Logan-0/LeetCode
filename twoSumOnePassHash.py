class Solution:

    # Also known as the sliding window approach to make a single pass
    def twoSumOnePassHash(self, nums: list[int], target: int) -> list[int]:
        
    # Create and empty dictionary
        numMap = {}

    # Iterate through the list
        for i, num in enumerate(nums):

    # Find what number is needed to meet the target based on the current value seen
            complement = target - num

    # If we already have the necessary number then lets return what we are looking at and the needed compliment
            if complement in numMap:
                return [numMap[complement], i]
                
    # If we didnt have the necessary number in the empty dicitonary add the currently seen number to the dicitonary so we can check for this later in case the number is useful
            numMap[num] = i
        return []


def main() -> None:
    result = Solution().twoSumOnePassHash([4, 5, 3, 67, 13, 42, 15], 45)
    print(result)


if __name__ == "__main__":
    main()
