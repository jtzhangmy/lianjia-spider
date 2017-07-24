# -*- coding: utf-8 -*-
import scrapy
from lianjia.items import LianjiaItem

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = []

    def start_requests(self):
        global headers
        urlhead = 'https://bj.lianjia.com/ershoufang/'
        for i in range(1,2):
            url = urlhead + 'pg%s' % i
            self.start_urls.append(url)
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        global headers
        for url in response.xpath('//div[@class="info clear"]/div[@class="title"]/a/@href').extract():
            yield scrapy.Request(url, headers=headers, callback=self.parse_fangjia)

    def parse_fangjia(self, response):
        item = LianjiaItem()
        item['title'] = self.ifNull(response.xpath('//h1[@class="main"]/text()').extract())
        item['plot'] = self.ifNull(response.xpath('//div[@class="communityName"]/a[@class="info"]/text()').extract())    # 小区
        item['floor'] = self.ifNull(response.xpath('//div[@class="room"]/div[@class="subInfo"]/text()').extract())       # 楼层
        item['area'] = self.ifNull(response.xpath('//div[@class="areaName"]/span[@class="info"]/a[1]/text()').extract())  # 区域
        item['price'] = self.ifNull(response.xpath('//span[@class="total"]/text()').extract())                           # 总价
        item['unitPrice'] = self.ifNull(response.xpath('//span[@class="unitPriceValue"]/text()').extract())              # 单价

        item['coveredArea'] = self.ifNull(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[3]/text()').extract())   # 建筑面积
        item['insideArea'] = self.ifNull(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[5]/text()').extract())  # 套内面积
        item['direction'] = self.ifNull(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[7]/text()').extract())   # 房屋朝向
        item['fitment'] = self.ifNull(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[9]/text()').extract())   # 装修情况
        item['heatingType'] = self.ifNull(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[11]/text()').extract())   # 供暖情况
        item['propertyTime'] = self.ifNull(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[13]/text()').extract())  # 产权年限

        item['inFloor'] = self.ifNull(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[2]/text()').extract())  # 所在楼层
        item['houseType'] = self.ifNull(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[4]/text()').extract())  # 户型结构
        item['buildType'] = self.ifNull(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[6]/text()').extract())  # 建筑类型
        item['liftProportion'] = self.ifNull(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[8]/text()').extract()) # 梯户比例
        item['isLift'] = self.ifNull(response.xpath('//div[@class="base"]/div[@class="content"]/ul/li[10]/text()').extract())  # 配备电梯

        item['hangTime'] = self.ifNull(response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[1]/text()').extract())  # 挂牌时间
        item['lastDeal'] = self.ifNull(response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[3]/text()').extract())  # 上次交易
        item['ageLimit'] = self.ifNull(response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[5]/text()').extract())  # 房屋年限
        item['pledgeInfo'] = self.ifNull(response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[7]/span[2]/text()').extract())  # 抵押信息
        item['buildingType'] = self.ifNull(response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[2]/text()').extract())  # 交易权属
        item['housePurpose'] = self.ifNull(response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[4]/text()').extract())  # 房屋用途
        item['propertyRight'] = self.ifNull(response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[6]/text()').extract())  # 产权所属
        item['propertyCertificate'] = self.ifNull(response.xpath('//div[@class="transaction"]/div[@class="content"]/ul/li[8]/text()').extract())  # 房本具备
        yield item

    def ifNull(self, argument):
        if (argument):
            return argument
        else:
            return ''


