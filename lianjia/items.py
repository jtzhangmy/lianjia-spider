# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    title = scrapy.Field()
    plot = scrapy.Field()                   # 小区
    floor = scrapy.Field()                  # 楼层
    area = scrapy.Field()                   # 区域
    price = scrapy.Field()                  # 总价
    unitPrice = scrapy.Field()              # 单价
    time = scrapy.Field()                   # 发布时间

    coveredArea = scrapy.Field()            # 建筑面积
    insideArea = scrapy.Field()             # 套内面积
    direction = scrapy.Field()              # 房屋朝向
    fitment = scrapy.Field()                # 装修情况
    heatingType = scrapy.Field()            # 供暖情况
    propertyTime = scrapy.Field()           # 产权年限

    inFloor = scrapy.Field()                # 所在楼层
    houseType = scrapy.Field()              # 户型结构
    buildType = scrapy.Field()              # 建筑类型
    liftProportion = scrapy.Field()         # 梯户比例
    isLift = scrapy.Field()                 # 配备电梯

    hangTime = scrapy.Field()               # 挂牌时间
    lastDeal = scrapy.Field()               # 上次交易
    ageLimit = scrapy.Field()               # 房屋年限
    pledgeInfo = scrapy.Field()             # 抵押信息
    buildingType = scrapy.Field()           # 交易权属
    housePurpose = scrapy.Field()           # 房屋用途
    propertyRight = scrapy.Field()          # 产权所属
    propertyCertificate = scrapy.Field()    # 房本具备
    pass
