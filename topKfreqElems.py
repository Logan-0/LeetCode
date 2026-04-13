class Solution:

    def topKElements(self, nums: list[int], k: int) -> list[int]:

        # Initialize the count
        count = {}

        # For each number in the list
        for num in nums:

            # Update the dictionary, key is the number, value is the count
            count[num] = 1 + count.get(num, 0)

        # Init an array
        arr = []

        # For num, and cnt from the dictionary
        for num, cnt in count.items():

            arr.append([cnt, num])

        arr.sort()

        print(arr)

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

def main() -> None:
    solution = Solution().topKElements([1,2,4,2,4,5,5,4,2,2,3,5,6,2,4,3,4,5,2,4,5,3,5,4,6,7,8,9,6,6,4,3,5,6], 3)
    print(solution)

if __name__ == "__main__":
    main()
