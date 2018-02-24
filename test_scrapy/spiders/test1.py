# -*- coding:utf-8 -*-
import sys,scrapy
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup

class companySpider(scrapy.Spider):
    name = 'test1'

    def start_requests(self):
        company_name = '浙江恒力建设有限公司'
        url = 'http://m.cbi360.net/hhb/SearchCompanyList.aspx?key=' + company_name
        yield scrapy.Request(url, callback=self.parse_company,meta={'company_name':company_name})

    def parse_company(self, response):
        company_name = response.meta['company_name']
        soup = BeautifulSoup(response.body, 'lxml')
        temp = soup.find('div', class_='soso_listnl').find_all('li')[0].find_all('font')
        # 有可能是第二的一个
        temp1 = soup.find('div', class_='soso_listnl').find_all('li')[1].find_all('font')
        com_name = ''
        com_name1 = ''
        for i in range(len(temp)):
            com_name += temp[i].text

        for j in range(len(temp1)):
            com_name1 += temp1[j].text

        if com_name == company_name:
            com_url = 'http://m.cbi360.net' + soup.find('div', class_='soso_listnl').find_all('li')[0].find('a')['href']
        elif com_name1 == company_name:
            com_url = 'http://m.cbi360.net' + soup.find('div', class_='soso_listnl').find_all('li')[1].find('a')['href']
        else:
            com_url = ''

        print com_url