import vk_api
import time
import datetime
import wikipedia
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
d = 0
s = 0
r = 0
e = 0
anecdot = ["Когда у русского молчания истекает срок годности - оно взрывается.",
"Детство круто изменилось. Раньше у соседей яблоки воровали, а теперь Wi-Fi.",
"Из меня веревки вить не получится! Только колючую проволоку...",
"На всякий случай одеваю на кота корону, чтобы вирус подумал, что он уже инфицирован.",
"Каждый гусеничный трактор мечтает стать танком.",
"Корпоратив - это мероприятие, где начальники ощущают себя на вечеринке, а подчиненные - на утреннике.",
"Швеция. Здесь отменен традиционный праздник Вальпургиева ночь. Власти обратились к ведьмам с призывом до "
"окончания эпидемии не покидать своих метел.",
"Человека без бровей очень сложно удивить.",
"Сегодня у нашего кота был праздник - гонял по квартире попугая. У попугая, соответственно, наоборот.",
"Удивительно, но пингвины - это долго сидевшие в карантине ласточки.",
        "Борщ и у соседки можно поесть, а вот наорать что пересолила, тут жена нужна.",
"Запрет хождения в лес связан с опасением спонтанного формирования партизанских отрядов.",
"Заплати программисту чеканным биткойном...",
"Как только в России корона, так все люди снова крепостные.",
        "В результате наводнения в Хабаровске территория завода Ролтон увеличилась в два раза.",
"Ей нравятся только непьющие, а она нравится только пьяным.",
"Тебе страшно и одиноко? Карантин сводит с ума? Нечем заняться? Запей селедку молоком.",
"Теперь на фоне ситуации в мире передачи Рен ТВ смотрятся как обычные новости.",
"Иногда человек бывает счастливым только потому, что у него плохая память.",
"Утро понедельника это время, когда ты завидуешь котам.",
"В Греции прогулки разрешены только для выгула домашних питомцев. По местному "
"ТВ показывали людей выгуливавших золотых рыбок.",
"Долой 1 сентября, да здравствует 32 августа!",
"На уссурийских тигров запрещено охотиться. Но рыбачить-то на них никто не запрещал!",
"Криштиану Рональдо был госпитализирован с травмой прически.",
"Купила туфли. В них очень удобно. Сидеть.",
"Кабачковая икра - это миллионы не родившихся кабачат!",
"Когда соседи шумят, Николай Валуев стучит по батарее холодильником.",
"Можно ли назвать археологические открытия - отрытия?",
"С учетом динамики цен на нефть, пойду-ка ночью солью с авто у соседа бензин, деньги потом отдаст, так уж и быть.",
"Симулирую боязнь пауков, чтобы казаться немного женственнее...",
"Если Windows - это окна, то можно ли панель задач называть подоконником?",
"Слой пригоревшей картошки - это прекрасное антипригарное покрытие для макарон.",
"Стало известно зачем нужно носить с собой паспорт: тот, кто родился в год собаки - может гулять в парке сам.",
"А вы уже решили на каком сайте проведете свой отпуск?",
"Правильный блинчик с начинкой - это шаурма!",
"Пошла как-то Аленушка в Москву-реку топиться. Заодно и отравилась.",
"Дядя Вася, крановщик с тридцатилетним стажем, за десять минут обчистил автомат с мягкими игрушками.",
"Я человек простой: есть проблема - прокрастинирую.",
"Если самоизоляция не поможет, введут самоликвидацию.",
"Эпическую музыку пишут для того, чтобы было что наложить на видео, когда снимаешь "
"с квадрокоптера ролик про свое село.",
"Отошел от дома на 300 метров. Адреналин зашкаливает!"]
TOKEN = "2c921302545cd3f3e6678f6acea25f1e0be591c2291072f2b25591a482719acd4521486f06543107c1b90"


def main():
    global s, d, r, e
    vk_session = vk_api.VkApi(
        token=TOKEN)

    id_сообщества = 194627198
    longpoll = VkBotLongPoll(vk_session, id_сообщества)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            for event in longpoll.listen():

                if event.type == VkBotEventType.MESSAGE_NEW:
                    print('Новое сообщение:')
                    print('Для меня от:', event.obj.message['from_id'])
                    print('Текст:', event.obj.message['text'])
                    vk = vk_session.get_api()
                    response = vk.users.get(user_id=event.obj.message['from_id'])
                    name = response[0]['first_name']
                    if 'прив' in event.obj.message['text'].lower() or 'хай' in event.obj.message['text'].lower():
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=f"Привет, {name})",
                                         random_id=random.randint(0, 2 ** 64))
                    elif 'пока' in event.obj.message['text'].lower() or 'покеда' in event.obj.message['text'].lower():
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=f"Пока, {name})",
                                         random_id=random.randint(0, 2 ** 64))
                    elif 'как дела' in event.obj.message['text'].lower():
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Хорошо, а у тебя?)",
                                         random_id=random.randint(0, 2 ** 64))
                    elif 'как ты' in event.obj.message['text'].lower():
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Хорошо, а ты?)",
                                         random_id=random.randint(0, 2 ** 64))
                    elif 'какой день недели' in event.obj.message['text'].lower():
                        r = 1
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Введите дату в формате 2000.01.29",
                                         random_id=random.randint(0, 2 ** 64))
                    elif 'сколько дней прошло' in event.obj.message['text'].lower():
                        s = 1
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Введите дату в формате 2000.01.29",
                                         random_id=random.randint(0, 2 ** 64))
                    elif 'википедия' in event.obj.message['text'].lower():
                        d = 1
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Введите ваш запрос",
                                         random_id=random.randint(0, 2 ** 64))
                    elif 'анекдот' in event.obj.message['text'].lower() or 'шут' in event.obj.message['text'].lower():
                        g = random.randint(0, len(anecdot))
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=anecdot[g],
                                         random_id=random.randint(0, 2 ** 64))
                    elif 'время' in event.obj.message['text'].lower() or 'число' in event.obj.message['text'].lower() \
                        or 'дата' in event.obj.message['text'].lower():
                        f = time.ctime()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message= f,
                                         random_id=random.randint(0, 2 ** 64))
                    elif event.obj.message['text'] == '5':
                        d = 1
                        p = time.strftime("%Y.%m.%d", time.localtime())
                        p = p.split('.')
                        p[0] = int(p[0])
                        p[1] = int(p[1])
                        p[2] = int(p[2])
                        io = datetime.date(p[0], p[1], p[2])
                        x = io.toordinal()
                        ioi = x - y
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=ioi,
                                         random_id=random.randint(0, 2 ** 64))
                    elif s == 1:
                        p = event.obj.message['text'].split('.')
                        p[0] = int(p[0])
                        p[1] = int(p[1])
                        p[2] = int(p[2])
                        io = datetime.date(p[0], p[1], p[2])
                        y = io.toordinal()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=f'{y} дней прошло, если считать с 01/01/01, если ты хочешь узнать '
                                                 f'сколько дней прошло с той даты до сегодняшнего дня нажми 5',
                                         random_id=random.randint(0, 2 ** 64))
                    elif r == 1:
                        p = event.obj.message['text'].split('.')
                        p[0] = int(p[0])
                        p[1] = int(p[1])
                        p[2] = int(p[2])
                        io = datetime.date(p[0], p[1], p[2])
                        y = io.weekday()
                        if y == 0:
                            y = 'Понедельник'
                        elif y == 1:
                            y = 'Вторник'
                        elif y == 2:
                            y = 'Среда'
                        elif y == 3:
                            y = 'Четверг'
                        elif y == 4:
                            y = 'Пятница'
                        elif y == 5:
                            y = 'Суббота'
                        elif y == 6:
                            y = 'Воскресенье'
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message=y,
                                         random_id=random.randint(0, 2 ** 64))
                    elif d == 1:
                        e =  wikipedia.search(event.obj.message['text'].lower())
                        if e:
                            inf = wikipedia.page(e[0]).content.encode('UTF8')
                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message=inf,
                                             random_id=random.randint(0, 2 ** 64))
                        else:
                            vk.messages.send(user_id=event.obj.message['from_id'],
                                             message="Запрос не найден",
                                             random_id=random.randint(0, 2 ** 64))
                    else:
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Я могу сказать дату и время, ответь мне. \nЯ могу найти информацию"
                                                 " в википедии напиши мне 'Википедия'. \n"
                                                 "Могу считать количество дней c начала эры и с введенной даты до "
                                                 "сегодняшнего дня, и рассказывать анекдоты. Ответь мне "
                                                 "сообщением содержащее ключевые слова вашего запроса",
                                         random_id=random.randint(0, 2 ** 64))
                if event.type == VkBotEventType.MESSAGE_TYPING_STATE:
                    print(f'Печатает {event.obj.from_id} для {event.obj.to_id}')


if __name__ == '__main__':
    main()