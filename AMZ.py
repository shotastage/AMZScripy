import os, platform
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


DRIVER_PATH = os.path.join(os.environ['HOME'], ".amz_scraper", "webdriver", "chromedriver")


class AMZ():

    def __init__(self):
        self.driver = webdriver.Chrome(DRIVER_PATH)
        self.driver.get('https://www.amazon.co.jp/')
        self.driver.implicitly_wait(10)


    def search(self, word):
        self.driver.find_element_by_id('twotabsearchtextbox').send_keys(word)
        self.driver.find_element_by_class_name('nav-input').click()

    def next_page(self):
        elm = self.driver.find_element_by_class_name('navFooterBackToTopText')
        actions = ActionChains(self.driver)
        actions.move_to_element(elm)
        actions.perform()

        try:
            self.driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[7]/div/div/div/ul/li[7]/a').click()
            return True
        except:
            return False

    def complete(self):
        self.driver.close()
        self.driver.quit()

        if platform.system() == 'Darwin':
            os.system("osascript -e 'display notification \"" + "AMZ Scraper: " + "Scraping has been completed!" + "\"'")
