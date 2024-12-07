import asyncio
import time


timeaut=12

async def start_strongman(name, power):
    '''
    start_strongman - функция описывает соревнования.Является асинхрооной.
    каждый участник выполняет поднятие шаров со скоростью пропорционально
    своей силе не ожидая очередности.
    :param name: Имя участника
    :param power: Мощность в кВт
    :return:
    '''
    print(f'Силач {name} начал соревнования.')
    start=time.time()
    #Начало цикла соревнований
    for i in range(5):
        #поднятие шаров от 1 до 5
        await asyncio.sleep(timeaut / power)
        #задержка поднятия шара, чем сильнее участник тем, меньше задержка.
        #await - пока asyncio.sleep(timeaut / power) не отработает, не переходит
        print(f'Силач {name} поднял шар {i+1}.')

    finish=time.time()
    # Конец цикла соревнований
    time_tour=round(finish-start,2)
    #Время на выполнение
    print(f'Силач {name} закончил соревнования.Время :{time_tour}сек.')

async def start_tournament():
    #start_tournament - функция Является асинхрооной. передает параметры
    #участников name и pover в соревнования start_strongman

    task_ilia=asyncio.create_task(start_strongman('Илья',6))
    #задача task_ilia, которая будет работать в асинхронном режиме.
    #задача запустится, и основная программа продолжит выполнение.
    task_nik=asyncio.create_task(start_strongman('Никита', 4))
    #задача task_nik, которая будет работать в асинхронном режиме.
    #задача запустится, и основная программа продолжит выполнение.
    task_alex=asyncio.create_task(start_strongman('Алёша', 3))
    #задача task1_alex, которая будет работать в асинхронном режиме.
    #задача запустится, и основная программа продолжит выполнение.
    await task_ilia
    await task_nik
    await task_alex
    #«await» чтобы программа не завершалась, пока задачи не отработают

asyncio.run(start_tournament())
#«start_tournament» запускаем через «asyncio.run» для запуска асинхронного потока