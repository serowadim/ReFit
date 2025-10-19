import db
from datetime import date
import os

now = date.today()

def MainScreen(now = date.today()):
    os.system('clear')
    print('\n\n\n'+ str(now))
    meal = db.GetMeal(now)
    workout = db.GetWorkout(now)

    if meal:
        meal = meal[2]
        kkal = 0
        for i in range(len(meal)):
            kkal += int(meal[i][1]) * int(db.GetDish(meal[i][0])[2])
            meal[i][0] = db.GetDish(meal[i][0])[1]


        print('\nКалорий за сегодня:', kkal, '\n')
        for dish in meal:
            print(dish[0], dish[1])
    else:
        print('\nКалорий за сегодня: 0')

    if workout:
        workout = workout[2]
        for i in range(len(workout)):
            workout[i][0] = db.GetExercise(workout[i][0])[1]


        print('\nТренировка за сегодня\n')
        for exercise in workout:
            print(exercise[0], ' '.join(exercise[1:]))
    else:
        print('\nТренировки сгодня не было')

    print('\n1 Добавить прием пищи       5 Удалить прием пищи\n' \
            '2 Добавть тренировку        6 Удалить тренировку\n' \
            '3 Добавить блюдо            7 Удалить блюдо\n' \
            '4 Добавить упражнение       8 Удалить упражнение\n' \
            '9 Посмтореть историю')
    c = input()
    if c == '1':
        AddMealScreen()
        MainScreen()
    elif c == '2':
        AddWorkoutScreen()
        MainScreen()
    elif c == '3':
        AddDishScreen()
        MainScreen()
    elif c == '4':
        AddExerciseScreen()
        MainScreen()
    elif c == '5':
        DelMealScreen()
        MainScreen()
    elif c == '6':
        DelWorkoutScreen()
        MainScreen()
    elif c == '7':
        DelDishScreen()
        MainScreen()
    elif c == '8':
        DelExerciseScreen()
        MainScreen()
    elif c == '9':
        HistoryScreen()
        MainScreen()
    else:
        print('Я не знаю такой команды')
        MainScreen()


def AddMealScreen():
    os.system('clear')
    now = date.today()
    print('Добавление приема пищи\n\n')

    dishes = db.GetListDishes()
    if dishes:
        for i in dishes:
            print(i[0], i[1], i[2],'kkal')
    else:
        print('Список блюд пуст')

    print('\nВведите номер блюда и через пробел количество порций, закончите надписью "все"\n')
    dishes = []
    dish = input()
    while dish !='все':
        dish = list(map(int, dish.split()))
        dishes.append(dish)
        dish = input()
    meal_curr = db.GetMeal(now)
    if meal_curr:
        dishes += meal_curr[2]
        db.DelMeal(now)
    db.AddMeal(now, dishes)


def AddDishScreen():
    os.system('clear')
    now = date.today()
    print('Добавление блюда\n\n')

    dishes = db.GetListDishes()
    if dishes:
        for i in dishes:
            print(i[0], i[1], i[2],'kkal')
    else:
        print('Список блюд пуст')

    print('\nВведите название блюда и через пробел калорийность порции (100г), закончите надписью "все"\n')
    dishes = []
    dish = input()
    while dish !='все':
        dish = dish.split()
        dishes.append(dish)
        dish = input()

    for dish in dishes:
        db.AddDish(dish[0], int(dish[1]))


def DelMealScreen():
    os.system('clear')
    now = date.today()
    print('\nУдалить прием пищи\n')

    print('Введите дату в формате 2012-12-31\n')
    n = input()
    db.DelMeal(n)


def DelDishScreen():
    os.system('clear')
    now = date.today()
    print('\nУдалить блюдо\n')

    dishes = db.GetListDishes()
    if dishes:
        for i in dishes:
            print(i[0], i[1], i[2],'kkal')
    else:
        print('Список блюд пуст')

    print('\nВведите номер блюда\n')
    n = input()
    db.DelDish(n)


def HistoryScreen():
    os.system('clear')
    print('\nПросмотр истории\n')
    print('Чтобы посмотреть историю введите дату в формате 2012-12-31')
    now = input()
    MainScreen(now)


def AddWorkoutScreen():
    os.system('clear')
    now = date.today()

    print('Добавление тренировки\n\n')

    exercises = db.GetListExercises()
    if exercises:
        for i in exercises:
            print(i[0], i[1])
    else:
        print('Список упражнений пуст')

    print('\nВведите номер упражнения и через пробел вес, подходы и повторения, закончите надписью "все"\n')

    exercises = []
    exercise = input()
    while exercise !='все':
        exercise = exercise.split()
        exercise[0] = int(exercise[0])
        exercises.append(exercise)
        exercise = input()
    workout_curr = db.GetWorkout(now)
    if workout_curr:
        exercises += workout_curr[2]
        db.DelWorkout(now)
    db.AddWorkout(now, exercises)


def AddExerciseScreen():
    os.system('clear')
    now = date.today()
    print('Добавление упражнения\n\n')

    exercises = db.GetListExercises()
    if exercises:
        for i in exercises:
            print(i[0], i[1])
    else:
        print('Список упражнений пуст')

    print('\nВведите названия упражнений, закончите надписью "все"\n')
    exercises = []
    exercise = input()
    while exercise !='все':
        exercises.append(exercise)
        exercise = input()

    for exercise in exercises:
        db.AddExercise(exercise)

def DelExerciseScreen():
    os.system('clear')
    now = date.today()
    print('\nУдалить упражнение\n')

    exercises = db.GetListExercises()
    if exercises:
        for i in exercises:
            print(i[0], i[1])
    else:
        print('Список упражнений пуст')

    print('\nВведите номер упражнения\n')
    n = input()
    db.DelExercise(n)

def DelWorkoutScreen():
    os.system('clear')
    now = date.today()
    print('\nУдалить тренировку\n')

    print('Введите дату в формате 2012-12-31\n')
    n = input()
    db.DelWorkout(n)

MainScreen(now)