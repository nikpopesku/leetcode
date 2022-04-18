def create_single_linked_list(arr):
    next = None
    for key, value in enumerate(reversed(arr)):
        next = ListNode(value, next)

    return next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


    def print(self):
        nodes = []
        nodes.append(str(self.val))
        node = self

        while node.next:
            node = node.next
            nodes.append(str(node.val))

        print(" -> ".join(nodes))