class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def travel(self):
        cur = self.head
        while cur:
            yield cur.item
            cur = cur.next

    def get(self, position):
        cur = self.head
        for _ in range(position):
            cur = cur.next
        return cur.item

    def remove(self, position):
        cur = self.head
        cur_position = 0
        cur_be_for = None
        while cur:
            if cur_position == position:
                if cur_be_for is None:
                    self.head = cur.next
                else:
                    cur_be_for.next = cur.next
            cur_be_for = cur
            cur = cur.next
            cur_position += 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', *(*my_list.travel(), ))
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', *(*my_list.travel(), ))
