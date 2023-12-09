from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
import time
import pickle

#大麦网首页
damai_url = 'https://www.damai.cn/'
#大麦网登录页面
damai_login = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'
#演唱会抢票页面
target_url = ''
service = Service(r"F:\\Anaconda3\\chromedriver.exe")
class Concert:
    def __init__(self):
        self.status = 0 #状态 表示当前操作执行到了哪一步
        self.login_method = 1 #{0:模拟登陆 1：cookie登陆}
        self.driver = webdriver.Chrome(service=service) #初始化浏览器

    def set_cookie(self):
        self.driver.get(damai_login)
        print("请登陆")
        time.sleep(10) #延迟十秒让我登陆
        print("登陆成功")
        pickle.dump(self.driver.get_cookies(), open('cookie.pkl', 'wb'))
        print("cookie保存成功")
        #抢票
        self.driver.get(target_url)
    
    def get_cookie(self):
        cookies = pickle.load(open('cookie.pkl','rb'))
        for cookie in cookies:
            print(cookie)



    '''登陆'''
    def login(self):
        if self.login_method == 0:
            self.driver.get(damai_login)
        elif self.login_method == 1:
            if not os.path.exists('cookie.pkl'):
                self.set_cookie()
            else:
                self.get_cookie()
if __name__ == '__main__':
    concert = Concert()
    concert.login()

                