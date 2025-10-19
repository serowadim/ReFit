import sqlite3

def CreateDataBase():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dishes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            kkal INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            exercises TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            dishes TEXT NOT NULL
        )
    ''')
    AddExercise('Жим лежа')
    AddExercise('Становая тяга')
    AddExercise('Приседания со штангой')
    AddDish('Гречка', 343)
    AddDish('Рис', 130)
    AddDish('Куриная грудка (вареная)', 150)
    conn.commit()
    conn.close()


def DelDataBase():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM exercises")
    cursor.execute("DELETE FROM dishes")
    cursor.execute("DELETE FROM workouts")
    cursor.execute("DELETE FROM meals")

    conn.commit()
    conn.close()

DelDataBase()
CreateDataBase()