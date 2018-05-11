#!/usr/bin/env python
#-*- coding:utf-8 -*-

import asyncio
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChromeRquest(object):
    def __init__(self):
        self.chrome_path = "/usr/bin/google-chrome-stable"
        self.chrome_driver_binary = "/home/eli/myspider/chromedriver"
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = self.chrome_path
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.brower = webdriver.Chrome(self.chrome_driver_binary, chrome_options=self.options)

    def request(self,url):
        self.brower.get(url)
        try:
            moreBtn = self.brower.find_element_by_class_name("detail-more")
            moreBtn.click()
            source = self.brower.page_source
        except NoSuchElementException:
                source = self.brower.page_source
        return source

    def parse_chapter_page(self,source):
        #html = etree.HTMLParser(source,encoding='utf-8')
        html = etree.HTML(source)
        title = html.xpath('//div[@class="banner_detail_form"]/div[@class="info"]/p[@class="title"]/text()')
        author = html.xpath('//div[@class="info"]//p[@class="subtitle"]/a/text()')
        #chapter_pages = html.xpath('//div[@id="chapterlistload"]/ul//li')
        chapter_pages = html.xpath('//div[@id="chapterlistload"]/ul//li//a/text()')
        chapter_pages = [ i.strip() for i in chapter_pages ]

        print(title,author)
        print(chapter_pages)

if __name__ == '__main__':
        spider = ChromeRquest()
        html = spider.request('http://tel.1kkk.com/manhua37169/')
        spider.parse_chapter_page(html)
