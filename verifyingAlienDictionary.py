class Solution:

    def verifyDicitonary(self, words: list[str], order: str) -> bool:
    
    # First we need a mapping from the order of the given alien dicitonary
        alienDicMapping = {char: position for position, char in enumerate(order)}

    # Some of the longest words commonly used in writing of any kind is 7 letters.
        for positionCheck in range(7):
            
        # Let's check based on a smaller than any valid value
            previousVal = -1

        # Find a way to do another item
            allDifferent = True

            for aWord in words:

            # Treat currentValue as -1 if we are past the words length.
            # Else check in the mapping for the index
                if positionCheck >= len(aWord):

                    currentVal = -1
                
                else:

                    currentVal = alienDicMapping[aWord[positionCheck]]

                if previousVal > currentVal:
                    return False

                if previousVal == currentVal:

                    allDifferent = False

                previousVal = currentVal

            if allDifferent:
                return True

        return True

def main() -> None:
    solution = Solution().verifyDicitonary(["app", "apple", "application", "appeal", "appear", "apprehend"], "hlabcdefgijkmnopqrstuvwxyz")
    print(solution)

if __name__ == "__main__":
    main()

