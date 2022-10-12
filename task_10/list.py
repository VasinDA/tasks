from operator import index


class Mylist:
    def __init__ (self, *data):
        self.tuple = data

    def min(self):
        data = self.tuple[0]
        for i in self.tuple:
            if i < data:
                data = i
        return data
    
    def max(self):
        data = self.tuple[0]
        for i in self.tuple:
            if i > data:
                data = i
        return data 

    def avg(self):
        counter = 0
        data = 0
        for i in self.tuple:
            counter += 1
            data += i
        avg = data / counter
        return avg
    
    def find(self, data):
        index = 0
        for i in self.tuple:
            if i == data:
                return index
            index += 1
        index = -1
        return index
    
    def remove(self, data):
        len = 0
        for _ in self.tuple:
            len += 1
        list = [self.tuple[i] for i in range(len) if i != data]
        newList = Mylist(*list,)
        return newList

