from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about


url = "https://sbis.ru/"


class Locators:
    """
    Локаторы элементов Web-страницы
    """
    Contacts = (By.LINK_TEXT, "Контакты")
    Tensor_link = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
    Sila_v_lyudyah = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    Podrobnee_link = (By.CSS_SELECTOR, '[href="/about"]')


def element_to_find(driver, locator, time=5):
    """
    Функция ожидает до тех пор, пока не найдёт элемент
    :param driver:  драйвер браузера
    :param locator: Локатор объекта
    :param time: Время ожидания
    :return: Элемент Web-страницы
    """
    element = WebDriverWait(driver, time).until(EC.presence_of_element_located(locator))
    return element


def move_to(driver, element):
    """
    Перемещает к указанному элементу
    :param driver: драйвер браузера
    :param element: Элемент, к которому нужно двигаться
    :return:
    """
    actions = ActionChains(driver)
    actions.move_to_element(element)
    return actions.perform()


def test_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(url=url)  # Переходим на sbis.ru
        element = element_to_find(driver, Locators.Contacts)  # Находим кнопку "Контакты"
        element.click()
        element = element_to_find(driver, Locators.Tensor_link)  # Находим баннер "Тензор"
        element.click()
        # 4
        windows = driver.window_handles
        driver.switch_to.window(windows[1])  # Явно указываем переключение на новое окно
        assert driver.current_url == "https://tensor.ru/"  # Проверяем ссылку рабочей страницы
        element = element_to_find(driver, Locators.Sila_v_lyudyah)  # Находим блок сила в людях
        move_to(driver, element)  # Перемещаемся к этому блоку
        assert element.is_displayed()  # Проверяем что блок теперь виден на дисплее
        element = element_to_find(driver, Locators.Podrobnee_link)  # Находим блок "Сила в людях"
        element.click()
        assert driver.current_url == 'https://tensor.ru/about'  # Проверяем ссылку рабочей страницы
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
