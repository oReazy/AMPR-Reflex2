"""

[ STATES ]

Бэкенд центра лицензирования

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

    COUNT_QUESTIONS = 0
    COUNT_OK = 0

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
            ['message-circle', 'blue', 'blue', 'Мне пора, до свидания', 'javascript:void(0);', '0'],
        ]
        self.tDialogText = 'Здраствуйте, вы желаете получить права на управление автомобилями, верно?'
        self.tDialogImage = ''
        self.tDialogImageHeight = ''
        self.dialog()
        # —————————————————————————————————————————————————————————————————————————————————————
        passport = ast.literal_eval(str(self.USER[21]))
        if passport[0] == 0:
            self.isPassport = '0'
        else:
            self.isPassport = '1'

    def startDialog2(self):
        self.Stage = '1'
        self.tIsActiveTimer = 0
        self.tActiveDialog = random.randint(1000, 9999)
        # —————————————————————————————————————————————————————————————————————————————————————
        # Динамический рендеринг диалогов | v. 1.1
        self.tDialogIcon = 'message-circle'
        self.tDialogIconColor = 'blue'
        self.tDialogButtons = [
            ['message-circle', 'blue', 'blue', 'Да, верно', 'javascript:void(0);', '1'],
            ['message-circle', 'blue', 'blue', 'Мне пора, до свидания', 'javascript:void(0);', '0'],
        ]
        self.tDialogText = 'Здраствуйте, вы желаете получить права на управление мотоциклами, верно?'
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
    async def controlState2(self, count):
        if self.Stage == '1':
            if count == '0':
                async with self:
                    return rx.redirect('/places/licensing-center')
            if count == '1':
                async with self:
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    if self.isPassport == '1':
                        self.tDialogButtons = [
                            ['hand', 'blue', 'blue', 'Передать паспорт', 'javascript:void(0);', '2'],
                            ['message-circle', 'blue', 'blue', 'Извините, я ошибся', 'javascript:void(0);', '0'],
                        ]
                    if self.isPassport == '0':
                        self.tDialogButtons = [
                            ['x', 'tomato', 'tomato', 'У вас нет паспорта данного штата', 'javascript:void(0);', '1'],
                            ['message-circle', 'blue', 'blue', 'Извините, я ошибся', 'javascript:void(0);', '0'],
                        ]
                    self.tDialogText = 'Отлично, можете пожалуйста передать ваш паспорт для того, чтобы я зарегистрировал вас как кандидата на получение прав'
                    self.tDialogImage = ''
                    self.tDialogImageHeight = ''
                    self.dialog()
            if count == '2':
                async with self:
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    self.tDialogButtons = [
                    ]
                    self.tDialogText = 'Спасибо, подождите пожалуйста минуту, сейчас зарегистрирую вас в системе...'
                    self.dialog()
                    self.tIsActiveTimer = 1
                    self.tActiveDialogKey = self.tActiveDialog
                await asyncio.sleep(10)
                async with self:
                    if self.tIsActiveTimer == 1 and self.tActiveDialogKey == self.tActiveDialog:
                        self.tIsActiveTimer = 0
                        tLicenses = ast.literal_eval(str(self.USER[27]))
                        if tLicenses[1] == 0:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['banknote', 'green', 'green', 'Заплатить 150 долларов', 'javascript:void(0);', '3'],
                                ['message-circle', 'blue', 'blue', 'Простите, но мне надо уйти', 'javascript:void(0);', '0'],
                            ]
                            self.tDialogText = 'Зарегистрировал вас как кандидата. Получение прав на мотоцикл сложнее, чем на автомобили, так-как могут попадаться вопросы без картинки. Стоимость прохождения - 150 долларов, это одна попытка. Если вы не сдаете тест, то после этого вы снова платите 150 долларов. Вы готовы заплатить?'
                            self.dialog()
                        else:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Простите, ошибся', 'javascript:void(0);', '0'],
                            ]
                            self.tDialogText = 'Простите, но вы уже сдавали тест на мотоциклы и у вас уже есть лицензия. Мы не можем вам предложить пройти тест повторно.'
                            self.dialog()
                    else:
                        self.tIsActiveTimer = 0
            if count == '3':
                async with self:
                    self.USER = await database.getUserHash(f"'{self.HASH}'")
                    if self.USER[6] >= 150:
                        newBalance = self.USER[6] - 150
                        await database.setUserID(self.USER[0], 'dollars', f"'{newBalance}'")
                        self.tDialogIcon = 'message-circle'
                        self.tDialogIconColor = 'blue'
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Хорошо', 'javascript:void(0);', '4'],
                        ]
                        self.tDialogText = 'Если вы готовы, то пройдите в учебный класс для сдачи теста'
                        self.dialog()
                        return rx.toast.success("Вы заплатили 150 долларов", position='top-right')
                    if self.USER[6] < 150:
                        return rx.toast.error("Вам нехватает денег", position='top-right')
            if count == '4':
                async with self:
                    self.COUNT_QUESTIONS = 0
                    self.COUNT_OK = 0
                    self.tIsActiveTimer = 0
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    self.tDialogButtons = [
                        ['hand', 'blue', 'blue', 'Начать выполнять тест', 'javascript:void(0);', '5'],
                    ]
                    self.tDialogText = 'Итак, сейчас у вас будет 15 вопросов, вдумчиво читайте вопрос и правильно отвечайте на них.'
                    self.dialog()
            if count == '5':
                async with self:
                    self.tIsActiveTimer = 0
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    tRandomQuestion = random.randint(0, 28)
                    if tRandomQuestion == 0:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота направо.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Дорога поворачивает налево, затем направо.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота налево.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Скользкий, когда мокрый.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот предупреждающий знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-1.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 1:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Предупреждение о том, что впереди знак «Стоп».', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Движение в прямом направлении запрещено.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Неправильный путь, нельзя въезжать.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Предупреждение о необходимости немедленно остановиться.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-2.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 2:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди заканчивается тротуар.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Полоса заканчивается впереди.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди строительство дороги.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Дорога впереди закрыта.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот предупреждающий знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-3.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 3:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди знак «Стоп».', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Ограничение скорости снижено, впереди школьная зона.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Впереди школьный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди зона окончания школы.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот предупреждающий знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-4.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 4:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Церковный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Только пешеходное движение.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-5.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 5:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди четырехсторонний перекресток.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди перекресток второстепенных дорог.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди предупреждение о перекрестке, дорога заканчивается, необходимо повернуть направо или налево.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Впереди перекресток Y.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-6.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 6:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Разворот запрещен.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Кривая.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Поверните направо или налево.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Движение транспорта осуществляется только в направлении стрелки.', 'javascript:void(0);', '6'],
                        ]
                        self.tDialogText = 'Этот дорожный знак означает?'
                        self.tDialogImage = '/images/places/Licensing Center/question-7.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 7:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Въезд запрещен', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Эта дорога или улица заканчивается впереди.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Впереди заканчивается двустороннее движение.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Не в ту сторону, развернись.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот предупреждающий знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-8.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 8:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'На улице играть нельзя.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Парковка запрещена.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Обгон запрещен.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Движение пешеходов запрещено.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-9.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 9:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Только пешеходы, движение транспорта запрещено.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Предупреждение о посещении школы: вы въезжаете на территорию школы.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Впереди пешеходный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Предупреждающий знак «Впереди пешеходы».', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-10.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 10:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Справа приближается транспортный поток.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Правая полоса заканчивается впереди, держитесь левой стороны.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Впереди разделительная полоса.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-11.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 11:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Полностью остановитесь у знака и уступите дорогу транспортному средству.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Снизьте скорость, приближаясь к перекрестку.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Снизьте скорость, при необходимости полностью остановитесь, уступите дорогу движению.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Дорога закрыта, не въезжать.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-12.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 12:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Движение автотранспортных средств запрещено.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Пешеходного перехода нет.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-13.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 13:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди съезд.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Низкий клиренс впереди.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Дорога впереди сужается.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди дорога под водой.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот предупреждающий знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-14.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 14:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Движение транспорта только справа.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Движение транспорта только левостороннее.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Ваша полоса закончится впереди.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Не проезжайте мимо этого знака, развернитесь.', 'javascript:void(0);', '6'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-15.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 15:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Перекресток.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Железнодорожный переезд.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Зона взрывных работ.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Этот знак предупреждает о приближении'
                        self.tDialogImage = '/images/places/Licensing Center/question-16.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 16:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Охота запрещена.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Территория заповедника.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди переходят дорогу олени.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Территория государственного парка.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-17.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 17:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди обратный поворот.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди одностороннее движение.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди начинается разделенное шоссе.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди заканчивается разделенная автомагистраль.', 'javascript:void(0);', '6'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-18.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 18:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Движение по центральной полосе может идти прямо или поворачивать налево.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Поворот направо возможен только с центральной полосы.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Центральная полоса сливается в одну полосу', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Движение по центральной полосе должно поворачивать налево.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Эта разметка на тротуаре сообщает вам, что на перекрестке впереди'
                        self.tDialogImage = '/images/places/Licensing Center/question-19.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 19:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Общий знак обслуживания больницы.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Общий знак для кабинета врача.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Общий знак обслуживания аптеки.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Общий знак для парковки.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-20.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 20:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Снизьте скорость, в идеальных условиях максимальная рекомендуемая скорость составляет 25 миль в час.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час в идеальных условиях.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Снизьте скорость, максимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак ограничения скорости на повороте?'
                        self.tDialogImage = '/images/places/Licensing Center/question-21.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 21:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Вы можете ехать только прямо.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Двигаться можно только в направлении зеленой стрелки.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Вам нужно дождаться зеленого света.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Транспортные средства, движущиеся в любом направлении, должны остановиться.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Светофор с зеленой стрелкой и красным светом означает, что'
                        self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 22:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Необходимо остановиться перед выездом на нее', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Необходимо уступить дорогу водителям, находящимся на кольцевой развязке или перекрестке с круговым движением', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Имеют преимущественное право проезда, если они прибудут первыми', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Иметь преимущественное право проезда, если есть две полосы движения', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Водители, въезжающие на кольцевую или перекресток с круговым движением:'
                        self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 23:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Сигнальные огни', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Другие автомобили на дороге', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Время суток', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Состояние дороги', 'javascript:void(0);', '6'],
                        ]
                        self.tDialogText = 'На вашу способность останавливаться влияют:'
                        self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 24:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Чтобы остановиться, нужно преодолеть большее расстояние, чем автомобилям.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Требуется меньше времени для перехода на более низкую передачу, чем у автомобилей', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Требуют меньшего радиуса поворота, чем автомобили', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Требуют меньше времени для прохождения подъёма, чем автомобили', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'При совместном движении по дороге с грузовым автомобилем важно помнить, что, как правило, грузовые автомобили:'
                        self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 25:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Избегайте резких поворотов и торможений.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Проверьте сцепление шин с дорогой при движении в гору.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Уменьшите расстояние, на которое вы смотрите перед своим автомобилем.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Дороги скользкие после того, как только начинается дождь. Когда дорога скользкая, вам следует:'
                        self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 26:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Общий информационный знак автовокзала.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Общий информационный знак для стоянки автофургонов.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Общий информационный знак для стоянки грузовиков.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Общий информационный знак для стоянки мобильных домов.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-22.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 27:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Они устраняются, если у вас по одному наружному зеркалу с каждой стороны автомобиля.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Большие грузовики имеют большие слепые зоны, чем большинство легковых автомобилей.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Слепые зоны можно проверить, посмотрев в зеркала заднего вида.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Какое из следующих утверждений о слепых зонах верно?'
                        self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 28:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Если другой водитель подает вам сигнал продолжать движение.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Если школьный автобус не движется и мигают красные огни.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Если школьный автобус находится в движении.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Все вышеперечисленное.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'В какое время вам разрешено обгонять школьный автобус?'
                        self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                        self.tDialogImageHeight = '232px'
                    self.dialog()
            if count == '6':
                async with self:
                    self.COUNT_QUESTIONS = self.COUNT_QUESTIONS + 1
                    self.COUNT_OK = self.COUNT_OK + 1
                    if self.COUNT_QUESTIONS == 15:
                        if self.COUNT_OK > 11:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['hand', 'blue', 'blue', 'Получить права', 'javascript:void(0);', '8'],
                            ]
                            self.tDialogText = f'Поздравляем, вы сдали тест. Число верных ответов: {self.COUNT_OK} из {self.COUNT_QUESTIONS}. Вы теперь можете получить права'
                            self.tDialogImage = ''
                            self.tDialogImageHeight = ''
                            self.dialog()
                        else:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Окей', 'javascript:void(0);', '0'],
                            ]
                            self.tDialogText = f'Извините, но вы не сдали тест. Число верных ответов: {self.COUNT_OK} из {self.COUNT_QUESTIONS}. Попробуйте снова'
                            self.tDialogImage = ''
                            self.tDialogImageHeight = ''
                            self.dialog()
                    else:
                        self.tIsActiveTimer = 0
                        self.tDialogIcon = 'message-circle'
                        self.tDialogIconColor = 'blue'
                        tRandomQuestion = random.randint(0, 28)
                        if tRandomQuestion == 0:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота направо.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога поворачивает налево, затем направо.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота налево.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Скользкий, когда мокрый.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-1.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 1:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Предупреждение о том, что впереди знак «Стоп».', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Движение в прямом направлении запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Неправильный путь, нельзя въезжать.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждение о необходимости немедленно остановиться.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-2.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 2:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается тротуар.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Полоса заканчивается впереди.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди строительство дороги.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Дорога впереди закрыта.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-3.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 3:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди знак «Стоп».', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Ограничение скорости снижено, впереди школьная зона.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди школьный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди зона окончания школы.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-4.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 4:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Церковный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Только пешеходное движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-5.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 5:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди четырехсторонний перекресток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди перекресток второстепенных дорог.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди предупреждение о перекрестке, дорога заканчивается, необходимо повернуть направо или налево.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди перекресток Y.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-6.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 6:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Разворот запрещен.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Кривая.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Поверните направо или налево.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение транспорта осуществляется только в направлении стрелки.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Этот дорожный знак означает?'
                            self.tDialogImage = '/images/places/Licensing Center/question-7.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 7:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Въезд запрещен', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Эта дорога или улица заканчивается впереди.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается двустороннее движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Не в ту сторону, развернись.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-8.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 8:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'На улице играть нельзя.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Парковка запрещена.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Обгон запрещен.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение пешеходов запрещено.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-9.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 9:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Только пешеходы, движение транспорта запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждение о посещении школы: вы въезжаете на территорию школы.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждающий знак «Впереди пешеходы».', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-10.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 10:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Справа приближается транспортный поток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Правая полоса заканчивается впереди, держитесь левой стороны.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди разделительная полоса.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-11.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 11:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Полностью остановитесь у знака и уступите дорогу транспортному средству.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, приближаясь к перекрестку.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, при необходимости полностью остановитесь, уступите дорогу движению.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога закрыта, не въезжать.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-12.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 12:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение автотранспортных средств запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходного перехода нет.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-13.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 13:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди съезд.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Низкий клиренс впереди.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога впереди сужается.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди дорога под водой.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-14.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 14:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение транспорта только справа.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение транспорта только левостороннее.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Ваша полоса закончится впереди.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Не проезжайте мимо этого знака, развернитесь.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-15.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 15:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Перекресток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Железнодорожный переезд.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Зона взрывных работ.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Этот знак предупреждает о приближении'
                            self.tDialogImage = '/images/places/Licensing Center/question-16.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 16:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Охота запрещена.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Территория заповедника.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди переходят дорогу олени.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Территория государственного парка.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-17.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 17:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди обратный поворот.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди одностороннее движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди начинается разделенное шоссе.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается разделенная автомагистраль.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-18.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 18:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение по центральной полосе может идти прямо или поворачивать налево.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Поворот направо возможен только с центральной полосы.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Центральная полоса сливается в одну полосу', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение по центральной полосе должно поворачивать налево.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Эта разметка на тротуаре сообщает вам, что на перекрестке впереди'
                            self.tDialogImage = '/images/places/Licensing Center/question-19.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 19:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Общий знак обслуживания больницы.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий знак для кабинета врача.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий знак обслуживания аптеки.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Общий знак для парковки.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-20.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 20:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, в идеальных условиях максимальная рекомендуемая скорость составляет 25 миль в час.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час в идеальных условиях.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, максимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак ограничения скорости на повороте?'
                            self.tDialogImage = '/images/places/Licensing Center/question-21.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 21:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Вы можете ехать только прямо.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Двигаться можно только в направлении зеленой стрелки.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Вам нужно дождаться зеленого света.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Транспортные средства, движущиеся в любом направлении, должны остановиться.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Светофор с зеленой стрелкой и красным светом означает, что'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 22:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Необходимо остановиться перед выездом на нее', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Необходимо уступить дорогу водителям, находящимся на кольцевой развязке или перекрестке с круговым движением', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Имеют преимущественное право проезда, если они прибудут первыми', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Иметь преимущественное право проезда, если есть две полосы движения', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Водители, въезжающие на кольцевую или перекресток с круговым движением:'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 23:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Сигнальные огни', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Другие автомобили на дороге', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Время суток', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Состояние дороги', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'На вашу способность останавливаться влияют:'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 24:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Чтобы остановиться, нужно преодолеть большее расстояние, чем автомобилям.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Требуется меньше времени для перехода на более низкую передачу, чем у автомобилей', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Требуют меньшего радиуса поворота, чем автомобили', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Требуют меньше времени для прохождения подъёма, чем автомобили', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'При совместном движении по дороге с грузовым автомобилем важно помнить, что, как правило, грузовые автомобили:'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 25:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Избегайте резких поворотов и торможений.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Проверьте сцепление шин с дорогой при движении в гору.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Уменьшите расстояние, на которое вы смотрите перед своим автомобилем.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Дороги скользкие после того, как только начинается дождь. Когда дорога скользкая, вам следует:'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 26:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Общий информационный знак автовокзала.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Общий информационный знак для стоянки автофургонов.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий информационный знак для стоянки грузовиков.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий информационный знак для стоянки мобильных домов.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-22.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 27:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Они устраняются, если у вас по одному наружному зеркалу с каждой стороны автомобиля.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Большие грузовики имеют большие слепые зоны, чем большинство легковых автомобилей.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Слепые зоны можно проверить, посмотрев в зеркала заднего вида.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Какое из следующих утверждений о слепых зонах верно?'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 28:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Если другой водитель подает вам сигнал продолжать движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Если школьный автобус не движется и мигают красные огни.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Если школьный автобус находится в движении.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Все вышеперечисленное.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'В какое время вам разрешено обгонять школьный автобус?'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        self.dialog()
            if count == '7':
                async with self:
                    self.COUNT_QUESTIONS = self.COUNT_QUESTIONS + 1
                    if self.COUNT_QUESTIONS == 15:
                        if self.COUNT_OK > 11:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['hand', 'blue', 'blue', 'Получить права', 'javascript:void(0);', '8'],
                            ]
                            self.tDialogText = f'Поздравляем, вы сдали тест. Число верных ответов: {self.COUNT_OK} из {self.COUNT_QUESTIONS}. Вы теперь можете получить права'
                            self.tDialogImage = ''
                            self.tDialogImageHeight = ''
                            self.dialog()
                        else:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Окей', 'javascript:void(0);', '0'],
                            ]
                            self.tDialogText = f'Извините, но вы не сдали тест. Число верных ответов: {self.COUNT_OK} из {self.COUNT_QUESTIONS}. Попробуйте снова'
                            self.tDialogImage = ''
                            self.tDialogImageHeight = ''
                            self.dialog()
                    else:
                        self.tIsActiveTimer = 0
                        self.tDialogIcon = 'message-circle'
                        self.tDialogIconColor = 'blue'
                        tRandomQuestion = random.randint(0, 20)
                        if tRandomQuestion == 0:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота направо.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога поворачивает налево, затем направо.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота налево.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Скользкий, когда мокрый.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-1.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 1:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Предупреждение о том, что впереди знак «Стоп».', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Движение в прямом направлении запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Неправильный путь, нельзя въезжать.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждение о необходимости немедленно остановиться.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-2.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 2:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается тротуар.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Полоса заканчивается впереди.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди строительство дороги.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Дорога впереди закрыта.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-3.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 3:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди знак «Стоп».', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Ограничение скорости снижено, впереди школьная зона.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди школьный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди зона окончания школы.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-4.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 4:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Церковный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Только пешеходное движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-5.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 5:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди четырехсторонний перекресток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди перекресток второстепенных дорог.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди предупреждение о перекрестке, дорога заканчивается, необходимо повернуть направо или налево.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди перекресток Y.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-6.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 6:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Разворот запрещен.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Кривая.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Поверните направо или налево.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение транспорта осуществляется только в направлении стрелки.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Этот дорожный знак означает?'
                            self.tDialogImage = '/images/places/Licensing Center/question-7.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 7:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Въезд запрещен', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Эта дорога или улица заканчивается впереди.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается двустороннее движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Не в ту сторону, развернись.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-8.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 8:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'На улице играть нельзя.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Парковка запрещена.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Обгон запрещен.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение пешеходов запрещено.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-9.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 9:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Только пешеходы, движение транспорта запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждение о посещении школы: вы въезжаете на территорию школы.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждающий знак «Впереди пешеходы».', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-10.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 10:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Справа приближается транспортный поток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Правая полоса заканчивается впереди, держитесь левой стороны.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди разделительная полоса.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-11.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 11:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Полностью остановитесь у знака и уступите дорогу транспортному средству.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, приближаясь к перекрестку.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, при необходимости полностью остановитесь, уступите дорогу движению.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога закрыта, не въезжать.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-12.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 12:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение автотранспортных средств запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходного перехода нет.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-13.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 13:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди съезд.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Низкий клиренс впереди.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога впереди сужается.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди дорога под водой.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-14.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 14:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение транспорта только справа.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение транспорта только левостороннее.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Ваша полоса закончится впереди.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Не проезжайте мимо этого знака, развернитесь.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-15.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 15:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Перекресток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Железнодорожный переезд.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Зона взрывных работ.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Этот знак предупреждает о приближении'
                            self.tDialogImage = '/images/places/Licensing Center/question-16.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 16:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Охота запрещена.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Территория заповедника.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди переходят дорогу олени.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Территория государственного парка.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-17.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 17:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди обратный поворот.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди одностороннее движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди начинается разделенное шоссе.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается разделенная автомагистраль.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-18.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 18:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение по центральной полосе может идти прямо или поворачивать налево.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Поворот направо возможен только с центральной полосы.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Центральная полоса сливается в одну полосу', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение по центральной полосе должно поворачивать налево.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Эта разметка на тротуаре сообщает вам, что на перекрестке впереди'
                            self.tDialogImage = '/images/places/Licensing Center/question-19.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 19:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Общий знак обслуживания больницы.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий знак для кабинета врача.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий знак обслуживания аптеки.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Общий знак для парковки.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-20.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 20:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, в идеальных условиях максимальная рекомендуемая скорость составляет 25 миль в час.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час в идеальных условиях.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, максимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак ограничения скорости на повороте?'
                            self.tDialogImage = '/images/places/Licensing Center/question-21.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 21:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Вы можете ехать только прямо.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Двигаться можно только в направлении зеленой стрелки.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Вам нужно дождаться зеленого света.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Транспортные средства, движущиеся в любом направлении, должны остановиться.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Светофор с зеленой стрелкой и красным светом означает, что'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 22:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Необходимо остановиться перед выездом на нее', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Необходимо уступить дорогу водителям, находящимся на кольцевой развязке или перекрестке с круговым движением', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Имеют преимущественное право проезда, если они прибудут первыми', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Иметь преимущественное право проезда, если есть две полосы движения', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Водители, въезжающие на кольцевую или перекресток с круговым движением:'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 23:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Сигнальные огни', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Другие автомобили на дороге', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Время суток', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Состояние дороги', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'На вашу способность останавливаться влияют:'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 24:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Чтобы остановиться, нужно преодолеть большее расстояние, чем автомобилям.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Требуется меньше времени для перехода на более низкую передачу, чем у автомобилей', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Требуют меньшего радиуса поворота, чем автомобили', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Требуют меньше времени для прохождения подъёма, чем автомобили', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'При совместном движении по дороге с грузовым автомобилем важно помнить, что, как правило, грузовые автомобили:'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 25:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Избегайте резких поворотов и торможений.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Проверьте сцепление шин с дорогой при движении в гору.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Уменьшите расстояние, на которое вы смотрите перед своим автомобилем.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Дороги скользкие после того, как только начинается дождь. Когда дорога скользкая, вам следует:'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 26:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Общий информационный знак автовокзала.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Общий информационный знак для стоянки автофургонов.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий информационный знак для стоянки грузовиков.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий информационный знак для стоянки мобильных домов.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-22.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 27:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Они устраняются, если у вас по одному наружному зеркалу с каждой стороны автомобиля.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Большие грузовики имеют большие слепые зоны, чем большинство легковых автомобилей.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Слепые зоны можно проверить, посмотрев в зеркала заднего вида.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Какое из следующих утверждений о слепых зонах верно?'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 28:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Если другой водитель подает вам сигнал продолжать движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Если школьный автобус не движется и мигают красные огни.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Если школьный автобус находится в движении.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Все вышеперечисленное.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'В какое время вам разрешено обгонять школьный автобус?'
                            self.tDialogImage = '/images/places/Licensing Center/question-0.png'
                            self.tDialogImageHeight = '232px'
                        self.dialog()
            if count == '8':
                async with self:
                    tLicenses = ast.literal_eval(str(self.USER[27]))
                    tLicenses[1] = 1
                    await database.setUserID(self.USER[0], 'licences', f"\"{tLicenses}\"")
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    self.tDialogButtons = [
                        ['message-circle', 'blue', 'blue', 'Спасибо, до свидания', 'javascript:void(0);', '0'],
                    ]
                    self.tDialogText = 'Спасибо, что обратились в центр лицензирования. Ждем вас снова, если вдруг вам необходимо будет получить новые лицензии'
                    self.dialog()
                    return rx.toast.info("Вы получили права на автомобили", position='top-right')





















    @rx.event(background=True)
    async def controlState(self, count):
        if self.Stage == '1':
            if count == '0':
                async with self:
                    return rx.redirect('/places/licensing-center')
            if count == '1':
                async with self:
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    if self.isPassport == '1':
                        self.tDialogButtons = [
                            ['hand', 'blue', 'blue', 'Передать паспорт', 'javascript:void(0);', '2'],
                            ['message-circle', 'blue', 'blue', 'Извините, я ошибся', 'javascript:void(0);', '0'],
                        ]
                    if self.isPassport == '0':
                        self.tDialogButtons = [
                            ['x', 'tomato', 'tomato', 'У вас нет паспорта данного штата', 'javascript:void(0);', '1'],
                            ['message-circle', 'blue', 'blue', 'Извините, я ошибся', 'javascript:void(0);', '0'],
                        ]
                    self.tDialogText = 'Хорошо, для того, чтобы получить права на управление автомобилями необходим паспорт, пожалуйста дайте его.'
                    self.tDialogImage = ''
                    self.tDialogImageHeight = ''
                    self.dialog()
            if count == '2':
                async with self:
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    self.tDialogButtons = [
                    ]
                    self.tDialogText = 'Спасибо, сейчас зарегистрирую вас как кандидата на получение прав'
                    self.dialog()
                    self.tIsActiveTimer = 1
                    self.tActiveDialogKey = self.tActiveDialog
                await asyncio.sleep(10)
                async with self:
                    if self.tIsActiveTimer == 1 and self.tActiveDialogKey == self.tActiveDialog:
                        self.tIsActiveTimer = 0
                        tLicenses = ast.literal_eval(str(self.USER[27]))
                        if tLicenses[0] == 0:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['banknote', 'green', 'green', 'Заплатить 300 долларов', 'javascript:void(0);', '3'],
                                ['message-circle', 'blue', 'blue', 'Простите, но мне надо уйти', 'javascript:void(0);', '0'],
                            ]
                            self.tDialogText = 'Итак, все отлично. Получение прав происходит в один этап: вам необходимо ответить на 10 вопросов. Если вы на них отвечаете верно — получаете права. Будьте внимательны, что вы сейчас оплачиваете попытку прохождения. Каждая новая попытка будет сопровождаться новой оплатой. Стоимость прохождения теста — 300 долларов.'
                            self.dialog()
                        else:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Простите, ошибся', 'javascript:void(0);', '0'],
                            ]
                            self.tDialogText = 'Извините, но у вас уже есть лицензия на управление автомобилями. Мы не можем для вас предложить пройти тест'
                            self.dialog()
                    else:
                        self.tIsActiveTimer = 0
            if count == '3':
                async with self:
                    self.USER = await database.getUserHash(f"'{self.HASH}'")
                    if self.USER[6] >= 300:
                        newBalance = self.USER[6] - 300
                        await database.setUserID(self.USER[0], 'dollars', f"'{newBalance}'")
                        self.tDialogIcon = 'message-circle'
                        self.tDialogIconColor = 'blue'
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Хорошо', 'javascript:void(0);', '4'],
                        ]
                        self.tDialogText = 'Если вы готовы, то пройдите в учебный класс для сдачи теста'
                        self.dialog()
                        return rx.toast.success("Вы заплатили 300 долларов", position='top-right')
                    if self.USER[6] < 300:
                        return rx.toast.error("Вам нехватает денег", position='top-right')
            if count == '4':
                async with self:
                    self.COUNT_QUESTIONS = 0
                    self.COUNT_OK = 0
                    self.tIsActiveTimer = 0
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    self.tDialogButtons = [
                        ['hand', 'blue', 'blue', 'Начать выполнять тест', 'javascript:void(0);', '5'],
                    ]
                    self.tDialogText = 'Итак, сейчас у вас будет 10 вопросов, вдумчиво читайте вопрос и правильно отвечайте на них.'
                    self.dialog()
            if count == '5':
                async with self:
                    self.tIsActiveTimer = 0
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    tRandomQuestion = random.randint(0, 20)
                    if tRandomQuestion == 0:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота направо.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Дорога поворачивает налево, затем направо.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота налево.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Скользкий, когда мокрый.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот предупреждающий знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-1.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 1:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Предупреждение о том, что впереди знак «Стоп».', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Движение в прямом направлении запрещено.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Неправильный путь, нельзя въезжать.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Предупреждение о необходимости немедленно остановиться.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-2.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 2:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди заканчивается тротуар.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Полоса заканчивается впереди.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди строительство дороги.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Дорога впереди закрыта.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот предупреждающий знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-3.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 3:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди знак «Стоп».', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Ограничение скорости снижено, впереди школьная зона.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Впереди школьный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди зона окончания школы.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот предупреждающий знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-4.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 4:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Церковный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Только пешеходное движение.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-5.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 5:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди четырехсторонний перекресток.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди перекресток второстепенных дорог.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди предупреждение о перекрестке, дорога заканчивается, необходимо повернуть направо или налево.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Впереди перекресток Y.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-6.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 6:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Разворот запрещен.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Кривая.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Поверните направо или налево.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Движение транспорта осуществляется только в направлении стрелки.', 'javascript:void(0);', '6'],
                        ]
                        self.tDialogText = 'Этот дорожный знак означает?'
                        self.tDialogImage = '/images/places/Licensing Center/question-7.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 7:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Въезд запрещен', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Эта дорога или улица заканчивается впереди.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Впереди заканчивается двустороннее движение.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Не в ту сторону, развернись.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот предупреждающий знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-8.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 8:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'На улице играть нельзя.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Парковка запрещена.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Обгон запрещен.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Движение пешеходов запрещено.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-9.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 9:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Только пешеходы, движение транспорта запрещено.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Предупреждение о посещении школы: вы въезжаете на территорию школы.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Впереди пешеходный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Предупреждающий знак «Впереди пешеходы».', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-10.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 10:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Справа приближается транспортный поток.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Правая полоса заканчивается впереди, держитесь левой стороны.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Впереди разделительная полоса.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-11.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 11:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Полностью остановитесь у знака и уступите дорогу транспортному средству.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Снизьте скорость, приближаясь к перекрестку.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Снизьте скорость, при необходимости полностью остановитесь, уступите дорогу движению.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Дорога закрыта, не въезжать.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-12.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 12:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Движение автотранспортных средств запрещено.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Пешеходного перехода нет.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-13.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 13:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди съезд.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Низкий клиренс впереди.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Дорога впереди сужается.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди дорога под водой.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот предупреждающий знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-14.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 14:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Движение транспорта только справа.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Движение транспорта только левостороннее.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Ваша полоса закончится впереди.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Не проезжайте мимо этого знака, развернитесь.', 'javascript:void(0);', '6'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-15.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 15:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Перекресток.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Железнодорожный переезд.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Зона взрывных работ.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Этот знак предупреждает о приближении'
                        self.tDialogImage = '/images/places/Licensing Center/question-16.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 16:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Охота запрещена.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Территория заповедника.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди переходят дорогу олени.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Территория государственного парка.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-17.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 17:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Впереди обратный поворот.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди одностороннее движение.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди начинается разделенное шоссе.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Впереди заканчивается разделенная автомагистраль.', 'javascript:void(0);', '6'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-18.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 18:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Движение по центральной полосе может идти прямо или поворачивать налево.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Поворот направо возможен только с центральной полосы.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Центральная полоса сливается в одну полосу', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Движение по центральной полосе должно поворачивать налево.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Эта разметка на тротуаре сообщает вам, что на перекрестке впереди'
                        self.tDialogImage = '/images/places/Licensing Center/question-19.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 19:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Общий знак обслуживания больницы.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Общий знак для кабинета врача.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Общий знак обслуживания аптеки.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Общий знак для парковки.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак?'
                        self.tDialogImage = '/images/places/Licensing Center/question-20.png'
                        self.tDialogImageHeight = '232px'
                    if tRandomQuestion == 20:
                        self.tDialogButtons = [
                            ['message-circle', 'blue', 'blue', 'Снизьте скорость, в идеальных условиях максимальная рекомендуемая скорость составляет 25 миль в час.', 'javascript:void(0);', '6'],
                            ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час в идеальных условиях.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                            ['message-circle', 'blue', 'blue', 'Снизьте скорость, максимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                        ]
                        self.tDialogText = 'Что означает этот знак ограничения скорости на повороте?'
                        self.tDialogImage = '/images/places/Licensing Center/question-21.png'
                        self.tDialogImageHeight = '232px'
                    self.dialog()
            if count == '6':
                async with self:
                    self.COUNT_QUESTIONS = self.COUNT_QUESTIONS + 1
                    self.COUNT_OK = self.COUNT_OK + 1
                    if self.COUNT_QUESTIONS == 10:
                        if self.COUNT_OK > 7:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['hand', 'blue', 'blue', 'Получить права', 'javascript:void(0);', '8'],
                            ]
                            self.tDialogText = f'Поздравляем, вы сдали тест. Число верных ответов: {self.COUNT_OK} из {self.COUNT_QUESTIONS}. Вы теперь можете получить права'
                            self.tDialogImage = ''
                            self.tDialogImageHeight = ''
                            self.dialog()
                        else:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Окей', 'javascript:void(0);', '0'],
                            ]
                            self.tDialogText = f'Извините, но вы не сдали тест. Число верных ответов: {self.COUNT_OK} из {self.COUNT_QUESTIONS}. Попробуйте снова'
                            self.tDialogImage = ''
                            self.tDialogImageHeight = ''
                            self.dialog()
                    else:
                        self.tIsActiveTimer = 0
                        self.tDialogIcon = 'message-circle'
                        self.tDialogIconColor = 'blue'
                        tRandomQuestion = random.randint(0, 20)
                        if tRandomQuestion == 0:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота направо.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога поворачивает налево, затем направо.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота налево.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Скользкий, когда мокрый.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-1.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 1:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Предупреждение о том, что впереди знак «Стоп».', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Движение в прямом направлении запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Неправильный путь, нельзя въезжать.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждение о необходимости немедленно остановиться.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-2.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 2:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается тротуар.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Полоса заканчивается впереди.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди строительство дороги.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Дорога впереди закрыта.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-3.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 3:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди знак «Стоп».', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Ограничение скорости снижено, впереди школьная зона.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди школьный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди зона окончания школы.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-4.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 4:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Церковный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Только пешеходное движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-5.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 5:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди четырехсторонний перекресток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди перекресток второстепенных дорог.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди предупреждение о перекрестке, дорога заканчивается, необходимо повернуть направо или налево.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди перекресток Y.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-6.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 6:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Разворот запрещен.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Кривая.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Поверните направо или налево.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение транспорта осуществляется только в направлении стрелки.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Этот дорожный знак означает?'
                            self.tDialogImage = '/images/places/Licensing Center/question-7.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 7:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Въезд запрещен', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Эта дорога или улица заканчивается впереди.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается двустороннее движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Не в ту сторону, развернись.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-8.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 8:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'На улице играть нельзя.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Парковка запрещена.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Обгон запрещен.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение пешеходов запрещено.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-9.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 9:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Только пешеходы, движение транспорта запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждение о посещении школы: вы въезжаете на территорию школы.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждающий знак «Впереди пешеходы».', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-10.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 10:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Справа приближается транспортный поток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Правая полоса заканчивается впереди, держитесь левой стороны.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди разделительная полоса.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-11.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 11:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Полностью остановитесь у знака и уступите дорогу транспортному средству.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, приближаясь к перекрестку.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, при необходимости полностью остановитесь, уступите дорогу движению.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога закрыта, не въезжать.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-12.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 12:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение автотранспортных средств запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходного перехода нет.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-13.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 13:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди съезд.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Низкий клиренс впереди.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога впереди сужается.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди дорога под водой.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-14.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 14:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение транспорта только справа.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение транспорта только левостороннее.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Ваша полоса закончится впереди.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Не проезжайте мимо этого знака, развернитесь.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-15.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 15:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Перекресток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Железнодорожный переезд.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Зона взрывных работ.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Этот знак предупреждает о приближении'
                            self.tDialogImage = '/images/places/Licensing Center/question-16.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 16:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Охота запрещена.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Территория заповедника.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди переходят дорогу олени.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Территория государственного парка.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-17.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 17:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди обратный поворот.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди одностороннее движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди начинается разделенное шоссе.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается разделенная автомагистраль.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-18.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 18:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение по центральной полосе может идти прямо или поворачивать налево.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Поворот направо возможен только с центральной полосы.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Центральная полоса сливается в одну полосу', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение по центральной полосе должно поворачивать налево.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Эта разметка на тротуаре сообщает вам, что на перекрестке впереди'
                            self.tDialogImage = '/images/places/Licensing Center/question-19.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 19:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Общий знак обслуживания больницы.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий знак для кабинета врача.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий знак обслуживания аптеки.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Общий знак для парковки.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-20.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 20:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, в идеальных условиях максимальная рекомендуемая скорость составляет 25 миль в час.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час в идеальных условиях.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, максимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак ограничения скорости на повороте?'
                            self.tDialogImage = '/images/places/Licensing Center/question-21.png'
                            self.tDialogImageHeight = '232px'
                        self.dialog()
            if count == '7':
                async with self:
                    self.COUNT_QUESTIONS = self.COUNT_QUESTIONS + 1
                    if self.COUNT_QUESTIONS == 10:
                        if self.COUNT_OK > 7:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['hand', 'blue', 'blue', 'Получить права', 'javascript:void(0);', '8'],
                            ]
                            self.tDialogText = f'Поздравляем, вы сдали тест. Число верных ответов: {self.COUNT_OK} из {self.COUNT_QUESTIONS}. Вы теперь можете получить права'
                            self.tDialogImage = ''
                            self.tDialogImageHeight = ''
                            self.dialog()
                        else:
                            self.tDialogIcon = 'message-circle'
                            self.tDialogIconColor = 'blue'
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Окей', 'javascript:void(0);', '0'],
                            ]
                            self.tDialogText = f'Извините, но вы не сдали тест. Число верных ответов: {self.COUNT_OK} из {self.COUNT_QUESTIONS}. Попробуйте снова'
                            self.tDialogImage = ''
                            self.tDialogImageHeight = ''
                            self.dialog()
                    else:
                        self.tIsActiveTimer = 0
                        self.tDialogIcon = 'message-circle'
                        self.tDialogIconColor = 'blue'
                        tRandomQuestion = random.randint(0, 20)
                        if tRandomQuestion == 0:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота направо.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога поворачивает налево, затем направо.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога, начинается с поворота налево.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Скользкий, когда мокрый.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-1.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 1:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Предупреждение о том, что впереди знак «Стоп».', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Движение в прямом направлении запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Неправильный путь, нельзя въезжать.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждение о необходимости немедленно остановиться.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-2.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 2:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается тротуар.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Полоса заканчивается впереди.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди строительство дороги.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Дорога впереди закрыта.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-3.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 3:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди знак «Стоп».', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Ограничение скорости снижено, впереди школьная зона.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди школьный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди зона окончания школы.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-4.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 4:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Церковный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Только пешеходное движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-5.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 5:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди четырехсторонний перекресток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди перекресток второстепенных дорог.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди предупреждение о перекрестке, дорога заканчивается, необходимо повернуть направо или налево.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди перекресток Y.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-6.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 6:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Разворот запрещен.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Кривая.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Поверните направо или налево.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение транспорта осуществляется только в направлении стрелки.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Этот дорожный знак означает?'
                            self.tDialogImage = '/images/places/Licensing Center/question-7.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 7:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Въезд запрещен', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Эта дорога или улица заканчивается впереди.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается двустороннее движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Не в ту сторону, развернись.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-8.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 8:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'На улице играть нельзя.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Парковка запрещена.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Обгон запрещен.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение пешеходов запрещено.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-9.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 9:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Только пешеходы, движение транспорта запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждение о посещении школы: вы въезжаете на территорию школы.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Предупреждающий знак «Впереди пешеходы».', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-10.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 10:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Справа приближается транспортный поток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди извилистая дорога.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Правая полоса заканчивается впереди, держитесь левой стороны.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Впереди разделительная полоса.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-11.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 11:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Полностью остановитесь у знака и уступите дорогу транспортному средству.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, приближаясь к перекрестку.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, при необходимости полностью остановитесь, уступите дорогу движению.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога закрыта, не въезжать.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-12.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 12:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение автотранспортных средств запрещено.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходного перехода нет.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Школьный переход.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-13.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 13:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди съезд.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Низкий клиренс впереди.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Дорога впереди сужается.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди дорога под водой.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот предупреждающий знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-14.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 14:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение транспорта только справа.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение транспорта только левостороннее.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Ваша полоса закончится впереди.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Не проезжайте мимо этого знака, развернитесь.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-15.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 15:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Перекресток.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Пешеходный переход.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Железнодорожный переезд.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Зона взрывных работ.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Этот знак предупреждает о приближении'
                            self.tDialogImage = '/images/places/Licensing Center/question-16.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 16:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Охота запрещена.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Территория заповедника.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди переходят дорогу олени.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Территория государственного парка.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-17.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 17:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Впереди обратный поворот.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди одностороннее движение.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди начинается разделенное шоссе.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Впереди заканчивается разделенная автомагистраль.', 'javascript:void(0);', '6'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-18.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 18:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Движение по центральной полосе может идти прямо или поворачивать налево.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Поворот направо возможен только с центральной полосы.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Центральная полоса сливается в одну полосу', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Движение по центральной полосе должно поворачивать налево.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Эта разметка на тротуаре сообщает вам, что на перекрестке впереди'
                            self.tDialogImage = '/images/places/Licensing Center/question-19.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 19:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Общий знак обслуживания больницы.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий знак для кабинета врача.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Общий знак обслуживания аптеки.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Общий знак для парковки.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак?'
                            self.tDialogImage = '/images/places/Licensing Center/question-20.png'
                            self.tDialogImageHeight = '232px'
                        if tRandomQuestion == 20:
                            self.tDialogButtons = [
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, в идеальных условиях максимальная рекомендуемая скорость составляет 25 миль в час.', 'javascript:void(0);', '6'],
                                ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час в идеальных условиях.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Минимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                                ['message-circle', 'blue', 'blue', 'Снизьте скорость, максимальная рекомендуемая скорость составляет 25 миль в час при любых условиях.', 'javascript:void(0);', '7'],
                            ]
                            self.tDialogText = 'Что означает этот знак ограничения скорости на повороте?'
                            self.tDialogImage = '/images/places/Licensing Center/question-21.png'
                            self.tDialogImageHeight = '232px'
                        self.dialog()
            if count == '8':
                async with self:
                    tLicenses = ast.literal_eval(str(self.USER[27]))
                    tLicenses[0] = 1
                    await database.setUserID(self.USER[0], 'licences', f"\"{tLicenses}\"")
                    self.tDialogIcon = 'message-circle'
                    self.tDialogIconColor = 'blue'
                    self.tDialogButtons = [
                        ['message-circle', 'blue', 'blue', 'Спасибо, до свидания', 'javascript:void(0);', '0'],
                    ]
                    self.tDialogText = 'Спасибо, что обратились в центр лицензирования. Ждем вас снова, если вдруг вам необходимо будет получить новые лицензии'
                    self.dialog()
                    return rx.toast.info("Вы получили права на автомобили", position='top-right')


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