import logging
import pymssql
import sys
import time
import datetime
import re

class Base(object):
    #定义构造函数，定义各种属性和logging类的配置
    def __init__(self):
        self.url = ""
        self.rule1 = ""
        self.rule2 = ""
        self.pageid = 0

        logging.basicConfig(level=logging.WARNING,#控制台打印的日志级别 DEBUG WARNING
                    # filename=sys.path[0]+'/log/'+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.log',
                    filename='./log/' + time.strftime('%Y-%m-%d',time.localtime(time.time())) + '.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )

    #数据库连接
    def db_conn(self):
            # server = '192.168.6.111\mssqlzf'
            # user = 'sa'
            # password = 'sa@2016'
            # database = 'zfnewdb'
            # charset = 'utf8'
            # port = '1433'
            server = 'localhost'
            user = 'BJUser1'
            password = 'stock_BJ2010'
            database = 'ZFJSSITE'
            charset = 'utf8'
            port = '24567'
            return pymssql.connect(host=server, user=user, password=password, database=database, charset=charset, port=port)
            # return pymssql.connect(server, user, password, database)

    #对信息进行分类其中title_num/content_num分别为，item中title和content所在位置
    def do_category(self, item, title_num, content_num):
        # print(item[0])
        title = item[title_num]
        content = item[content_num]
        important_news_list = ["19个部","发改委","审计署","卫生计生委","中央财经委员会","中共中央政治局","上交所","深交所",
                     "中国人民银行/央行","证监会","银保监会","国家统计局","国家外汇局","中科院","社科院","新闻联播",
                     "新华网","人民网","新华社","人民日报","经济日报","中国证券报","证券时报","证券日报","经济参考报",
                     "北向资金","融资融券","财政政策","减税","货币政策","降息","降准","印花税","逆回购",
                     "中期借贷便利/MLF/TMLF","社保资金","养老金"]
        industry_list = ["种植业与林业","视听器材","半导体及元件","养殖业","公交","其他电子","国防军工","交运设备服务",
                       "非汽车交运","通信服务","仪器仪表","环保工程","专用设备","电气设备","汽车零部件","建筑装饰",
                       "计算机设备","纺织制造","服装家纺","电子制造","通用设备","新材料","景点及旅游","建筑材料",
                       "燃气水务","化工合成材料","计算机应用","农产品加工","化工新材料","基础化学","化学制品",
                       "有色冶炼加工","证券","酒店及餐饮","园区开发","光学光电子","汽车整车","电力","煤炭开采加工",
                       "传媒","贸易","家用轻工","钢铁","零售","采掘服务","通信设备","石油矿业开采","包装印刷",
                       "白色家电","房地产开发","医疗器械服务","港口航运","造纸","化学制药","公路铁路运输",
                       "保险及其他","物流","银行","医药商业","中药","综合","机场航运","农业服务","饮料制造",
                       "生物制品","食品加工制造"]
        #读取存在文件中的上市公司名称，并转为list
        f = open("./companyName/companyName.txt", 'r', encoding="ISO-8859-1")
        # f = open("./companyName/companyName.txt", 'r')
        companyname = f.read()
        company_list = companyname.split(",")

        data_list = ["%", "百分比", "基点"]
        if any(important_news_title in title for important_news_title in important_news_list):
            return [1, "重大新闻"]
        
        elif any(industry in title for industry in industry_list):
            return [2, "行业"]

        elif any(company in title for company in company_list):
            return[3, "公告"]

        elif any(data_name in title for data_name in data_list):
            return [4, "数据"]
        
        elif any(data_name in content for data_name in data_list):
            return [4, "数据"]
            
        else:
            return [0, "全部"]

    #获取爬取页面中数据库里最新数据的时间，返回datetime
    def get_newest_time_by_pageid(self):
        conn = self.db_conn()
        cursor = conn.cursor()
        # 获取该爬取页面在数据库中最新的一条数据
        cursor.execute('select top 1 publicTime_d from tblGrabNews where pageId =' + str(
            self.pageid) + ' order by publicTime_d desc')
        values_new = cursor.fetchall()
        if len(values_new) == 0:
            return datetime.datetime.strptime("1980-01-01 00:00:00", '%Y-%m-%d %H:%M:%S')
        else:
            return values_new[0][0]

    #去除html标签
    def remove_html_tab(self, item, index1, index2):
        # 去除html标签
        item = list(item)
        pattern = re.compile(r'<[^>]+>', re.S)
        item[index1] = pattern.sub('', item[index1])
        item[index2] = pattern.sub('', item[index2])
        return item
        # end

        
