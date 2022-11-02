class Mylist:
    def __init__ (self, *data):
        self.mylist = [*data]
                
    def min(self):
        if self.lenList() == 0:
            return None
        data = self.mylist[0]
        for i in self.mylist:
            if i < data:
                data = i
        return data
    
    def max(self):
        if self.lenList() == 0:
            return None
        data = self.mylist[0]
        for i in self.mylist:
            if i > data:
                data = i
        return data 

    def avg(self):
        if self.lenList() == 0:
            return None
        data = 0
        for i in self.mylist:
            data += i
        avg = data / self.lenList()
        return avg
    
    def find(self, value):
        # TODO: may we initiate `index` with -1 and then return after for loop nothing found/
        # TODO: what if list is empty?
        if self.lenList() == 0:
            return -1
        for i in range(self.lenList()):
            if self.mylist[i] == value:
                return i
            # TODO: may we use another for loop with I-index instead?
        return -1
    
    def remove(self, index):
        if self.lenList() == 0:
            return None
        remove_list = [self.mylist[i] for i in range(self.lenList()) if i != index] 
        newList = Mylist(*remove_list,)
        return newList

    def replace(self, old_value, new_value):
        if self.lenList() == 0:
            return -1
        hint_counter = self.hintCounter(old_value)
        if hint_counter == 0:
            return hint_counter
        for i in range(self.lenList()):
            if self.mylist[i] == old_value:
                self.mylist[i] = new_value
        return hint_counter
    
    def includes(self, value):
        # TODO: just 1 return instead of all lines?
        return self.hintCounter(value) > 0

    def sortDirection(self):
        if self.lenList() == 0:
            return None
        elif self.lenList() == 1:
            return 1
        flag = True
        value = self.mylist[0]
        for i in range(1, self.lenList()):
            if value > self.mylist[i]:
                flag = False
                value = self.mylist[0]
                break
            value = self.mylist[i]
        if flag == True:
            return 1
        for i in range(1, self.lenList()):
            if value < self.mylist[i]:
                flag = True
                break
            value = self.mylist[i]
        if flag == False:
            return -1
        return 0

    def isSorted(self):
       # TODO: may we have just 1 check instead?
        if self.sortDirection() == None:
            return None  
        return self.sortDirection() != 0
    
    def count(self, value=None):
        if value == None:
            return self.lenList()
        return self.hintCounter(value)

    def append(self, value):
        if isinstance(value, list):
            # TODO: what if that list is empty?
            self.mylist = self.mylist + value
            return self.mylist
        self.mylist = self.mylist + [value]
        return self.mylist
    
    # TODO: insert?
    def insert(self, index, value):
        if index < 0:
            return None # TODO: None?
        elif index >= self.lenList():
            return self.append(value)
        right_side_list = self.mylist[index:self.lenList()]
        self.mylist[index] = value
        self.mylist = self.mylist[:index+1]
        self.mylist = self.append(right_side_list)
        return self.mylist
    
    def concat(self, newList):
        new_list = newList.mylist
        self.mylist = self.append(new_list)
        return self.mylist
    
    def clear(self):
        self.mylist = []
        return self.mylist
    
    def sort(self, direction):
        if self.sortDirection() == None:
            # TODO: return... what?
            return None
        # TODO: check for direction == 0 1st?
        # TODO: then check for isSorted and possible revert
        # TODO: do sorting
        if self.sortDirection() == 0:
            swapped = True
            while swapped:
                swapped = False
                for i in range(self.lenList() - 1):
                    if self.mylist[i] > self.mylist[i + 1]:
                        self.mylist[i], self.mylist[i + 1] = self.mylist[i + 1], self.mylist[i]
                        swapped = True
            return self.sort(direction)
        if direction == self.sortDirection():
                return self.mylist
        if (direction == 1 and self.sortDirection() == -1) or (direction == -1 and self.sortDirection() == 1):
                self.mylist = self.mylist[::-1]
                return self.mylist
           
        return self.mylist

    def hintCounter(self, value):
        counter = 0
        for i in self.mylist:
            if i == value:
                counter += 1
        return counter

    def lenList(self):
        len = 0
        for _ in self.mylist:
            len += 1
        return len

    def __eq__(self, other):
        if isinstance(other, Mylist):
            return self.mylist == other.mylist
        return NotImplemented

list1 = Mylist()
print(list1.sort(-1))

