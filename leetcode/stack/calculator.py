import operator as op

from algorithm.Stack import Stack


def calc(express_list):
    opr_dict = {'+': 1, '-': 1, '*': 2, '/': 2}
    ops = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
    num_stack = Stack()
    opr_stack = Stack()
    for data in express_list:
        if data in opr_dict:
            while not opr_stack.isEmpty() and opr_dict[data] <= opr_dict[opr_stack.peek()]:
                num1 = num_stack.pop()
                num2 = num_stack.pop()
                operator = opr_stack.pop()
                num_stack.push(ops[operator](num2, num1))
            opr_stack.push(data)
        else:
            num_stack.push(data)
    num1 = num_stack.pop()
    num2 = num_stack.pop()
    operator = opr_stack.pop()
    num_stack.push(ops[operator](num2, num1))
    return num_stack.pop()


if __name__ == '__main__':
    exp_list = [3, '+', 5, '*', 8, '-', 6]
    print(exp_list)
    print(calc(exp_list))
