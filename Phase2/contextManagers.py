class GameSession():
    def __enter__(self):
        print('Starting the game...')

    def __exit__(self, exc_type, exc, tb):
        print('Exiting the game...')

        if exc_type:
            print(f'The error occured , error is :{exc} and {tb}')

with GameSession():
    print('Game is playing')