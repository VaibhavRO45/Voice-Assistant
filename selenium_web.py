from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pyttsx3 as p


class infow():
    def __init__(self):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        
    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
       # search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
      #  enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()
        
        try:
            paragraphs = self.driver.find_elements(By.CSS_SELECTOR, ".mw-parser-output p")
            first_two_paragraphs = "\n\n".join([p.text for p in paragraphs[:3]])
            
            engine = p.init()
            engine.setProperty('rate', 150)  # Speed percent (can go over 100)
            engine.setProperty('volume', 0.9)  # Volume 0-1

            engine.say(first_two_paragraphs)
            engine.runAndWait()

        except Exception as e:
            print("Error occurred:", e)

        # Close the browser
        self.driver.quit()


        


        '''sleep(300)
        title = self.driver.title
        assert "Wikipedia" in title
        print("TEST: Title test passed")
'''
       

# Create an instance of infow class
