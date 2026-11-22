import os

class FileIterator:
    def __init__(self, filename):
        try:
            self.file = open(filename)
        except IOError as e:
            print(f"Error opening file: {e}")
            self.file = None

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.file is None:
            raise StopIteration
        line = self.file.readline()
        if line != '':
            return line
        else:
            self.file.close()
            raise StopIteration

def iterate_file(filename):
    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        return
    for line in FileIterator(filename):
        print(line)

if __name__ == "__main__":
    iterate_file('1_passagem_param.py')