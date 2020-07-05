from selenium import webdriver
import time

class Login: 
    def __init__(self):
        self.login_url = "https://shimo.im/login?from=home"
        # 需要填写个人账号/密码
        self.mobile = '15200000000'
        self.password = 'xxx123456'

    def run(self):
        try:
            browser = webdriver.Chrome()
            browser.get(self.login_url)
            time.sleep(1)
            browser.find_element_by_xpath('//input[@name=\'mobileOrEmail\']').send_keys(self.mobile)
            time.sleep(1)
            browser.find_element_by_xpath('//input[@name=\'password\']').send_keys(self.password)
            time.sleep(2)
            browser.find_element_by_xpath("//button[contains(text(), '立即登录')]").click()
            time.sleep(1)

            cookies = browser.get_cookies()
            print(cookies)
            time.sleep(3)
        except Exception as e:
           print(e)    
        finally:
            browser.close()

def main():
    im = Login()
    im.run()


if __name__ == '__main__':
    main()