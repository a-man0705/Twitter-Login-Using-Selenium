import username
from selenium import webdriver
from confidential import username,password

class Bot():
    def __init__(self):
        self.driver=webdriver.Chrome()

    def tweet(self):
        self.driver.get('https://twitter.com/login?lang=en-gb')

        user=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        user.click()
        user.send_keys(username)

        pswd=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        pswd.click()
        pswd.send_keys(password)

        btn=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
        btn.click()

bot=Bot()
bot.tweet()
