"""

[ STATES ]

Бэкенд Мэрии

"""
import ast, asyncio, random

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import reflex as rx
from rxconfig import config

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

import AMPR.database as database
from AMPR.states.localStorage import Storage as LS

# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

style = {"text-decoration": "none !important",  # Убираем подчёркивание
         "color": "inherit !important",  # Цвет наследуется от родителя
         "cursor": "hover",  # Убираем указатель на ссылке
        }
hover = {"color": "inherit !important",  # Цвет не меняется при наведении
        "text-decoration": "none !important",  # Подчёркивание не появляется
        "background-color": "transparent !important",  # Чтобы исключить изменения фона
        }

class State(LS):
    Stage = '1'
    isPassport = ''
    tDialogText = ''
    tDialogIcon = ''
    tDialogIconColor = ''
    tDialogButtons = ''
    tDialogImage = ''
    tDialogImageHeight = '250px'
    tDialogMassiveDone: list[list[list[str, str, str, str, str, str]]]
    tDialogDone = ''
    tIsActiveTimer = 0
    tActiveDialog = 0
    tActiveDialogKey = 0

    def startDialog(self):
        self.Stage = '1'
        self.tIsActiveTimer = 0
        self.tActiveDialog = random.randint(1000, 9999)
        # —————————————————————————————————————————————————————————————————————————————————————
        # Динамический рендеринг диалогов | v. 1.1
        self.tDialogIcon = 'message-circle'
        self.tDialogIconColor = 'blue'
        self.tDialogButtons = [
            ['message-circle', 'blue', 'blue', 'Да, верно', 'javascript:void(0);', '1'],
            ['message-circle', 'blue', 'blue', 'Извините, я ошибся', 'javascript:void(0);', '0'],
        ]
        self.tDialogText = 'Доброго времени суток. Я сотрудник мэрии, я так полагаю, что вам необходима услуга по получению паспорта, верно?'
        self.tDialogImage = ''
        self.tDialogImageHeight = ''
        self.dialog()
        # —————————————————————————————————————————————————————————————————————————————————————
        passport = ast.literal_eval(str(self.USER[21]))
        if passport[0] == 0:
            self.isPassport = '0'
        else:
            self.isPassport = '1'

    @rx.event(background=True)
    async def controlState(self, count):
        if self.Stage == '1':
            if count == '0':
                async with self:
                    return rx.redirect('/places/cityHall')
            if count == '1':
                async with self:
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    if self.isPassport == '1':
                        self.tDialogButtons = [
                            ['x', 'tomato', 'tomato', 'У вас нет старого паспорта', 'javascript:void(0);', '1'],
                            ['message-circle', 'blue', 'blue', 'Извините, я ошибся', 'javascript:void(0);', '0'],
                        ]
                    if self.isPassport == '0':
                        self.tDialogButtons = [
                            ['hand', 'blue', 'blue', 'Держите мой старый паспорт', 'javascript:void(0);', '2'],
                            ['message-circle', 'blue', 'blue', 'Извините, я ошибся', 'javascript:void(0);', '0'],
                        ]
                    self.tDialogText = 'Хорошо, пожалуйста, передайте ваш старый паспорт. После с помощью вашего старого паспорта, я смогу вам оформить новый'
                    self.tDialogImage = ''
                    self.tDialogImageHeight = ''
                    self.dialog()
            if count == '2':
                async with self:
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    self.tDialogButtons = [
                    ]
                    self.tDialogText = 'Ожидайте пожалуйста, мне необходимо проверить ваши данные для того, чтобы оформить вам новый паспорт, это может занять некоторое время.'
                    self.dialog()
                    self.tIsActiveTimer = 1
                    self.tActiveDialogKey = self.tActiveDialog
                await asyncio.sleep(10)
                async with self:
                    if self.tIsActiveTimer == 1 and self.tActiveDialogKey == self.tActiveDialog:
                        self.tIsActiveTimer = 0
                        self.tDialogIcon = 'message-circle'
                        self.tDialogIconColor = 'blue'
                        self.tDialogButtons = [
                            ['banknote', 'green', 'green', 'Заплатить 500 долларов', 'javascript:void(0);', '3'],
                            ['message-circle', 'blue', 'blue', 'Простите, но мне надо уйти', 'javascript:void(0);', '-1'],
                        ]
                        self.tDialogText = 'Итак я подготовила все необходимые документы для оформления паспорта, вы же знаете, что выпуск паспорта платный? Стоимость нового паспорта составит 500 долларов. Вы готовы сейчас заплатить?'
                        self.dialog()
                    else:
                        self.tIsActiveTimer = 0
            if count == '3':
                async with self:
                    self.USER = await database.getUserHash(f"'{self.HASH}'")
                    if self.USER[6] >= 500:
                        newBalance = self.USER[6] - 500
                        await database.setUserID(self.USER[0], 'dollars', f"'{newBalance}'")
                        self.tDialogIcon = 'message-circle'
                        self.tDialogIconColor = 'blue'
                        self.tDialogButtons = [
                            ['hand', 'blue', 'blue', 'Передать фотографии для паспорта', 'javascript:void(0);', '4'],
                        ]
                        self.tDialogText = 'Отлично, пожалуйста предоставьте ваши фотографии для паспорта'
                        self.dialog()
                        return rx.toast.success("Вы заплатили 500 долларов", position='top-right')
                    if self.USER[6] < 500:
                        return rx.toast.error("Вам нехватает денег", position='top-right')
            if count == '4':
                async with self:
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    self.tDialogButtons = [
                    ]
                    self.tDialogText = 'Отлично, сейчас я их прикреплю к паспорту и к остальным документам...'
                    self.dialog()
                    self.tIsActiveTimer = 1
                    self.tActiveDialogKey = self.tActiveDialog
                await asyncio.sleep(5)
                async with self:
                    if self.tIsActiveTimer == 1 and self.tActiveDialogKey == self.tActiveDialog:
                        self.tIsActiveTimer = 0
                        self.tDialogIcon = 'message-circle'
                        self.tDialogIconColor = 'blue'
                        self.tDialogButtons = [
                        ]
                        self.tDialogText = 'Фотографии прикреплены к вашим документам, ждем пока ответит паспортная система'
                        self.dialog()
                        self.tIsActiveTimer = 1
                    else:
                        self.tIsActiveTimer = 0
                await asyncio.sleep(10)
                async with self:
                    if self.tIsActiveTimer == 1 and self.tActiveDialogKey == self.tActiveDialog:
                        self.tIsActiveTimer = 0
                        self.tDialogIcon = 'message-circle'
                        self.tDialogIconColor = 'blue'
                        self.tDialogButtons = [
                            ['hand', 'blue', 'blue', 'Забрать паспорт', 'javascript:void(0);', '5'],
                        ]
                        self.tDialogText = 'Отлично, все данные теперь находятся в реестре. Это ваш паспорт, если вдруг вы его потеряете, то вы сможете снова обратится к мэрию, но заранее сообщаю, что перевыпуск паспорта стоит денег, поэтому будьте осторожнее. Вы можете забрать свой паспорт'
                        self.dialog()
                    else:
                        self.tIsActiveTimer = 0
            if count == '5':
                async with self:
                    tInventoryPassport = ast.literal_eval(str(self.USER[21]))
                    newPassport = [1, random.randint(100000, 999999), tInventoryPassport[2], tInventoryPassport[3]]
                    await database.setUserID(self.USER[0], 'passport', f"\"{newPassport}\"")
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    self.tDialogButtons = [
                        ['message-circle', 'blue', 'blue', 'Спасибо, до свидания', 'javascript:void(0);', '0'],
                    ]
                    self.tDialogText = 'Спасибо, что обратились в мэрию, хорошего дня.'
                    self.dialog()
                    return rx.toast.info("Вы получили паспорт", position='top-right')
            if count == '-1':
                async with self:
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    self.tDialogButtons = [
                        ['message-circle', 'blue', 'blue', 'Учту, хорошего дня.', 'javascript:void(0);', '0'],
                    ]
                    self.tDialogText = 'Хорошо, но помните, что паспорт — это важно. С получением паспорта у вас откроется множество возможнсотей и пособий от государства'
                    self.dialog()


    def dialog(self):
        count = 0
        massive = []
        line = []
        for NAME in self.tDialogButtons:
            if count > 1:
                massive.append(line)
                count = 0
                line = []
                count = count + 1
                MASSIVE_ITEM = [NAME[0], NAME[1], NAME[2], NAME[3], NAME[4], NAME[5]] # [ИКОНКА, ЦВЕТ ИКОНКИ, ЦВЕТ КНОПКИ, ТЕКСТ, ССЫЛКА]
                line.append(MASSIVE_ITEM)
            else:
                count = count + 1
                MASSIVE_ITEM = [NAME[0], NAME[1], NAME[2], NAME[3], NAME[4], NAME[5]]
                line.append(MASSIVE_ITEM)
        massive.append(line)
        self.tDialogMassiveDone = massive