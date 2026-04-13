class Solution:
    def combinationsOfAPhoneNumber(self, digits: str) -> list[str]:

    # Get a mapping for the keypad
        keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs" ,"tuv", "wxyz"]
        
    # Setup a place for the answer to be returned
        ans = [""]

    # for each number in the list given
        for i in digits:

        # s is keypad string for the corresponding number from the string
            s = keypad[int(i)]

        # for every letter in "a" add on every letter in "b" and get a combo to add to our answer.
        # e.g. 23 -> "abc", "def" ====== ad, ae, af, db, be, bf, cd, ce, cf
            ans = [a + b for a in ans for b in s]

        return ans

def main() -> None:
    solution = Solution().combinationsOfAPhoneNumber("2475")
    print(solution)

if __name__ == "__main__":
    main()