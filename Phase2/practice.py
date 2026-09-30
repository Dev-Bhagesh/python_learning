# 1. create a countdown generator
# def CountDown(num,lim):
#     value = num
#     while(value != lim+1):
#         yield value
#         value += 1

# count = CountDown(1,5)
# for i in count:
#     print(i)
# ======================================================================
# 2. Even numbers generator
# def EvenNumbers(num , lim):
#     value = num 
#     while(value <= lim):
#         if value % 2 == 0:
#             yield value
#         value += 1

# even = EvenNumbers(1,10)
# for i in even:
#     print(i)
#=======================================================================

# 3. Movie ticket queue
# def Ticket():
#     ticket = ['super man','bat man','iron man','captain america']
#     for i in ticket:
#         yield i

# tick = Ticket()
# print(next(tick))        
# print(next(tick))        
# print(next(tick))        
# print(next(tick))        
# print(next(tick))        
# print(next(tick))        

# 4-5. Context Manager: Game Session
# class GameSession():
#     def __init__(self,name):
#         self.name = name

#     def __enter__(self):
#         print(f'Starting : {self.name}')

#     def __exit__(self,exc_type,exc,tb):
#         print(f'Ending : {self.name}')
#         if exc_type:
#             print(f'A error : {exc}')
#             return True

# game = 'Legend Of Zelda'
# with GameSession(game):
#     print(f'I am playing {game}')
#     value = 0/0

# 6. All combined 

class GameSession2():
    def __enter__(self):
        print('Starting the generator')

    def __exit__(self,exc_type,exc,tb):
        print('Ending the generator')

    def genNum(self,start,end):
        value = start
        while value <= end:
            yield value
            value += 100

    def gen(self):
        li = [100,250,450,700,900]
        for i in li:
            yield i

gene = GameSession2()

with GameSession2():
    for i in gene.gen():
        print(i)