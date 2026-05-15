class Square:
    def __init__(self):
        self.current = 0

    def __getitem__(self, index):
        return index * index

    def __len__(self):
        return 10
    
s = Square()
print(s[13])
print(s[5])
print(s[567])
