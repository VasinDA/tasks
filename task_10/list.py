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
        index_list = [index for _ in self.tuple index += 1]
        return index_list 


myList = Mylist(1,2,3,4)
print(myList.find(2))