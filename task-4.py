"""
Односвязный стек
"""


class MyNode:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev


class MyStack:
    def __init__(self):
        self.head = None

    def push(self, value):
        if self.head is None:
            self.head = MyNode(value=value, prev=None)
        else:
            self.head = MyNode(value=value, prev=self.head)

    def pop(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.prev
            return value

    def print_me(self):
        if self.head is None:
            print("EMPTY")
        else:
            node = self.head
            while node is not None:
                print(node.value, end="")
                if node.prev is not None:
                    print(" -> ", end=" ")
                node = node.prev
            print("")

    def reverse(self):
        def reversed_head(node):
            new_node = MyNode(value=node.value)
            if node.prev is None:
                return new_node, new_node
            else:
                head, tail = reversed_head(node.prev)
                tail.prev = new_node
                return head, new_node

        if self.head is None:
            return MyStack()
        reversed_stack = MyStack()
        new_head, new_tail = reversed_head(self.head)
        reversed_stack.head = new_head
        return reversed_stack


def main():
    stack = MyStack()
    stack.print_me()
    print('Добавим 0')
    stack.push(0)
    stack.print_me()
    print('Добавим 1')
    stack.push(1)
    stack.print_me()
    print('Добавим 2')
    stack.push(2)
    stack.print_me()
    print('Добавим 3')
    stack.push(3)
    stack.print_me()
    print('Добавим 4')
    stack.push(4)
    stack.print_me()
    print('Добавим 5')
    stack.push(5)
    stack.print_me()
    print('Снимем со стека')
    print(stack.pop())
    stack.print_me()
    print('Снимем со стека')
    print(stack.pop())
    stack.print_me()
    print('Ревёрс!')
    stack = stack.reverse()
    stack.print_me()
    print('Снимем со стека')
    print(stack.pop())
    stack.print_me()
    print('Снимем со стека')
    print(stack.pop())
    stack.print_me()
    print('Ревёрс!')
    stack = stack.reverse()
    stack.print_me()
    print('Снимем со стека')
    print(stack.pop())
    stack.print_me()
    print('Снимем со стека')
    print(stack.pop())
    stack.print_me()


if __name__ == "__main__":
    main()
