# import sys
# print(sys.version)

# import os
# os.getcwd()

# import datetime
# print(datetime.date.today().day)
# print(datetime.date.today().month)
# print(datetime.date.today().year)
#
# # вывод даты в формате гггг-мм-дд
# print(datetime.date.isoformat(datetime.date.today()))

# import time
# print(time.strftime("%I:%M"))
# print(time.strftime("%A %p"))

# from datetime import datetime
#
# odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
#         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
#         41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]
#
# right_this_minute = datetime.today().minute
#
# if right_this_minute in odds:
#     print('This minute seems a little odd.')
# else:
#     print('Not an odd minute.')

# for i in [1, 2, 3]:
#     print(i)

# for ch in 'Hi!':
#     print(ch)

# # Получаем инфорамцию о функции
# import random
# help(random.randint)

# # Случайное число в диапазоне
# import random
# print(random.randint(1, 60))

from datetime import datetime
import time
import random

odds = [ 1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

for i in range(5):
    right_this_minute = datetime.today().minute

    if right_this_minute in odds:
        print('This minute seems a little odd.')
    else:
        print('Not an odd minute.')
    wait_time = random.randint(1, 10)
    time.sleep(wait_time)
    
