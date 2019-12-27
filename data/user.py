class User(object):
    def __init__(self, id, name, create_time, update_time):
        self.id = id
        self.name = name
        self.create_time = create_time
        self.update_time = update_time

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_create_time(self):
        return self.create_time

    def get_update_time(self):
        return self.update_time

    def __str__(self):
        return 'User object (id: %s, name: %s)' % (self.id, self.name)

    __repr__ = __str__
