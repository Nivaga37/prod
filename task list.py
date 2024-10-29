
tasks=[] # пустой массив можно сделать сохранение в файл

def new_task(tasks):   # новая штука
    newtask = input("Введите задачу")
    tasks.append(newtask)

def view_task(tasks): # показать все штуки
    for i in tasks:
        print(i) # можно добавить иф при пустом списке но обед кончился

def del_task(tasks): # удалить штуку по ее счету или индексу
# должно появляться с номерами нужно выводить numder с index(number)
    number = 1
    for i in tasks:
        print(number,i)
        number = number + 1
    deltask = int(input("какую номер задачи удалить?"))
    deltask = deltask - 1 # гребаные индексы
    if deltask <= number:
        tasks.pop(deltask)
    else:
        print ("ты че дурак чтоль?") 
        return

while True:   # бесконечные вопросы?????
    anser = int(input("что ты хочешь?\n1-добавить задачу\n2-посмотреть список\n3-удалить задачу\n4-выйти из проги\n"))
    if anser == 1:
        new_task(tasks)
    elif anser == 2:
        view_task(tasks)
    elif anser == 3:
        del_task(tasks)
    elif anser == 4:
        break
    else:
        print ("ты че дурак чтоль?")



