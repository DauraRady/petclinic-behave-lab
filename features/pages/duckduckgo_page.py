from selenium.webdriver.common.by import By

class DuckDuckGoPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "searchbox_input")
        self.search_button = (By.XPATH, "//button[@aria-label='Search']")
        self.result_links = (By.CSS_SELECTOR, "a.result__a")

    def open(self):
        self.driver.get("https://duckduckgo.com/")

    def enter_search(self, query):
        self.driver.find_element(*self.search_box).send_keys(query)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()

    def get_results(self):
        return self.driver.find_elements(*self.result_links)
