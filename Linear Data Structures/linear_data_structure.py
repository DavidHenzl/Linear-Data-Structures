"""
Implementation of linear data structures:
Stack, Queue, Linked List
"""


class Node:
    """Creates node with value and pointer to the next element"""

    def __init__(self, val=None):
        self.value = val
        self.next_node = None


class Stack:
    """Linear data structure based on Last-In-First-Out principle"""

    def __init__(self):
        self.top = None

    def is_empty(self):
        """Checks if the stack is empty and returns boolean"""
        return self.top is None

    def push(self, elm):
        """Adds element on the top of the stack"""
        if self.is_empty():
            self.top = Node(elm)
        else:
            new_node = Node(elm)
            new_node.next_node = self.top
            self.top = new_node

    def pop(self):
        """Remove element from the top of the stack and returns the removed element"""
        if self.is_empty():
            return None
        output = self.top
        self.top = self.top.next_node
        return output.value

    def peek(self):
        """Returns top element"""
        if self.is_empty():
            return None
        return self.top.value

    def check_stack(self):
        """Prints all elements"""
        if self.is_empty():
            print("Empty stack")
        else:
            current = self.top
            while current:
                if current == self.top and not current.next_node:
                    print(current.value)
                elif current.next_node:
                    print(f"{current.value}->", end="")
                else:
                    print(current.value)
                current = current.next_node

    def size(self):
        """Returns count of all elements"""
        count = 0
        if self.top:
            current = self.top
            while current:
                count += 1
                current = current.next_node
        return count


class Queue:
    """Linear data structure based on First-In-First-Out principle"""

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def push(self, elm):
        """Append element to the end of the queue"""
        if self.is_empty():
            self.front = Node(elm)
            self.rear = self.front
        else:
            self.rear.next_node = Node(elm)
            self.rear = self.rear.next_node

    def pop(self):
        """Remove the first element in the queue and returns the value of the removed element"""
        if self.is_empty():
            return None
        output = self.front.value
        self.front = self.front.next_node
        return output

    def peek(self):
        """Returns the front element"""
        if self.is_empty():
            return None
        return self.front.value

    def check_queue(self):
        """Prints all elements"""
        if self.is_empty():
            print("Empty queue")
        else:
            current = self.front
            while current:
                if current == self.front and not current.next_node:
                    print(current.value)
                elif current.next_node:
                    print(f"{current.value}->", end="")
                else:
                    print(current.value)
                current = current.next_node

    def size(self):
        """Returns count of all elements"""
        count = 0
        if self.front:
            current = self.front
            while current:
                count += 1
                current = current.next_node
        return count


class LinkedList:
    """Linear data structure, with previous node pointing to the next"""

    def __init__(self, nodes=None):
        self.head_node = None
        self.tail_node = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head_node = node
            self.tail_node = node
            for elm in nodes:
                node.next_node = Node(elm)
                node = node.next_node
                if node.next_node is None:
                    self.tail_node = node

    def __iter__(self):
        """Makes the linked list iterable"""
        current = self.head_node
        while current is not None:
            yield current
            current = current.next_node

    def __getitem__(self, index):
        """Making the linked list subscriptable; linklist[index] returns value with the index"""
        if self.is_empty():
            raise Exception("Linked list is empty")
        if not isinstance(index, int):
            raise Exception(
                f'Inappropriate index type: {type(index)}')
        ind = 0
        current = self.head_node
        if index < 0:
            index = self.count() + index
        while current is not None:
            if index == ind:
                return current.value
            if current == self.tail_node:
                break
            current = current.next_node
            ind += 1
        raise Exception("List index out of range")

    def count(self):
        """Returns the count of all nodes in the linked list"""
        count = 0
        for _ in self:
            count += 1
        return count

    def is_empty(self):
        """Returns True(False) if the linked list is (not) empty"""
        return self.head_node is None

    def print_list(self):
        """Prints the linked list"""
        for node in self:
            if node not in (self.head_node, self.tail_node):
                print(f"{node.value}, ", end="")
            elif node == self.head_node:
                print(f"[{node.value}, ", end="")
            else:
                print(f" {node.value}]")

    def add_head(self, val):
        """Adds head before the actual head (first element)"""
        new_head = Node(val)
        if self.is_empty():
            self.tail_node = new_head
        new_head.next_node = self.head_node
        self.head_node = new_head

    def add_tail(self, val):
        """Adds tail linked to the actual tail (last element"""
        new_tail = Node(val)
        if self.is_empty():
            self.head_node = self.tail_node = new_tail
        else:
            self.tail_node.next_node = new_tail
            self.tail_node = new_tail

    def index_of(self, val):
        """Returns the index of first occurrence of value in the linked list"""
        index = 0
        current = self.head_node
        while current is not None:
            if current.value == val:
                return index
            else:
                index += 1
                current = current.next_node
        return -1

    def contains(self, val):
        """Returns True(False) if the linked list (doesn't) contains value"""
        return self.index_of(val) != -1

    def add_after(self, target_node_value, val):
        """Adds new node with val=value after specific node"""
        new_node = Node(val)
        for node in self:
            if node.value == target_node_value:
                new_node.next_node = node.next_node
                node.next_node = new_node
                if new_node.next_node is None:
                    self.tail_node = new_node
                return
        raise Exception(f"Node with value {target_node_value} not found")

    def add_before(self, target_node_value, val):
        """Adds new node with val=value before specific node"""
        if self.head_node.value == target_node_value:
            self.add_head(val)
            return
        new_node = Node(val)
        previous = self.head_node
        for node in self:
            if node.value == target_node_value:
                previous.next_node = new_node
                new_node.next_node = node
                return
            previous = node
        raise Exception(f"Node with value {target_node_value} not found")

    def print_head_tail(self):
        """Prints head and tail of the linked list"""
        if self.head_node is not None:
            print(f"head: {self.head_node.value}")
        if self.tail_node is not None:
            print(f"tail: {self.tail_node.value}")

    def remove_node(self, target_node_value):
        """Removes the first node with value = target_node_value"""
        if self.head_node.value == target_node_value:
            if self.head_node == self.tail_node:
                self.tail_node = None
            self.head_node = self.head_node.next_node
            return

        previous = self.head_node
        for node in self:
            if node.value == target_node_value:
                previous.next_node = node.next_node
                if previous.next_node is None:
                    self.tail_node = previous
                return
            previous = node
        raise Exception(f"Node with value {target_node_value} not found")

    def reverse(self):
        """Reverses the linked list"""
        current = self.head_node
        previous = None
        following = current.next_node
        while current:
            current.next_node = previous
            previous = current
            current = following
            if following:
                following = following.next_node
        self.head_node, self.tail_node = self.tail_node, self.head_node
