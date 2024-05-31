from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

class music():
    def __init__(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        
    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
       # search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
        video.click()
        #search.send_keys(query)
      #  enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        #enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        #enter.click()


        


        sleep(300)
        title = self.driver.title
        assert "Wikipedia" in title
        print("TEST: Title test passed")
'''assist = music()
assist.play("Soch na Sake")'''
# Create an instance of infow class