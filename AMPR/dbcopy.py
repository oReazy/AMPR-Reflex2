"""

DATABASE

Взаимодействие сервера с базой данных.

Версия: 2.0 | Последнее обновление: 02.01.2025

[2.0: Большая переработка взаимодействия базы данных со всем проектом. Переписаны SQL-запросы, переименование функций]
[1.5: Сокращение лишнего кода для Reflex]
[1.1: Обновлено под Telegram]
[1.0: Написана первая версия DATABASE.PY для чат-бота ВКонтакте]

"""

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import asyncio, json, re, random, datetime, aiomysql, string, random, ast

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

USER = 'root'
PASSWORD = ''
HOST = 'localhost'
DATABASE = 'amprnew'

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

loop = asyncio.get_event_loop()

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

async def connectBase():  # Подключение к БД
    connected = await aiomysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        db=DATABASE,
        loop=loop
    )
    return connected

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# ДОБАВЛЕНИЕ НОВЫХ ПОЛЬЗОВАТЕЛЕЙ
async def addNewAccount(username, password):  # Создание нового аккаунта в базе данных
    try:
        connection = await connectBase()
        characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
        HASH_GEN = ''.join(random.choices(characters, k=36))
        Temporary = await getData('settings', 'id', "'1'")
        Temporary = str(Temporary[9])
        Temporary = ast.literal_eval(Temporary)
        # ---------------------------------------------------------------------------------------------
        PASSPORT = [0, 0, 0]
        # ---------------------------------------------------------------------------------------------

        async with connection.cursor() as cursor:
            new_user = "INSERT INTO `users` (password, hash, nick, lvl, exp, dollars, euro, yen, pounds, bank_dollars, bank_euro, bank_yen, bank_pounds, donate, admin, inventory, state, avatar, sex, age, admin_info, passport) VALUES " \
                       f"('{password}', " \
                       f"'{HASH_GEN}', " \
                       f"'{username}', " \
                       f"'{Temporary[0]}', " \
                       f"'{Temporary[2]}', " \
                       f"'{Temporary[1]}', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'0', " \
                       f"'{Temporary[3]}', " \
                       f"'{Temporary[4]}', " \
                       "'{}', " \
                       f"'welcome-1', " \
                       f"'avatar0.png', " \
                       f"'', " \
                       f"'0', " \
                       "'{}', " \
                       f"\"{PASSPORT}\"" \
                       f")"
            await cursor.execute(new_user)
            await connection.commit()
            connection.close()
            print(f'\033[38m[\033[33m!\033[38m\033[38m[\033][\033[33mDEBUG\033[38m] Встречайте нового пользователя')
    except Exception as ex:
        print(f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Не удалось создать пользователя, причина: {ex}')
async def addNewData(table, keys, values):  # Создание нового аккаунта в базе данных
    try:
        connection = await connectBase()
        async with connection.cursor() as cursor:
            new_data = f"INSERT INTO `{table}` ({keys}) VALUES ({values})"
            await cursor.execute(new_data)
            await connection.commit()
            connection.close()
    except Exception as ex:
        print(f'\033[38m[\033[31m!\033[38m][\033[33mDEBUG\033[38m] Произошла ошибка в базе данных: {ex}')

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# ПОЛУЧЕНИЕ ДАННЫХ
async def getUserID(userID):  # получение данных пользователя
    connection = await connectBase()
    async with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `users` WHERE `id` = {userID}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        for row in rows:
            data = row
        connection.close()
    return data
async def getUserHash(userHash):  # получение данных пользователя из хэша
    connection = await connectBase()
    async with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `users` WHERE `hash` = {userHash}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        for row in rows:
            data = row
        connection.close()
    return data


async def getData(table, key, value):
    # получение данных (выводит только последнее)
    connection = await connectBase()
    async with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `{table}` WHERE {key} = {value}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        for row in rows:
            data = row
        connection.close()
    return data
async def getDataMulti(table, key, value):  # получение данных (выводит все)
    connection = await connectBase()
    async with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `{table}` WHERE {key} = {value}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        connection.close()
    return rows
async def getDataMultiCount(table, key, value):  # найти значения в базе данных. Выводит их количестве в БД
    count_row = 0
    connection = await connectBase()
    async with connection.cursor() as cursor:
        select_row = f"SELECT * FROM `{table}` WHERE `{key}` = {value}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        for row in rows:
            count_row = count_row + 1
        connection.close()
    return count_row

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# ИЗМЕНЕНИЕ ДАННЫХ
async def setUserID(userID, key, value):  # Изменение переменных у пользователя (по одной переменной)
    connection = await connectBase()
    async with connection.cursor() as cursor:
        update_row = f"UPDATE `users` SET {key} = {value} WHERE id = {userID}"
        await cursor.execute(update_row)
        await connection.commit()
        connection.close()
async def setUserHash(userHash, key, value):  # Изменение переменных у пользователя (по одной переменной)
    connection = await connectBase()
    async with connection.cursor() as cursor:
        update_row = f"UPDATE `users` SET {key} = {value} WHERE hash = {userHash}"
        await cursor.execute(update_row)
        await connection.commit()
        connection.close()

async def setData(table, where_key, where_value, key, value):  # Изменение переменных (по одной переменной)
    connection = await connectBase()
    async with connection.cursor() as cursor:
        update_row = f"UPDATE `{table}` SET {key} = {value} WHERE {where_key} = {where_value}"
        await cursor.execute(update_row, (table, key, value, where_key, where_value))
        await connection.commit()
        connection.close()
async def setDataMulti(table, keys, values):  # Изменение переменных (несколько переменных)
    connection = await connectBase()
    async with connection.cursor() as cursor:
        update_row = f"INSERT INTO `{table}` ({keys}) VALUES ({values})"
        await cursor.execute(update_row)
        await connection.commit()
        connection.close()

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# УДАЛЕНИЕ ДАННЫХ
async def deleteUser(where_key, where_value):  # Удаление данных пользователя
    connection = await connectBase()
    async with connection.cursor() as cursor:
        delete_row = f"DELETE from `user` WHERE `{where_key}` = {where_value}"
        await cursor.execute(delete_row)
        await connection.commit()
        connection.close()
async def deleteData(table, where_key, where_value):  # Удаление данных пользователя
    connection = await connectBase()
    async with connection.cursor() as cursor:
        delete_row = f"DELETE from `{table}` WHERE `{where_key}` = {where_value}"
        await cursor.execute(delete_row)
        await connection.commit()
        connection.close()

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# СОБСТВЕННЫЙ SQL-запрос
async def sqlRequest(sql):  # получение данных пользователя
    connection = await connectBase()
    async with connection.cursor() as cursor:
        select_row = f"{sql}"
        await cursor.execute(select_row)
        rows = await cursor.fetchall()
        connection.close()
    return rows

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# МАКРОСЫ

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

# ПРОЧЕЕ


# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————