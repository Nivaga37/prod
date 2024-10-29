
tasks=[] # пустой массив можно сделать сохранение в файл

def new_task(tasks):   # новая штука
    newtask = input("Введите текст задачи:")
    tasks.append(newtask)
    print ("Задача добавлена!") 

def view_task(tasks): # показать все штуки
    print ("Список задач:")
    number = 1
    for i in tasks:
        print(number,i, sep=", ")
        number = number + 1

def del_task(tasks): # удалить штуку по ее индексу
    number = 1
    for i in tasks:
        print(number,i, sep=", ")
        number = number + 1
    deltask = int(input("Выберите номер задачи для удаления:"))
    deltask = deltask - 1 # гребаные индексы
    if deltask <= number:
        tasks.pop(deltask)
        print ("Задача удалена.")
    else:
        print ("Неправильно") 
        return

while True:   # бесконечные вопросы?????
    anser = int(input("Выберите действие:\n1. Добавить задачу\n2. Просмотреть список задач\n3. Удалить задачу\n4. Выйти из программы\n"))
    if anser == 1:
        new_task(tasks)
    elif anser == 2:
        view_task(tasks)
    elif anser == 3:
        del_task(tasks)
    elif anser == 4:
        print ("Программа завершена.")
        break
    else:
        print ("Неправильно")



