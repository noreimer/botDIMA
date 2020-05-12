import vk_api
import time
import datetime
import wikipedia
from vk_messages import MessagesAPI
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
d = 0
r = 0
TOKEN = "2c921302545cd3f3e6678f6acea25f1e0be591c2291072f2b25591a482719acd4521486f06543107c1b90"
def main():
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
                    elif 'синагога' in event.obj.message['text'].lower():
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Что такое синагога??",
                                         random_id=random.randint(0, 2 ** 64))
                    elif 'какой день недели' in event.obj.message['text'].lower():
                        r = 1
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Введите дату в формате 2000.01.29",
                                         random_id=random.randint(0, 2 ** 64))
                    elif 'википедия' in event.obj.message['text'].lower():
                        d = 1
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Введите ваш запрос",
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

                    elif 'время' in event.obj.message['text'].lower() or 'число' in event.obj.message['text'].lower() \
                        or 'дата' in event.obj.message['text'].lower():
                        f = time.ctime()
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message= f,
                                         random_id=random.randint(0, 2 ** 64))
                    else:
                        vk.messages.send(user_id=event.obj.message['from_id'],
                                         message="Я могу сказать дату и время, ответь мне "
                                                 "сообщение содержащее эти слова. Я могу найти информацию"
                                                 " в википедии напиши мне 'Википедия'. ",
                                         random_id=random.randint(0, 2 ** 64))
                if event.type == VkBotEventType.MESSAGE_TYPING_STATE:
                    print(f'Печатает {event.obj.from_id} для {event.obj.to_id}')


if __name__ == '__main__':
    main()