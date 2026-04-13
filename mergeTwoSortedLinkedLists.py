class ListNode:
    def __init__(self, value = 0, next = None):
        self.value = value
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
        out.append(node.value)
        node = node.next
    return out


class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        # Create those dummies. It is important to make heads and tail... he he he. of it all.
        head = ListNode(0)
        tail = head

        # If niether are empty find out which is a smaller vlaue to stay sorted.
        while list1 is not None and list2 is not None:
            if list1.value < list2.value:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Once you run out fill in the remaining numbers. Lists entered this function sorted.
        tail.next = list1 if list1 is not None else list2
        return head.next

def main() -> None:
    list1 = list_to_nodes([1, 4, 6, 7, 8])
    list2 = list_to_nodes([2, 3, 5, 9])
    solution = Solution().mergeTwoLists(list1, list2)
    print(nodes_to_list(solution))

if __name__ == "__main__":
    main()