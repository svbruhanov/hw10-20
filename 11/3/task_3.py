from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import os
import requests

# Перейти на https://sbis.ru/
# В Footer'e найти "Скачать СБИС"(Footer -> 'Скачать локальные версии' ->СБИС Плагин
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах


class Locators:
    """
    Локаторы элементов Web-страницы
    """
    FooterDW = (By.CSS_SELECTOR, '[href="/download"]')
    DW_btn = (By.CSS_SELECTOR, '[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')


def element_to_find(driver, locator, time=10):
    """
    Функция ожидает до тех пор, пока не найдёт элемент
    :param driver:  драйвер браузера
    :param locator: Локатор объекта
    :param time: Время ожидания
    :return: Элемент Web-страницы
    """
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    element = WebDriverWait(driver, time, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located(locator))
    return element


def test():
    """
    Тест сценария
    :return:
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(url="https://sbis.ru/")  # Переход на sbis.ru
        element = element_to_find(driver, Locators.FooterDW)  # Находим кнопку "Скачать локальные версии"
        element.send_keys(Keys.END)  # Листаем в самый низ страницы
        element.click()
        # Находим кнопки и кликаем по той, у которой текст 'СБИС Плагин'
        buttons = driver.find_elements(By.CSS_SELECTOR, '[data-component="SBIS3.CONTROLS/Tab/Button"]')
        for i in range(0, len(buttons)):
            if buttons[i].text == 'СБИС Плагин':
                buttons[i].click()
        element = element_to_find(driver, Locators.DW_btn)  # Находим кнопку "Скачать"
        url = element.get_attribute('href')  # Берём ссылку на скачивание файла
        filename = "sbis_plugin.exe"
        response = requests.get(url, allow_redirects=True)  # Посылаем запрос по ссылке
        assert response.status_code == 200  # Проверяем статус запроса
        # Сохраняем контент файла
        with open(filename, mode="wb") as file:
            file.write(response.content)
        dir_path = os.path.dirname(os.path.realpath(__file__))  # Путь локальной директории
        dir_path += '\{0}'.format(filename)  # Добавляем к пути имя скаченного файла
        file_size = round((os.path.getsize(dir_path) / 1024 / 1024), 2)  # Вычисляем размер файла в МБ
        print(f'\n{file_size} МБ')
        sleep(2)
        # 2
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
