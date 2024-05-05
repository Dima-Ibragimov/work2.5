from datetime import datetime

dt_to_str = datetime.now()
type(dt_to_str)
res_str = datetime.strftime(dt_to_str, '%A, %B %d, %Y')


def today(name):
    print('Сегодня', name)


today(res_str)
today(res_str)
