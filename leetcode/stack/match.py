from algorithm.Stack import Stack


def match(express: str) -> bool:
    stack = Stack()
    str_dict = {'}': '{', ')': '(', ']': '['}
    for exp in express:
        if exp in str_dict:
            if stack.isEmpty() or stack.pop() != str_dict[exp]:
                return False
        else:
            stack.push(exp)
    return stack.isEmpty()

if __name__ == '__main__':
    assert match("({[]})")
    assert not match("(({{]]")
    assert not match("({]")
