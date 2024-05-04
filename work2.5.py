from datetime import datetime

dt_to_str = datetime.now()
type(dt_to_str)
res_str = datetime.strftime(dt_to_str, '%A, %B %d, %Y , %I:%M')


def r(arg0):
    print(arg0)


r('Доброе утро')
r('Сегодня ' + res_str)
