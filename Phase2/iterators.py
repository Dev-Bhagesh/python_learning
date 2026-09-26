class CaughtUp():
    def __init__(self,num,end):
        self.num = num-1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num == self.end:
            raise StopIteration
        self.num += 1
        num = self.num
        return num

cought = CaughtUp(1,5)
print(next(cought))
print(next(cought))
print(next(cought))
print(next(cought))
print(next(cought))
print(next(cought))
print(next(cought))