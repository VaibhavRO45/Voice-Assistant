from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

class music1():
    def __init__(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        
    def play1(self, query):
        self.query = query
        self.driver.get(url="https://open.spotify.com/search/" + query)
        
       # search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        video = self.driver.find_element(By.XPATH, '//*[@id="searchPage"]/div/div/section[2]/section/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/img')
        video.click()
        #search.send_keys(query)
      #  enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        #enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        #enter.click()


        


        sleep(300)
        #title = self.driver.title
        ##assert "Wikipedia" in title
        #print("TEST: Title test passed")'''
'''assist = music1()
assist.play("BULLEYA")'''
# Create an instance of infow class