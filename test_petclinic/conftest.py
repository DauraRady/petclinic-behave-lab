import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10) 
    yield driver  
    driver.quit()  

def test_duckduckgo_search(browser):

    browser.get("https://duckduckgo.com/")

    search_box = browser.find_element(By.XPATH, "//input[@id='searchbox_input']")
    search_box.send_keys("Panda")

    search_button = browser.find_element(By.XPATH, "//button[@aria-label='Search']")
    search_button.click()

    results = browser.find_elements(By.CSS_SELECTOR, "a.result__a")
    
    
    assert len(results) > 0, "❌ Aucun résultat affiché sur DuckDuckGo !"
    print("✅ Test réussi : Les résultats sont bien affichés.")





