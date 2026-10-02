from psycopg2 import connect

conn = connect(dbname= 'Tic Tao Toy', user= 'postgres', password= '12345678', host= 'localhost', port= 5432)
cursor = conn.cursor()

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

    user_1_move = ''.join(list_move_user_1)
    user_2_move = ''.join(list_move_user_2)
    winner: bool = None

    query = """ 
    
    INSERT INTO journal_game (round_counter, users_move, user_1_move, user_2_move, winner)
    VALUES(%s, %s, %s, %s, %s)

"""
    cursor.execute(query, (2,  correct_journal, user_1_move, user_2_move, winner))
    conn.commit()

    cursor.execute("SELECT * FROM journal_game;")
    print(cursor.fetchall())

    cursor.close()
    conn.close()