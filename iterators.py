# problem 1
class MyRange():
  def __init__(self, start=0, stop=4, step=1):
    self.start = start
    self.stop = stop
    self.step = step

  def __iter__(self):
    self.current = self.start
    return self

  def __next__(self):
    if self.current >= self.stop:
      raise StopIteration
    x = self.current
    self.current += self.step
    return x

myclass = MyRange(0,6,1)
for num in myclass:
  print(num)

# problem 2 

class ReadFile:
    def __init__(self, filename):
        self.filename = filename
    
    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self
    
    def __next__(self):
        line = self.file.readline()
        if not line: 
            self.file.close()
            raise StopIteration
        return line.strip() 

file_reader = ReadFile('testfile.txt')

for line in file_reader:
    print(line)

# problem 3 

class FlattList:
    def __init__(self, list):
        self.list = list
        self.list_index = 0
        self.list_item_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.list_index >= len(self.list):
            raise StopIteration
        
        current_list = self.list[self.list_index]
        
        if self.list_item_index >= len(current_list):
            self.list_index += 1
            self.list_item_index = 0
            return self.__next__()
        
        element = current_list[self.list_item_index]
        self.list_item_index += 1
        return element

input = [[1,2],[5],[3,6,5]]
myclass = FlattList(input)
list = []
for num in myclass:
    list.append(num)

print(list)
