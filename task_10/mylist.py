class Mylist:
    def __init__ (self, *data):
        self.list = [*data]
                
    def min(self):
        if self.lenList() == 0:
            return -1
        data = self.list[0]
        for i in self.list:
            if i < data:
                data = i
        return data
    
    def max(self):
        if self.lenList() == 0:
            return -1
        data = self.list[0]
        for i in self.list:
            if i > data:
                data = i
        return data 

    def avg(self):
        if self.lenList() == 0:
            return -1
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
        if self.lenList() == 0:
            return -1
        list = [self.list[i] for i in range(self.lenList()) if i != index] 
        newList = Mylist(*list,)
        return newList

    def replace(self, old_value, new_value):
        if self.lenList() == 0:
            return -1
        hint_counter = self.hintCounter(old_value)
        if hint_counter == 0:
            return hint_counter
        for i in range(self.lenList()):
            if self.list[i] == old_value:
                self.list[i] = new_value
        return hint_counter
    
    def includes(self, value):
        if self.lenList() == 0:
            return -1
        hint_counter = self.hintCounter(value)
        if hint_counter == 0:
            return False
        return hint_counter

    def sortDirection(self):
        if self.lenList == 1:
            return 1
        flag = True
        value = self.list[0]
        for i in range(1, self.lenList()):
            if value > self.list[i]:
                flag = False
                value = self.list[0]
                break
            value = self.list[i]
        if flag == True:
            return 1
        for i in range(1, self.lenList()):
            if value < self.list[i]:
                flag = True
                break
            value = self.list[i]
        if flag == False:
            return -1
        return 0

    def isSorted(self):
        if self.sortDirection() == 1 or self.sortDirection() == -1:
            return True
        return False
 
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