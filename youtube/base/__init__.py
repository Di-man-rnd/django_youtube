import os
import urllib

from lxml import html
from teach.settings import *
from youtube.models import Bloger


class Log(object):
    def info(self, msg):
        a = '============  INFO ==========\n'
        text = a + msg
        self.wr(text)

    def wr(self, msg):
        loger = open(LOG_PATH, 'a')
        loger.write('{}'.format(msg) + '\n')
        loger.close()


def grab():
    # init name img
    count = 0
    # read rss html
    htm = open(BASE_DIR + '/youtube/base/rss.html').read()

    # parse rss
    tree = html.fromstring(htm)
    tag_a = tree.xpath('//a')
    tag_img = tree.xpath('//img')

    # название каталога /bloger/1/img.jpg
    folder = 1
    # бежим по тегам
    for a in tag_a:
        # for img in tag_img:

        # т.к. много элементов в ленте много картинок, чтоб не грузить все в один каталог
        # делим по 50 картинок на каталог
        if count % 50 == 0 and count != 0:
            folder += 1

        # создаем папку 1 в /bloger/
        try:
            os.makedirs(MEDIA_ROOT + '/bloger/' + str(folder) + '/', mode=0o777)
        except FileExistsError as ex:
            pass

        #  получаем урл для загрузки картинки
        img_from = tag_img[count].get('data-thumb', tag_img[count].get('src'))
        img_to = 'bloger/' + str(folder) + '/' + str(count) + '.jpg'

        try:
            # скачаиваем картинку на диск
            urllib.request.urlretrieve(img_from, MEDIA_ROOT + '/' + img_to)
        except Exception as ex:
            img_to = 'bloger/tmp.jpg'

        cur_item = {
            'title': a.attrib['title'],
            'href': 'https://www.youtube.com' + a.attrib['href'],
            'img': img_to
        }

        # увеличиваем название картинки на 1, т.к в rss ленте они все называются photo
        count += 1
        print(count, cur_item)

        # создаем элемент в БД
        elem = Bloger(
            name=cur_item['title'],
            url=cur_item['href'],
            img=cur_item['img'],
        )
        elem.save()


# ===============   Change Category =============
'''
django.jQuery('img').click(function(){
  tt= django.jQuery(this).parent().parent()
  id =   django.jQuery(tt).find('.action-checkbox input').attr('value')
  console.info(id)
  django.jQuery.get("/bloger/setcat/?pk="+ id + '&cat=5')

})
'''
