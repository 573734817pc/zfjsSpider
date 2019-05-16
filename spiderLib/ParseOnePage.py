#爬取页面中指定数据的类
#param1：html（整个页面的html代码）
#param2：get_rule(爬取规则)
from spiderLib import GetOnePage
import re
class ParseOnePage(GetOnePage.GetOnePage):
    def parse_one_page(self, html, get_rule):
        pattern = re.compile(get_rule, re.S)
        items = re.findall(pattern, html)
        return items
