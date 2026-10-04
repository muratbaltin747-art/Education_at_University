# Tic-Tac-Toe (Console Game)

## Overview
This is a command-line implementation of the classic Tic-Tac-Toe game in Python. Two players take turns placing their signs on a 3x3 grid by specifying the sign and position. The game logs moves to a local CSV file during gameplay and records the final match details (including the full move sequence and the winner) to a PostgreSQL database.

## Prerequisites
- Python 3.x
- PostgreSQL server running locally
- `psycopg2` library (`pip install psycopg2`)

## Database Setup
The script connects to a local PostgreSQL database using the following default credentials:
- **Database Name**: `Tic Tao Toy`
- **User**: `postgres`
- **Password**: `12345678`
- **Host**: `localhost`

Make sure you have created the `Tic Tao Toy` database and a table named `journal_game` to store the game rounds.

## How to Play
1. Run the script: 
   ```bash
   python tic_tao_toy.py
   ```
2. Enter the names of `player_1` and `player_2`.
3. Players take turns entering their moves in the following format: `<Sign> <Position>` (e.g., `X 5`).
   - The grid positions are numbered 1 through 9 (like a standard numpad).
4. The game will detect horizontal, vertical, and diagonal winning conditions, or announce a draw.
5. After the game ends, the match summary is uploaded to the database.

## Files
- `tic_tao_toy.py`: The main game logic and database interaction script.
- `Lesson_01/Files/Round_Journal.csv`: A temporary CSV file used during gameplay to record moves before uploading them to the database.
