class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_nodes(values: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def nodes_to_list(node: ListNode | None) -> list[int]:
    out: list[int] = []
    while node is not None:
        out.append(node.val)
        node = node.next
    return out


class Solution:


    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        
        # Create a dummy list for memory and readability purposes
        dummy = ListNode(0)
        
        # Our current node will be the dummy node to start
        current = dummy

        # This will be our variable holding any numbers that when added spill over to double digits. e.g. if 11, carry is 1.
        carry = 0

        # While list 1 or list 2 is not None (or finished)
        while l1 is not None or l2 is not None:

            # if we have a digit in the first list get it or set to 0
            x = l1.val if l1 is not None else 0

            # if we have a digit in the second list get it or set to 0
            y = l2.val if l2 is not None else 0

            # sum the numbers and include any previously carried digit
            sum = carry + x + y

            # take that number and get any found carry by modulo division
            carry = sum // 10

            # set our current node's next to the next node for each list
            current.next = l1 if l1 is not None else l2
            current.next.val = sum % 10

            # update our current node
            current = current.next

            # shift down to the next node for each list
            if l1 is not None: l1 = l1.next
            if l2 is not None: l2 = l2.next

        # if carry is greater than 0 our next node should be the carry to assist in including overflowing numbers.
        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next



def main() -> None:
    l1 = list_to_nodes([6, 4, 7, 2, 8, 1])
    l2 = list_to_nodes([2, 6, 4, 8, 9, 1, 1, 1, 1, 1, 1])
    solution = Solution().addTwoNumbers(l1, l2)
    print(nodes_to_list(solution))


if __name__ == "__main__":
    main()

        
