class Solution:

    def mergeIntervals(self, intervals: list[list[int]]) -> list[list[int]]:

    # First sort your intervals to make the process just a little more simple with less loops
    # [5,7], [3,6], [8,11] -> [3,6], [5,7], [8,11]
        intervals.sort()

    # Create the result holders.
        mergedI = []

    # Being sorted we can gaurantee the first interval start. NintervalStart and IntervalEnd
        currentS, currentE = intervals[0]

    # For each interval loop through getting the start and end in the remaining intervals.
        for intervalS, intervalE in intervals[1:]:

        # If current intervalEnd is less than the next intervals start there is no overlap. Just add it. No merges
            if currentE < intervalS:

                mergedI.append([currentS, currentE])

            # Update the values to continue on
                currentS, currentE = intervalS, intervalE

            # Otherwise let's make our currentE the greater of currentE and intervalE
            # We do not care about the dropped values.
            else:
                currentE = max(currentE, intervalE)

        # Add it to the list now
        mergedI.append([currentS, currentE])

        return mergedI

def main() -> None:
    solution = Solution().mergeIntervals([[1,3], [2,5], [6,7], [9,14], [10,15]])
    print(solution)

if __name__ == "__main__":
    main()