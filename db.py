import sqlite3
import json



def CreateDataBase():
    # Подключение к БД (создаст файл, если его нет)
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    # Создание таблиц
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exercise (
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
    # Закрытие соединения
    conn.close()


def AddExercise(name):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO exercise (name) VALUES (?)", (name, ))

    # Сохранение изменений
    conn.commit()
    conn.close()
    

def GetExercise(id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM exercise WHERE id = ?", (id,))
    return cursor.fetchone()

    conn.close()


def DelExercise(id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM exercise WHERE id = ?", (id,))

    conn.commit()
    conn.close()


def EditExercise(id, name):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE exercise SET name = ? WHERE id = ?", (name, id))

    conn.commit()
    conn.close()


def AddDish(name, kkal):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO dishes (name, kkal) VALUES (?, ?)", (name, kkal,))

    # Сохранение изменений
    conn.commit()
    conn.close()
    

def GetDish(id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dishes WHERE id = ?", (id,))
    return cursor.fetchone()

    conn.close()


def GetListDishes():
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM dishes")
    return cursor.fetchall()

    conn.close()

def DelDish(id):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM dishes WHERE id = ?", (id,))

    conn.commit()
    conn.close()


def EditDish(id, name, kkal):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE dishes SET name = ?, kkal = ? WHERE id = ?", (name, kkal, id))

    conn.commit()
    conn.close()


def AddWorkout(date, exercises):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    json_list = json.dumps(exercises, ensure_ascii=False)


    cursor.execute("INSERT INTO workouts (date, exercises) VALUES (?, ?)", (date, json_list,))

    # Сохранение изменений
    conn.commit()
    conn.close()
    

def GetWorkout(date):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM workouts WHERE date = ?", (date,))

    row = cursor.fetchone()
    if row: 
        row = list(row)
        row[2] = json.loads(row[2])
    return row


    conn.close()


def DelWorkout(date):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM workouts WHERE date = ?", (date,))

    conn.commit()
    conn.close()


def EditWorkout(date, exercises):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    json_list = json.dumps(exercises, ensure_ascii=False)
    cursor.execute("UPDATE workouts SET date = ?, exercises = ? WHERE date = ?", (date, json_list, date, ))

    conn.commit()
    conn.close()


def AddMeal(date, dishes):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    json_list = json.dumps(dishes, ensure_ascii=False)


    cursor.execute("INSERT INTO meals (date, dishes) VALUES (?, ?)", (date, json_list,))

    # Сохранение изменений
    conn.commit()
    conn.close()
    

def GetMeal(date):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM meals WHERE date = ?", (date,))

    row = cursor.fetchone()
    if row:
        row = list(row)
        row[2] = json.loads(row[2])
    return row


    conn.close()


def DelMeal(date):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM meals WHERE date = ?", (date,))

    conn.commit()
    conn.close()


def EditMeal(date, dishes):
    conn = sqlite3.connect('main.db')
    cursor = conn.cursor()

    json_list = json.dumps(dishes, ensure_ascii=False)
    cursor.execute("UPDATE meals SET date = ?, dishes = ? WHERE date = ?", (date, json_list, date, ))

    conn.commit()
    conn.close()

CreateDataBase()