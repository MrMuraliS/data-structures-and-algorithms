class Element:
    count = 0

    def __init__(self, value):
        self.value = value
        self.next = None
        Element.count += 1


class LinkedList:
    def __init__(self, head=None):
        if head is None:
            self.head = head
        else:
            self.head = Element(head)

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = Element(new_element)
        else:
            self.head = Element(new_element)

    def get_position(self, position) -> int | None:
        """
        Get an element from a particular position.
        Assume the first position is 1.
        Return "None" if position is not in the list.
        :param position:
        :return:
        """
        current = self.head
        for _ in range(1, position):
            if current:
                current = current.next
            else:
                return None
        return current

    def insert(self, new_element, position):
        """
        Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.
        :param new_element:
        :param position:
        :return:
        """
        current = self.head
        count = 1
        if position == 1:
            self.head = Element(new_element)
            self.head.next = current
            return
        while current:
            count += 1
            if count == position:
                temp = current.next
                current.next = Element(new_element)
                current.next.next = temp
                return
            current = current.next

    def delete(self, value):
        if self.head.value == value:
            self.head = self.head.next
            return
        prev = self.head
        current = self.head.next
        while current:
            print(current.__dict__)
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next
        else:
            return


# l1 = LinkedList(5)
# print(l1.__dict__)
# print(l1.head.__dict__)
# l1.append(10)
# print(l1.head.__dict__)
# print(l1.head.next.__dict__)
# print()
# print("Getting Position")
# print(l1.get_position(5).value)
# print("Done")
# l1.insert(3, 1)
# print(l1)
#
# print()
# print(l1.__dict__)
# print(l1.head.__dict__)
# print(l1.head.next.__dict__)
# print(l1.head.next.next.__dict__)
# print()
#
# print("NEXT")
# l1.delete(13)
# print("After Delete")
# print(l1.__dict__)
# print(l1.head.__dict__)
# print(l1.head.next.__dict__)
# print(l1.head.next.next.__dict__)
#
# print(l1.get_position(1))
#
