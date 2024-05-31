from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class infow1():
    def __init__(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        
    def get_info1(self, query):
        self.query = query
        self.driver.get(url="https://www.google.co.in/search?q=" + query)
       # search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
       # search = self.driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div[1]/div/div/span/a/div/div/div/div[1]/span')
        search = self.driver.find_element(By.CSS_SELECTOR, "div.g h3")
        search.click()
        search.send_keys(query)
      #  enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
       # enter = self.driver.find_element(By.XPATH, '//*[@id="tsf"]/div[1]/div[1]/div[2]/button/div/span/svg')
       # enter.click()
       # search.send_keys(Keys.RETURN)


        


        sleep(3000)
        title = self.driver.title
        assert "Wikipedia" in title
        print("TEST: Title test passed")
'''assist = infow1()
assist.get_info1("Dear Zindigi")
'''       

# Create an instance of infow class