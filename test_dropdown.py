"""
Тест для выпадающего списка
Сайт: https://the-internet.herokuapp.com/dropdown
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def test_dropdown():
    driver = setup_driver()
    try:
        driver.get("https://the-internet.herokuapp.com/dropdown")
        
        dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dropdown"))
        )
        
        select = Select(dropdown)
        
        select.select_by_visible_text("Option 1")
        assert select.first_selected_option.text == "Option 1", "Не удалось выбрать Option 1"
        
        select.select_by_visible_text("Option 2")
        assert select.first_selected_option.text == "Option 2", "Не удалось выбрать Option 2"
        
        print("Тест пройден")
        
    finally:
        driver.quit()


if __name__ == "__main__":
    test_dropdown()
