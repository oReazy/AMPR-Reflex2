"""

[ LOCALSTORAGE ]

Версия: 2.0-A | Последнее изменение: 02.01.2025

[2.0-A: Бета-версия обновления: изменения в локальном хранилище: переименование данных, улучшенное взаимодействие между функциями и беком]
[1.0: Введено в проект, введены базовые принципы]

"""

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import reflex as rx
import json, ast, datetime, time

from typing import Union, Tuple
from rxconfig import config

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import AMPR.database as database

# ————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

class Storage(rx.State):

    # Переменные, которые необходимо сохранять в localStorage и использовать их в будущем
    HASH: str = rx.LocalStorage('0', name='hash') # Хэш игрока, хранится всегда в localStorage

    # Глобальные переменные, их всегда необходимо использовать при необходимости
    USER = () # Хранение данных об игроке
    SERVER = () # Хранение данных об сервере

    serverOpenRegistation = 0 # Открыта ли регистрация?
    serverOpenAuth = 0 # Открыта ли авторизация?
    serverOpenGame = 0 # Открыта ли игра?

    inventory: dict
    inventoryCount: int
    inventoryDone: list[list[list[list[int, str, str, int, str, int, str, str, int]]]]
    inventoryPassport: str
    inventoryPassportMax: list[int, int, str, str]
    inventoryLicenses: list[int, int, int, int, int, int, int, int]
    inventoryHealth: int
    inventoryEat: int
    inventoryHealthInt: int
    inventoryEatInt: int
    inventorySorting = 'standart'

    async def checkState(self): # Независимая проверка стейтов у авторизированного игрока
        if self.USER[17] == 'welcome-1': return rx.redirect('/welcome-1')
        if self.USER[17] == 'welcome-2': return rx.redirect('/welcome-2')
        if self.USER[17] == 'welcome-3': return rx.redirect('/welcome-3')
        if self.USER[17] == 'welcome-4': return rx.redirect('/welcome-4')
        if self.USER[17] == 'welcome-5': return rx.redirect('/welcome-5')
        if self.USER[17] == 'welcome-6': return rx.redirect('/welcome-6')
        if self.USER[17] == 'welcome-7': return rx.redirect('/welcome-7')
        if self.USER[17] == 'welcome-8': return rx.redirect('/welcome-8')
        if self.USER[17] == 'welcome-9': return rx.redirect('/welcome-9')
        if self.USER[17] == 'welcome-10': return rx.redirect('/welcome-10')
        if self.USER[17] == 'welcome-11': return rx.redirect('/welcome-11')

    async def onLoad(self): # Базовая загрузка страницы (проверка на открытость игры, авторизацию, стейты и загрузку данных)
        self.SERVER = await database.getData('settings', 'id', '1') # Получаем данные с сервера
        tServerOpen = ast.literal_eval(str(self.SERVER[4])) # создаем локальную переменную и заносим данные об доступности сервера
        self.serverOpenRegistation = tServerOpen[0]
        self.serverOpenAuth = tServerOpen[1]
        self.serverOpenGame = tServerOpen[2]

        if self.serverOpenGame == 1:
            if self.HASH != '0':
                tUserCount = await database.getDataMultiCount('users', 'hash', f"'{self.HASH}'") # Получаем количество игроков с таким хэшем
                if tUserCount != 0:
                    self.USER = await database.getUserHash(f"'{self.HASH}'") # Устанавливаем данные игрока из его хэша
                    if self.USER[17] != '': # Если есть у игрока стейт, то обрабатываем его
                        return await self.checkState()
                else:
                    # Игрок с HASH не найден, необходимо тут сбросить хэш на 0 и оптравить человека на главную страницу
                    return [rx.clear_local_storage(), rx.redirect('/')]
            else:
                # Игрок просто не авторизован, переброс на главную страницу
                return rx.redirect('/')
        else:
            # Сервер в этом случае закрыт, переброс на страницу we'll be right back
            return rx.redirect('/we-be-right-back')

    async def onLoadInventory(self):
        if self.HASH != '0':
            self.SERVER = await database.getData('settings', 'id', '1')  # Получаем данные с сервера
            tServerOpen = ast.literal_eval(str(self.SERVER[4]))  # создаем локальную переменную и заносим данные об доступности сервера
            self.serverOpenRegistation = tServerOpen[0]
            self.serverOpenAuth = tServerOpen[1]
            self.serverOpenGame = tServerOpen[2]
            self.USER = await database.getUserHash(f"'{self.HASH}'")
            tSortInventory = json.loads(str(self.USER[16]))
            if self.inventorySorting == 'standart':
                self.inventory = tSortInventory
            if self.inventorySorting == 'up-to-down':
                self.inventory = dict(sorted(tSortInventory.items(), key=lambda item: item[1], reverse=True))
            if self.inventorySorting == 'down-to-up':
                self.inventory = dict(sorted(tSortInventory.items(), key=lambda item: item[1]))
            if self.inventorySorting == 'a-z':
                self.inventory = dict(sorted(tSortInventory.items()))
            if self.inventorySorting == 'z-a':
                self.inventory = dict(sorted(tSortInventory.items(), reverse=True))
            count = 0
            self.inventoryCount = 0
            massive = []
            line = []
            for NAME in self.inventory:
                if count > 3:
                    massive.append(line)
                    count = 0
                    line = []
                    count = count + 1
                    self.inventoryCount = self.inventoryCount + 1
                    NAME_ITEM = await database.getDataMulti('items', 'names', f"'{NAME}'")
                    NAME_UPPER = str(NAME_ITEM[0][1]).upper()
                    HINT_INFO = ast.literal_eval(NAME_ITEM[0][5])
                    MASSIVE_ITEM = [NAME_ITEM[0][0], NAME_UPPER, NAME_ITEM[0][2], NAME_ITEM[0][3], NAME_ITEM[0][4], HINT_INFO, NAME_ITEM[0][6], NAME_ITEM[0][7], self.inventory[NAME], NAME_ITEM[0][1]]
                    line.append(MASSIVE_ITEM)
                else:
                    count = count + 1
                    self.inventoryCount = self.inventoryCount + 1
                    NAME_ITEM = await database.getDataMulti('items', 'names', f"'{NAME}'")
                    NAME_UPPER = str(NAME_ITEM[0][1]).upper()
                    HINT_INFO = ast.literal_eval(NAME_ITEM[0][5])
                    MASSIVE_ITEM = [NAME_ITEM[0][0], NAME_UPPER, NAME_ITEM[0][2], NAME_ITEM[0][3], NAME_ITEM[0][4], HINT_INFO, NAME_ITEM[0][6], NAME_ITEM[0][7], self.inventory[NAME], NAME_ITEM[0][1]]
                    line.append(MASSIVE_ITEM)
            massive.append(line)
            self.inventoryDone = massive
            tInventoryPassport = ast.literal_eval(str(self.USER[21]))
            self.inventoryLicenses = ast.literal_eval(str(self.USER[27]))
            self.inventoryPassportMax = tInventoryPassport
            self.inventoryHealth = self.USER[29] / 100 * 100
            self.inventoryEat = self.USER[30] / 100 * 100
            self.inventoryHealthInt = int(self.USER[29])
            self.inventoryEatInt = int(self.USER[30])

            if tInventoryPassport[0] == 0:
                self.inventoryPassport = '0'
            else:
                self.inventoryPassport = '1'
            if self.USER[17] != '':  # Если есть у игрока стейт, то обрабатываем его
                return await self.checkState()
        else:
            return rx.redirect('/')
        if self.serverOpenGame == 0:
            return rx.redirect('/we-be-right-back')

    async def onLoadLite(self): # Простая загрузка страницы (используется на главной странице в основном, где можно дать общий доступ)
        self.SERVER = await database.getData('settings', 'id', '1') # Получаем данные с сервера
        tServerOpen = ast.literal_eval(str(self.SERVER[4])) # создаем локальную переменную и заносим данные об доступности сервера
        self.serverOpenRegistation = tServerOpen[0]
        self.serverOpenAuth = tServerOpen[1]
        self.serverOpenGame = tServerOpen[2]

        if self.serverOpenGame == 1:
            if self.HASH != '0':
                tUserCount = await database.getDataMultiCount('users', 'hash', f"'{self.HASH}'") # Получаем количество игроков с таким хэшем
                if tUserCount != 0:
                    self.USER = await database.getUserHash(f"'{self.HASH}'") # Устанавливаем данные игрока из его хэша
                else:
                    # Игрок с HASH не найден, необходимо тут сбросить хэш на 0 и оптравить человека на главную страницу
                    return [rx.clear_local_storage()]
        else:
            # Сервер в этом случае закрыт, переброс на страницу we'll be right back
            return rx.redirect('/we-be-right-back')
    async def onLoadWelcome(self):  # Базовая загрузка страницы (проверка на открытость игры, авторизацию, стейты и загрузку данных)
        self.SERVER = await database.getData('settings', 'id', '1')  # Получаем данные с сервера
        tServerOpen = ast.literal_eval(str(self.SERVER[4]))  # создаем локальную переменную и заносим данные об доступности сервера
        self.serverOpenRegistation = tServerOpen[0]
        self.serverOpenAuth = tServerOpen[1]
        self.serverOpenGame = tServerOpen[2]

        if self.serverOpenGame == 1:
            if self.HASH != '0':
                tUserCount = await database.getDataMultiCount('users', 'hash', f"'{self.HASH}'")  # Получаем количество игроков с таким хэшем
                if tUserCount != 0:
                    self.USER = await database.getUserHash(f"'{self.HASH}'")  # Устанавливаем данные игрока из его хэша
                    if self.USER[17] != '':  # Если есть у игрока стейт, то обрабатываем его
                        pass  # Тут будет обработка стейта
                    else:
                        return rx.redirect('/')
                else:
                    # Игрок с HASH не найден, необходимо тут сбросить хэш на 0 и оптравить человека на главную страницу
                    return [rx.clear_local_storage(), rx.redirect('/')]
            else:
                # Игрок просто не авторизован, переброс на главную страницу
                return rx.redirect('/')
        else:
            # Сервер в этом случае закрыт, переброс на страницу we'll be right back
            return rx.redirect('/we-be-right-back')

