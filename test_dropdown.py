"""
Тест для выпадающего списка
Сайт: https://the-internet.herokuapp.com/dropdown
Задача: нажать на Dropdown и выбрать значение
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def setup_driver():
    """
    Настройка и запуск драйвера Chrome
    
    Returns:
        webdriver.Chrome: экземпляр драйвера
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def open_dropdown_page(driver):
    """
    Открывает страницу с выпадающим списком
    
    Args:
        driver: экземпляр WebDriver
    """
    driver.get("https://the-internet.herokuapp.com/dropdown")


def wait_for_dropdown(driver, timeout=10):
    """
    Ожидает появления выпадающего списка на странице
    
    Args:
        driver: экземпляр WebDriver
        timeout: время ожидания в секундах
    
    Returns:
        WebElement: элемент выпадающего списка
    """
    dropdown = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, "dropdown"))
    )
    return dropdown


def select_option_by_text(driver, option_text):
    """
    Выбирает опцию в выпадающем списке по видимому тексту
    
    Args:
        driver: экземпляр WebDriver
        option_text: текст опции для выбора
    """
    dropdown = driver.find_element(By.ID, "dropdown")
    select = Select(dropdown)
    select.select_by_visible_text(option_text)


def get_selected_option_text(driver):
    """
    Возвращает текст выбранной опции
    
    Args:
        driver: экземпляр WebDriver
    
    Returns:
        str: текст выбранной опции
    """
    dropdown = driver.find_element(By.ID, "dropdown")
    select = Select(dropdown)
    return select.first_selected_option.text


def test_dropdown_selection():
    """
    Основной тест: открыть dropdown и выбрать значение
    """
    driver = None
    
    try:
        print("=" * 50)
        print("ЗАПУСК ТЕСТА DROPDOWN")
        print("=" * 50)
        
        # Шаг 1: Запуск браузера
        print("1. Запуск браузера")
        driver = setup_driver()
        
        # Шаг 2: Открытие страницы
        print("2. Открытие страницы https://the-internet.herokuapp.com/dropdown")
        open_dropdown_page(driver)
        
        # Шаг 3: Ожидание загрузки
        print("3. Ожидание загрузки выпадающего списка")
        wait_for_dropdown(driver)
        print("   Страница загружена")
        
        # Шаг 4: Получение доступных опций
        print("4. Проверка доступных опций")
        dropdown = driver.find_element(By.ID, "dropdown")
        select = Select(dropdown)
        options = [opt.text for opt in select.options]
        print(f"   Доступные опции: {options}")
        
        # Шаг 5: Выбор Option 1
        print("5. Выбор опции 'Option 1'")
        select_option_by_text(driver, "Option 1")
        selected = get_selected_option_text(driver)
        print(f"   Выбрано: '{selected}'")
        
        # Проверка
        assert selected == "Option 1", \
            f"Ошибка: ожидалось 'Option 1', получено '{selected}'"
        print("   Проверка: Option 1 выбран корректно")
        
        # Шаг 6: Выбор Option 2
        print("6. Выбор опции 'Option 2'")
        select_option_by_text(driver, "Option 2")
        selected = get_selected_option_text(driver)
        print(f"   Выбрано: '{selected}'")
        
        # Проверка
        assert selected == "Option 2", \
            f"Ошибка: ожидалось 'Option 2', получено '{selected}'"
        print("   Проверка: Option 2 выбран корректно")
        
        print("\n" + "=" * 50)
        print("ТЕСТ ПРОЙДЕН УСПЕШНО")
        print("=" * 50)
        
    except AssertionError as e:
        print(f"\nОШИБКА ПРОВЕРКИ: {e}")
        raise
        
    except Exception as e:
        print(f"\nОШИБКА: {e}")
        raise
        
    finally:
        if driver:
            print("\nЗакрытие браузера...")
            driver.quit()
            print("Браузер закрыт")


if __name__ == "__main__":
    test_dropdown_selection()