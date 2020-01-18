class MinStack:

    def __init__(self):
        self.data_list = []
        self.min_index_list = []

    def push(self, x: int) -> None:
        self.data_list.append(x)
        if not self.min_index_list:
            self.min_index_list.append(0)
        else:
            min_data = self.getMin()
            if min_data > x:
                self.min_index_list.append(len(self.data_list) - 1)

    def pop(self) -> None:
        if not self.data_list:
            return None
        if len(self.data_list) - 1 == self.min_index_list[-1]:
            self.min_index_list.pop()
        self.data_list.pop()

    def top(self) -> int:
        if not self.data_list:
            return None
        return self.data_list[-1]

    def getMin(self) -> int:
        if not self.min_index_list:
            return None
        min_index = self.min_index_list[-1]
        return self.data_list[min_index]


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.top())
    print(min_stack.getMin())
