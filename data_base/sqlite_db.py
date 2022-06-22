import sqlite3 as sq
import datetime

nedelya = {0: ('PN', 'Понедельник'),
           1: ('VT', 'Вторник'),
           2: ('SR', 'Среда'),
           3: ('CHT', 'Четверг'),
           4: ('PT', 'Пятница')}


def sql_start():
    global base, cur
    base = sq.connect('data_base/bd_raspisanie.db')
    cur = base.cursor()

    if base:
        print('Data base connected OK!')


async def inc_day(day: int):
    return 0 if day > 4 else day


async def get_day(when=-1):
    if when < 0:
        return nedelya[await inc_day(datetime.datetime.today().weekday())]
    return nedelya[await inc_day(datetime.datetime.today().weekday() + when)]


async def getAll_schedule(when=-1):
    day = await get_day(when)
    res = f'<u>{day[1]}</u>\n\n'
    cur.execute(f'SELECT Id_group, {day[0]} FROM raspisanie')
    raspisaniya = cur.fetchall()

    for raspisanie in raspisaniya:
        cur.execute(f'SELECT NAME FROM groups WHERE id = {raspisanie[0]}')
        name = cur.fetchone()
        res = res + f'<b>{name[0]}</b>\n{raspisanie[1].rstrip()}\n\n'
    return res


async def getGroup_schedule(when=-1, *groups: str):
    day = await get_day(when)
    res = f'<u>{day[1]}</u>\n\n'
    exception_groups = []

    for group in groups:
        group_upper = group.upper()
        cur.execute(f'SELECT ID FROM groups WHERE NAME = "{group_upper}"')
        id_group = cur.fetchone()
        try:
            cur.execute(f"SELECT {day[0]}\
             FROM raspisanie where Id_group = '{id_group[0]}'")
        except TypeError:
            exception_groups.append(group)
            continue
        raspisanie = cur.fetchone()
        res = res + f'<b>{group_upper}</b>\n{raspisanie[0].rstrip()}\n\n'

    if exception_groups:
        res = res + f'\nТаких групп нет:\n-' + "\n-".join(exception_groups)

    return res
