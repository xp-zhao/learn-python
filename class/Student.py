class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


a = Student('a', 80)
a.age = 30
b = Student('b', 90)
print(a.age)
print(a.print_score(), b.print_score())
