import os
import redis
import urllib

from lxml import html

from youtube.models import Bloger


def grab():
    # init redis
    session = redis.StrictRedis(host='localhost', port=6379, db=0)
    # read rss html
    htm = open('/home/mint/store/site/python/project/teach/youtube/base/rss.html').read()

    # parse rss
    tree = html.fromstring(htm)
    tag_a = tree.xpath('//a')
    tag_img = tree.xpath('//img')

    # проверяем счетчик для названий картинок 1.jpg, 2.jpg, 3.jpg ...
    if session.get('count') is None or int(session.get('count')) > 0:
        session.set('count', 0)

    # название каталога /bloger/1/img.jpg
    folder = 1
    # бежим по тегам
    for a in tag_a:
        # for img in tag_img:

        # т.к. много элементов в ленте много картинок, чтоб не грузить все в один каталог
        # делим по 50 картинок на каталог
        if int(session.get('count')) % 50 == 0 and int(session.get('count')) != 0:
            folder += 1

        # создаем папку 1 в /bloger/
        try:
            os.makedirs('./files/media/bloger/' + str(folder) + '/', mode=0o777)
        except FileExistsError as e:
            pass

        # скачаиваем картинку на диск
        urllib.request.urlretrieve(
            tag_img[int(session.get('count'))].attrib['src'],
            './files/media/bloger/' + str(folder) + '/' + str(session.get('count')) + '.jpg'
        )

        cur_item = {
            'title': a.attrib['title'],
            'href': 'https://www.youtube.com' + a.attrib['href'],
            'img': 'bloger/' + str(folder) + '/' + str(session.get('count')) + '.jpg'
        }

        # увеличиваем название картинки на 1, т.к в rss ленте они все называются photo
        count = int(session.get('count')) +1
        session.set('count', count)

        print(cur_item)

        # создаем элемент в БД
        elem = Bloger(
            name=cur_item['title'],
            url=cur_item['href'],
            img=cur_item['img'],
        )
        elem.save()

        if int(session.get('count')) == 5:
            exit()
