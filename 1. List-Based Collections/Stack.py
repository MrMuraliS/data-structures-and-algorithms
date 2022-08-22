class Element:
    count = 0

    def __init__(self, value):
        self.value = value
        self.next = None
        Element.count += 1


class Stack:

    def __init__(self, head=None):
        if head is None:
            self.head = None
        else:
            self.head = Element(head)

    def push(self, new_element):
        """Push (add) a new element onto the top of the stack"""
        if self.head is None:
            self.head = Element(new_element)
        else:
            node = Element(new_element)
            node.next = self.head
            self.head = node

    def pop(self):
        """Pop (remove) the first element off the top of the stack and return it"""
        if self.head is None:
            return None
        else:
            value = self.head
            if self.head:
                self.head = self.head.next
                value.next = None
            return value


# s1 = Stack()
# print(s1.pop().value)
# s1.push(1)
# print(s1.head.__dict__)
# s1.push(2)
# print(s1.head.__dict__)
# print(s1.head.next.__dict__)
# s1.push(3)
# print(s1.head.__dict__)
# print(s1.pop().value)
# print(s1.head.__dict__)
