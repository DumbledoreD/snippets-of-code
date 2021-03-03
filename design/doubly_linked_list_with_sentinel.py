# From implementing LFU Cache https://leetcode.com/problems/lfu-cache/
class ListNode:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.sentinel = ListNode(None)
        self.sentinel.next = self.sentinel.prev = self.sentinel

    def __bool__(self):
        return self.sentinel.next != self.sentinel

    def __str__(self):
        representation = []
        node = self.sentinel.next
        while node != self.sentinel:
            representation.append(str(node.value))
            node = node.next
        return ", ".join(representation)

    @property
    def tail(self):
        return self.sentinel.prev

    @property
    def head(self):
        return self.sentinel.next

    def append(self, node):
        # tail <===> node
        self.tail.next = node
        node.prev = self.tail

        # node <===> sentinel
        node.next = self.sentinel
        self.sentinel.prev = node

    def appendleft(self, node):
        # head <===> node
        self.head.prev = node
        node.next = self.head

        # node <===> sentinel
        node.prev = self.sentinel
        self.sentinel.next = node

    def pop(self, node):
        # node.prev <=== node ===> node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        return node


if __name__ == "__main__":
    dll = DoublyLinkedList()
    nodes = [ListNode(i) for i in range(5)]

    for node in nodes[1:4]:
        dll.append(node)

    print(dll)

    # New head
    dll.appendleft(nodes[0])
    print(dll)

    # New tail
    dll.append(nodes[-1])
    print(dll)

    # Pop head
    dll.pop(nodes[0])
    print(dll)

    # Pop tail
    dll.pop(nodes[-1])
    print(dll)

    # Pop middle
    dll.pop(nodes[2])
    print(dll)
