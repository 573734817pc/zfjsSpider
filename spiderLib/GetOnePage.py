#爬取整个页面数据的类
#param：url
from spiderLib import Base
import requests
from requests.exceptions import RequestException
class GetOnePage(Base.Base):
    #爬取整个页面数据的方法
    def get_one_page(self, url):
        try:
            response = requests.get(url)
            #防止乱码
            response.encoding = response.apparent_encoding
            if response.status_code == 200:
                return response.text
            return None
        except RequestException:
            return None
