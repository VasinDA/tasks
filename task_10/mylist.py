from itertools import count


class Mylist:
    def __init__ (self, *data):
        self.list = [*data]

    def min(self):
        data = self.list[0]
        for i in self.list:
            if i < data:
                data = i
        return data
    
    def max(self):
        data = self.list[0]
        for i in self.list:
            if i > data:
                data = i
        return data 

    def avg(self):
        data = 0
        for i in self.list:
            data += i
        avg = data / self.lenList()
        return avg
    
    def find(self, value):
        index = 0
        for i in self.list:
            if i == value:
                return index
            index += 1
        index = -1
        return index
    
    def remove(self, index):
        list = [self.list[i] for i in range(self.lenList()) if i != index] 
        newList = Mylist(*list,)
        return newList

    def replace(self, old_value, new_value):
        hint_counter = self.hintCounter(old_value)
        if hint_counter == 0:
            return hint_counter
        for i in range(self.lenList()):
            if self.list[i] == old_value:
                self.list[i] = new_value
        return hint_counter
    
    def includes(self, value):
        hint_counter = self.hintCounter(value)
        if hint_counter == 0:
            return False
        return hint_counter

    def hintCounter(self, value):
        counter = 0
        for i in self.list:
            if i == value:
                counter += 1
        return counter

    def lenList(self):
        len = 0
        for _ in self.list:
            len += 1
        return len

    def __eq__(self, other):
        if isinstance(other, Mylist):
            return self.list == other.list
        return NotImplemented

