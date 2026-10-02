from typing import Any
from psycopg2 import connect

"""
TODO list:
1) create the DB for this programm and add count of round (done)
2) fix and finish the diagonal checking in rules_of_games()
3) accomplish the else statement
4) fix error with parametr of function insert_signs when at the end only one person fill field
5) fix problem when user can fill wrong sign (when he  usually write "X", but after he'll write "O")
"""

"""
I could check all loops thank for gathering all indexes from rows and columns 
and take all combinations with one of the sign and compare it with list of winner indexes.
"""

# data from client's server
user_1: str = input("Who will move first?\nplayer_1: ")
user_2: str = input("player_2: ")
attempts: int = 1 

def tic_tao_toy(user_1: str, user_2: str, attempts: int):

    with open("Lesson_01\Files\Round_Journal.csv", 'w', encoding= "UTF8") as Journal:
        pass

    conn = connect(dbname= 'Tic Tao Toy', user= 'postgres', password= '12345678', host= 'localhost')
    cursor = conn.cursor()

    query = """
    
    SELECT round_counter FROM Journal_game ORDER BY round_counter desc LIMIT 1;

    """
    cursor.execute(query)
    get_list: list = cursor.fetchall()
    round_index: int = get_list[0][0]

    cursor.close()
    conn.close()

    array = [["", "", ""], ["", "", ""], ["", "", ""]]
    positions = [1,2,3,4,5,6,7,8,9]

    while attempts <= 5:
        if attempts == 5:
            sign_position_1: str|list = input("Enter (sign + spacebar + position): ")
            sign_position_1: str|list = sign_position_1.split()
        else:
            sign_position_1: str|list = input("Enter (sign + spacebar + position): ")
            sign_position_1: str|list = sign_position_1.split()
            sign_position_2: str|list = input("Enter (sign + spacebar + position): ") 
            sign_position_2: str|list = sign_position_2.split()
        try:
            if int(sign_position_1[1]) in positions:
                with open("Lesson_01/Files/Round_Journal.csv", "a", encoding= "UTF8") as Journal:
                    line = f"{sign_position_1[0]};{sign_position_1[1]}\n"
                    Journal.write(line)
            if int(sign_position_2[1]) in positions:
                with open("Lesson_01/Files/Round_Journal.csv", "a", encoding= "UTF8") as Journal:
                    line = f"{sign_position_2[0]};{sign_position_2[1]}\n"
                    Journal.write(line)
            else:
                raise IndexError
        except IndexError:
            print(f"Error, please type sign and position correctly:/n{user_1}: {sign_position_1}/n{user_2}: {sign_position_2}")
            continue
        if attempts < 3:
            insert_signs(tuple(sign_position_1), tuple(sign_position_2), array, attempts)
            for row in array:
                print(row)
            attempts += 1
            continue
        else: #this statement 'd accomlish from TODO
            insert_signs(tuple(sign_position_1), tuple(sign_position_2), array, attempts)
            sign_1, sign_2 = sign_position_1[0], sign_position_2[0]
            player_1,player_2 = (user_1, sign_1), (user_2, sign_2)
            winner: None|str = rules_of_game(array, player_1, player_2)
            print(f"winner is {winner}")
            break #temporary
    else:
        sent_data_to_DB(round_index)
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
    count_1: int = 0
    count_2: int = 0
    sign_1, sign_2 = player_1[1], player_2[1]
    None_count: int = 0
    Uncorrect_signs: list = [
    
    # Английские строчные буквы
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z',

    # Английские заглавные буквы
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z',

    # Русские строчные буквы
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 
    'н', 'п', 'р', 'с', 'т', 'у', 'ф', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 
    'э', 'ю', 'я',

    # Русские заглавные буквы
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 
    'Н', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 
    'Э', 'Ю', 'Я',

    # Цифры
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',

    # Знаки препинания и спецсимволы (стандартная раскладка)
    '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', 
    '=', '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '<', 
    '.', '>', '/', '?', ' ', '№'
 ]

    #horizontal checking
    for row in array:
        if count_1 == 3:
            user_1: str = player_1[0]
            return user_1
        if count_2 == 3:
            user_2: str = player_2[0]
            return user_2
        else:
            count_1, count_2 = 0, 0
        for value in row:
            if value == sign_1:
                count_1 += 1
                continue
            else:
                if value == sign_2:
                    count_2 += 1
                    continue
                else:# if field is empty
                    if value in Uncorrect_signs:
                        raise TypeError(f"Error, field was filled by {sign_1} and {sign_2}. Call the Author of programm!!!")
                    else:
                        continue
    else:
        if count_1 != 3 and count_2 != 3:
            None_count += 1

    row: int = 0
    column: int = 0

    #vertical checking
    while row <= 2:
        if count_1 == 3:
            user_1 = player_1[0]
            return user_1
        if count_2 == 3:
            user_2: str == player_2[0]
            return user_2
        else:
            count_1, count_2 = 0, 0
            column = 0
        while column <= 2:
            if array[column][row] == sign_1:
                count_1 += 1
            if array[column][row] == sign_2:
                count_2 += 1
            column += 1
            continue
        else:
            row += 1
            continue
    else:
        if count_1 != 3 and count_2 != 3:
            None_count += 1
    
    attempts: int = 0

    #diagonal checking
    while attempts <= 2:
        if array[attempts][attempts] == sign_1:
            count_1 += 1
        if array[attempts][attempts] == sign_2:
            count_2 += 1
        attempts += 1
        continue
    else:
        if count_1 == 3:
            user_1: str = player_1[0]
            return user_1
        if count_2 == 3:
            user_2: str = player_2[0]
            return user_2
        else:
            None_count += 1
    if None_count == 3:
        return None
    else:
        raise TypeError("Error, fields was filled by another signs (not only X and O)!!!")
def sent_data_to_DB(previous_round_index: int):
    with open(r"Lesson_01\Files\Round_Journal.csv", "r", encoding= "UTF8") as Journal:
        
        correct_journal: str = ''
        correct_row: str = ''
        list_move: list = []

        for item in Journal:
            if item[0] == "X":
                line = item.rstrip("\n")
                line = line.replace(";", " ")
                correct_row += line
            else:
                correct_row += item
                correct_row = correct_row.replace(";", " ")
                correct_row= correct_row[:3] + ";" + correct_row[3:]

                copy = correct_row.split(";")
                list_move.append(copy)

                correct_journal += correct_row
                correct_row = ''
                continue
        else:
            print(correct_journal)
        list_move_user_1: list = []
        list_move_user_2: list = []
        for moves in list_move:
            for move in moves:
                if move[0] == "X":
                    list_move_user_1.append(move)
                    list_move_user_1.append("\n")
                    continue
                else:
                    list_move_user_2.append(move)
                    continue

        user_1_move: str = ''.join(list_move_user_1)
        user_2_move: str = ''.join(list_move_user_2)
        winner: bool = None
        current_round: int = previous_round_index + 1 

        conn = connect(dbname= 'Tic Tao Toy', user= 'postgres', password= '12345678', host= 'localhost')
        cursor = conn.cursor()
        
        query = """ 

        INSERT INTO journal_game (round_counter, users_move, user_1_move, user_2_move, winner)
        VALUES(%s, %s, %s, %s, %s)

        """
        cursor.execute(query, (current_round,  correct_journal, user_1_move, user_2_move, winner))
        conn.commit()

        cursor.close()
        conn.close()
    
tic_tao_toy(user_1, user_2, attempts)