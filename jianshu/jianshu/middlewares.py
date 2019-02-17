from scrapy import signals
from selenium import webdriver
import random
import time
from scrapy.http.response.html import HtmlResponse

class UserAgentDownLoadMiddleware(object):
    USER_AGENT = [
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)',
        'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)'
    ]

    def process_request(self,request,spider):
        user_agent = random.choice(self.USER_AGENT)
        request.headers['User-Agent'] = user_agent


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.drive = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')


    def process_request(self,request,spider):
        self.drive.get(request.url)
        time.sleep(1)
        try:
            while True:
                showmore = self.drive.find_element_by_class_name('show-more')
                showmore.click()
                time.sleep(0.3)
                if not showmore:
                    break
        except:
            pass

        source = self.drive.page_source
        response = HtmlResponse(url=self.drive.current_url,body=source,request=request,encoding='utf-8')
        return response