answer = int(input('*You* This will be the answer. Select a number between 10 - 49: '))
factor = 99 - answer
player_num = int(input('*Player* Pick a number between 50 - 99: '))

def calculation_result (player_num, factor):
    calc1 = str(player_num + factor)
    calc2 = int(calc1[0]) + int(calc1[1:3])
    return player_num - int(calc2)


print(f'I said the answer was {answer} and the calculation result was {calculation_result(player_num, factor)}')
