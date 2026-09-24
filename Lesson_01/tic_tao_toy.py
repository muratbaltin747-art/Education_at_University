from typing import Any
player_1: str = input("Who will move first?\nplayer_1: ")
player_2: str = input("player_2: ")
attempts: int = 1 
def tic_tao_toy( player_1: str, player_2: str, attempts: int):
    arrange = [["", "", ""], ["", "", ""], ["", "", ""]]
    while attempts <= 9:
        sign_position_1: str|list = input("Enter (sign and position): ")
        sign_position_2: str|list = input("Enter (sign and position): ")
        sign_position_1: str|list = sign_position_1.split()
        sign_position_2: str|list = sign_position_2.split()
        if attempts <= 5:
            insert_signs(tuple(sign_position_1), tuple(sign_position_2), arrange, attempts)
            for row in arrange:
                print(row)
            attempts += 1
            continue
        else:
            raise ValueError(f"trial test between {player_1} and {player_2} finished!")
def insert_signs(sign_pos_1: tuple, sign_pos_2: tuple, arrange: list[Any], attempts) -> list:
    sign_1: str = sign_pos_1[0]
    pos_num_1: int  = int(sign_pos_1[1])
    count: int = 1
    Flag_stop: bool = None
    if attempts <= 5:
        index_row, index_value = 0, 0
        for index_r, row in enumerate(arrange):
            if Flag_stop == True:
                break
            for index_c, value in enumerate(row):
                if pos_num_1 == count:
                    if value == '':
                        index_row = index_r
                        index_value = index_c
                        Flag_stop = True
                    break
                else:
                    count += 1
                    continue
        if Flag_stop == True:
            arrange[index_row][index_value] = sign_1

        Flag_stop = None
        index_row, index_value = 0, 0
        count: int = 1

        sign_2: str = sign_pos_2[0]
        pos_num_2: int = int(sign_pos_2[1])
        for index_r, row in enumerate(arrange):
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
            arrange[index_row][index_value] = sign_2
        return arrange
    else:
        pass

tic_tao_toy(player_1, player_2, attempts)