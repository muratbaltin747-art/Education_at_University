from typing import Any
user_1: str = input("Who will move first?\nplayer_1: ")
user_2: str = input("player_2: ")
attempts: int = 1 
with open("Lesson_01/Files/tic_tao_toy_Journal.csv", "r", encoding= "UTF8") as Journal:
    pass
def tic_tao_toy( user_1: str, user_2: str, attempts: int):
    array = [["", "", ""], ["", "", ""], ["", "", ""]]
    positions = [1,2,3,4,5,6,7,8,9]
    while attempts <= 5:
        if attempts != 5:
            sign_position_2: str|list = input("Enter (sign + spacebar + position): ") #because when attempt become 5, second user can't put into arra
            sign_position_2: str|list = sign_position_2.split()
        sign_position_1: str|list = input("Enter (sign + spacebar + position): ")
        sign_position_1: str|list = sign_position_1.split()
        try:
            if int(sign_position_1[1]) in positions:
                with open("Lesson_01/Files/tic_tao_toy_Journal.csv", "a", encoding= "UTF8") as Journal:
                    line = f"{sign_position_1[0]};{sign_position_1[1]}"
                    Journal.write(line)
            elif int(sign_position_2[1]) in positions:
                with open("Lesson_01/Files/tic_tao_toy_Journal.csv", "a", encoding= "UTF8") as Journal:
                    line = f"{sign_position_2[0]};{sign_position_2[1]}"
                    Journal.write(line)
            else:
                raise ValueError
        except ValueError:
            print(f"Error, please type sign and position correctly:/n{player_1}: {sign_position_1}/n{player_2}: {sign_position_2}")
            continue
        if attempts < 3:
            insert_signs(tuple(sign_position_1), tuple(sign_position_2), array, attempts)
            for row in array:
                print(row)
            attempts += 1
            continue
        else:
            sign_1, sign_2 = sign_position_1[1], sign_position_2[1]
            player_1,player_2 = (user_1, sign_1), (user_2, sign_2)
            winner: None|str = rules_of_game(array, player_1, player_2)
def insert_signs(sign_pos_1: tuple, sign_pos_2: tuple, array: list[Any], attempts) -> list[Any]:
    sign_1: str = sign_pos_1[0]
    pos_num_1: int  = int(sign_pos_1[1])
    count: int = 1
    Flag_stop: bool = None
    index_row, index_value = 0, 0
    for index_r, row in enumerate(array):
        if Flag_stop == True:
            break
        for index_c, value in enumerate(row):
            if pos_num_1 == count:
                if value == '':
                    index_row = index_r
                    index_value = index_c
                    Flag_stop = True
                else:
                    raise ValueError("Error, this field's already busy!")
                break
            else:
                count += 1
            continue
    if Flag_stop == True:
        array[index_row][index_value] = sign_1

    Flag_stop = None
    index_row, index_value = 0, 0
    count: int = 1

    sign_2: str = sign_pos_2[0]
    pos_num_2: int = int(sign_pos_2[1])
    for index_r, row in enumerate(array):
        if Flag_stop == True:
            break
        for index_c, value in enumerate(row):
            if pos_num_2 == count:
                if value == '':
                    index_row = index_r
                    index_value = index_c
                    Flag_stop = True
                break
            else:
                count += 1
                continue
    if Flag_stop == True:
        array[index_row][index_value] = sign_2
    return array
def rules_of_game(array: list[Any], player_1: tuple, player_2: tuple) -> None|str:
    pass
tic_tao_toy(user_1, user_2, attempts)