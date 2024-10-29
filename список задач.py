
tasks=[] # пустой массив можно сделать сохранение в файл

while True:   # бесконечные вопросы
    def greet(anser):  
       anser=input("что ты хочешь?\n1-добавить задачу\n2-посмотреть список\n3-удалить задачу")
       if anser == 1:
            new_task()
       elif anser == 2:
             view_task()
       elif anser == 3:
            del_task()
       else:
       print ("ты че дурак чтоль?")
    break

   
def new_task():   # новая штука
new_task=input("Введите задачу")
list.append(new_task)


def view_task(): # показать все штуки
    print 


def del_task(): # удалить штуку по ее счету или индексу 
# должно появляться с номерами нужно выводить numder с index(number)
    list.count()
    
    for i in range()
    
    list.pop
    