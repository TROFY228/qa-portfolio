"""
Автотест: Форма входа Saucedemo
Автор: Ильяс
Дата: 08.04.2026
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login_success():
    """Тест успешной авторизации"""
    # Инициализация браузера
    driver = webdriver.Chrome()
    
    try:
        # Открыть сайт
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        
        # Найти поля ввода
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")
        
        # Ввести данные
        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        
        # Нажать Login
        login_button.click()
        
        # Подождать загрузку
        time.sleep(2)
        
        # Проверить, что перешли на главную
        assert "inventory" in driver.current_url
        print("✅ Тест пройден: Успешная авторизация")
        
    except AssertionError:
        print("❌ Тест провален: Не удалось авторизоваться")
    finally:
        # Закрыть браузер
        driver.quit()

def test_login_invalid_password():
    """Тест с неверным паролем"""
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        # Ввести неверные данные
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("wrong_pass")
        driver.find_element(By.ID, "login-button").click()
        
        time.sleep(2)
        
        # Проверить наличие ошибки
        error_message = driver.find_element(By.CLASS_NAME, "error-message")
        assert error_message.is_displayed()
        print("✅ Тест пройден: Ошибка отображается")
        
    finally:
        driver.quit()

# Запуск тестов
if __name__ == "__main__":
    print("Запуск тестов Saucedemo...")
    test_login_success()
    test_login_invalid_password()
    print("Все тесты завершены!")
