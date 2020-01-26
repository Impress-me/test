# -*- coding: utf-8 -*-
import requests
import threading
import parsel


def getinfo():
    response = requests.get('https://www.bilibili.com/ranking')
    sel = parsel.Selector(response.text)
    # print(sel.css("a.mnav::text").getall())
    lis = sel.css('li.rank-item')
    for li in lis:
        filetmp = li.css('a.title::text').getall()[0] + ',' + li.css('span.data-box::text').getall()[0] + ',' + \
                  li.css('span.data-box::text').getall()[1] + ',' + li.css('span.data-box::text').getall()[2] + '\n'
        print(filetmp)


def getmovie(num):
    url = 'https://www.mcmod.cn/class/category/1-%s.html' % num
    print(url)
    response = requests.get(url)
    sel = parsel.Selector(response.text)
    # print(sel.getall())
    divs = sel.css('div.name.t')
    # print(divs)
    # print(sel.extract())
    for div in divs:
        ftmp = div.css('a::text').extract()
        print(ftmp)
        # print(div.css('div.num::attr(title)').extract() + div.css('div.push::attr(title)').extract() + div.css('div.like::attr(title)').extract())


if __name__ == "__main__":
    t1 = threading.Thread(target=getinfo(), name='runThread1')
    t2 = threading.Thread(target=getmovie(1, ), name='runThread2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("(%s)结束" % threading.current_thread().name)
