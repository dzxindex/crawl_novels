import urllib.request
# http://www.booktxt.net/1_1439/482060.html
# http://www.booktxt.net/1_1439/482061.html
import re


class Spider:
    def __init__(self):
        #初始化页面
        self.page = 482060
        #爬取开关，True 继续爬去
        self.switch = True

    def loadPage(self):
        url = 'http://www.booktxt.net/1_1439/' + str(self.page) + '.html'
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}

        #使用请求头
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        #每页的html 源码
        html_gbk = response.read()
        html_utf = html_gbk.decode('gbk')
        # print(html_utf)


        #创建正则表达式对象，匹配每页段子内容，re,S 表示匹配全部字符串内容
        pattern = re.compile('<div\sid="content">(.*?)</div>', re.S)

        #将正则匹配对象应用到html源码，返回页面所有段子内容
        content_list = pattern.findall(html_utf)

        for item in content_list:
            item = item.replace('<br />','').replace('&nbsp;&nbsp;&nbsp;&nbsp;',' ')

            self.writePage(item)




    def writePage(self,item):
        with open('xiuzhen.txt', 'w') as f:
            f.write(item)
        print('正在写入数据%s',self.page)
    #     self.page += 1
    #     self.loadPage()
    #     self.start_work()
    #
    # def start_work(self):
    #     while self.switch:
    #         command = input('继续爬取，请按回车,停止按quit:')
    #         if command == 'quit':
    #             self.switch == False
    #     self.page += 1
    #     self.loadPage()


# if __name__ =='__mian__':
xiuzhen = Spider()
xiuzhen.loadPage()
