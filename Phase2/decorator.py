class Test():
    healt = 100

    @classmethod
    def increase_healt(cls,amt):
        cls.healt += amt

    @staticmethod
    def calculate_damage(defence,attack):
        print(defence - attack)

    def __init__(self):
        pass

    def battle_decorator(fun):
        def wrapper(self):
            print('⚔️  Preparing attack...')
            fun(self)
            print('⚔️  Attack finished!')
        return wrapper

    @battle_decorator
    def attack(self):
        print('💥 Attack is happening')

test = Test()
print(test.healt)
Test.increase_healt(50)
print(test.healt)
test.calculate_damage(100,30)