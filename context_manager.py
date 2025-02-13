class FileWriter:
    def __init__(self, filename, mode='w'):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print("file is opening")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print("file closed")

with FileWriter('testfile.txt') as f:
    f.write('-----------------')
    f.write('Hello, World!\n')
