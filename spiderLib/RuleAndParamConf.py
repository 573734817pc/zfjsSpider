from spiderLib import Main

#爬取页面参数配置类
#param1:url(string)
#param1:rule1(string)
#param1:rule2(string)
#param1:pageid(int)
class RuleAndParamConf(Main.Main):
    #获取公司名称
    def get_company_name(self):
        # #定义爬取的url
        self.url = 'https://www.banban.cn/gupiao/list_sh.html'
        # 定义爬取规则1
        self.rule1 = '<li>.*?<a href="/gupiao/\d.*?">([\u4e00-\u9fa5]+).*?</a>'
        # 定义爬取规则2
        self.rule2 = ''
        # 定义pageid
        self.pageid = 0
        # 调用main_pengpai方法
        self.main_get_company_name()

    # 澎湃新闻
    def pengpai(self):
        # #定义爬取的url
        self.url = 'https://www.thepaper.cn/load_index.jsp?nodeids=25434,25436,25433,25438,25435,25437,27234,25485,25432,37978,&topCids=,3420378,3419837,3418451&pageidx='
        # 定义爬取规则1
        self.rule1 = '<img.*?src="(.*?)".*?>.*?<h2>.*?href="(.*?)".*?>(.*?)</a>.*?</h2>.*?<p>(.*?)</p>.*?<div class="pdtt_trbs">.*?<a.*?>(.*?)</a>.*?<span>(.*?)</span>'
        # 定义爬取规则2
        self.rule2 = '<div class="news_about">.*?</p>.*?<p>.*?([\d-]+\s+[\d:]+).*?<span>'
        # 定义pageid
        self.pageid = 1
        #调用main_pengpai方法
        self.main_pengpai()

    # 中国经济网
    def zgjj(self):
        # #定义爬取的url
        # print('Run task %s...' % (os.getpid(),))
        self.url = 'http://finance.ce.cn/rolling/index.shtml'
        # 定义爬取规则1
        self.rule1 = '<td height="28".*?href="(.*?)".*?\[(.*?)\].*?</td>'
        # 定义爬取规则2
        self.rule2 = '<h1 id="articleTitle">(.*?)</h1>.*?<span id="articleSource">来源：(.*?)</span>.*?<div class="content" id="articleText">.*?><p.*?>(.*?)</p>'
        # 定义pageid
        self.pageid = 2
        # 调用Main类中的Main方法
        self.main_zgjj()

    # 中国科技网
    def zgkj(self):
        # 定义爬取的url
        # print('Run task %s...' % (os.getpid(),))
        self.url = 'http://www.stdaily.com/cxzg80/kejizixun/kejizixun'
        # 定义爬取规则1
        self.rule1 = '<dl>.*?<h3>.*?>(.*?)</a>.*?<dd>.*?<p>(.*?)</p>.*?"sp_1">(.*?)</span>'
        # 定义爬取规则2
        self.rule2 = ''
        # 定义pageid
        self.pageid = 3
        # 调用Main类中的Main方法
        self.main_zgkj()

    # 人民网
    def rmw(self):
        # 定义爬取的url
        self.url = 'http://finance.people.com.cn/GB/70846/index.html'
        # 定义爬取规则1
        self.rule1 = "<li>.*?<a href='(.*?)'.*?>.*?</li>"
        # 定义爬取规则2
        self.rule2 = 'text_title">.*?<h1>(.*?)</h1>.*?"fl">.*?([\d]+).*?([\d]+).*?([\d]+).*?([\d]+).*?([\d]+).*?"_blank">(.*?)</a>.*?<div class="box_pic"></div>.*?<p>(.*?)</p>'
        # 定义pageid
        self.pageid = 4
        # 调用Main类中的Main方法
        self.main_rmw()

    # 新浪财经7*24小时
    def xlcj(self):
        # 定义爬取的url
        # print('Run task %s...' % (os.getpid(),))
        self.url = 'http://zhibo.sina.com.cn/api/zhibo/feed?callback=jQuery111208852375871132476_1557710175201&page_size=20&zhibo_id=152&page='
        # 定义爬取规则1
        self.rule1 = '.*?"rich_text":"(.*?)".*?"create_time":"(.*?)".*?'
        # 定义爬取规则2
        self.rule2 = ''
        # 定义pageid
        self.pageid = 5
        # 调用Main类中的Main方法
        self.main_xlcj()

    # 36氪
    def ke(self):
        # 定义爬取的url
        self.url = 'https://36kr.com/newsflashes'
        # 定义爬取规则1
        self.rule1 = '"\/newsflashes\/([\d]{6})"'
        # 定义爬取规则2
        self.rule2 = '{"id":([\d]{6}),.*?"title":"(.*?)".*?"description":"(.*?)".*?"published_at":"(.*?)"'
        # 定义pageid
        self.pageid = 6
        # 调用Main类中的Main方法
        self.main_ke()