from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили


class Locators:
    """
    Локаторы элементов Web-страницы
    """
    Login = (By.CSS_SELECTOR, '[type="text"]')
    Password = (By.CSS_SELECTOR, '[type="password"]')
    Contacts_acord = (By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"]')
    Chats_btn = (By.CSS_SELECTOR, '[name="TabContent1"]')
    Chats_list_target = (By.CSS_SELECTOR, '[title="Автотестирование Раздела"]')
    Msg_input = (By.CSS_SELECTOR, '[class="textEditor_Viewer__Paragraph"]')
    Enter_btn = (By.CSS_SELECTOR, '.icon-EnterRight')
    Chats_history = (By.CSS_SELECTOR, '.msg-dialogs-item__addressee_limited')
    Chats_msg_text = (By.CSS_SELECTOR, '.msg-dialogs-item__message-text')
    Chats_row_1 = (By.CSS_SELECTOR, '.controls-ListView__item_default-topPadding_null')
    Erase_btn = (By.CSS_SELECTOR, '.icon-Erase')
    No_msg_text = (By.CSS_SELECTOR, '.hint-Template__text_message_m')


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


url = "https://fix-online.sbis.ru/"
user_login, user_password = 'автотестирование_имущество', 'автотестирование_имущество'


def test():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(url=url)   # Переходим на fix-online.sbis.ru
        sleep(1)
        # Вводим логи и пароль
        login = element_to_find(driver, Locators.Login)
        login.send_keys(user_login, Keys.ENTER)
        password = element_to_find(driver, Locators.Password)
        password.send_keys(user_password, Keys.ENTER)
        sleep(1)
        # Находим в аккордеоне "Контакты" и кликаем дважды
        element = element_to_find(driver, Locators.Contacts_acord)
        actionChains = ActionChains(driver)
        actionChains.double_click(element).perform()
        sleep(2)
        # 3
        element = element_to_find(driver, Locators.Chats_btn)  # Находим кнопку "Чаты"
        element.click()
        # В чатах находим себя и проверяем, чтобы отправить сообщение
        element = element_to_find(driver, Locators.Chats_list_target)
        assert element.text == 'Автотестирование Раздела'
        element.click()
        # Оправляем тестовое сообщение
        element = element_to_find(driver, Locators.Msg_input)
        element.send_keys('test')
        sleep(2)
        element = element_to_find(driver, Locators.Enter_btn) # Находим кнопку "Создать новый диалог"
        element.click()
        # Проверяем что сообщение отправилось и находится в реестре
        element = element_to_find(driver, Locators.Chats_history)
        assert element.text == 'Автотестирование Раздела'
        element = element_to_find(driver, Locators.Chats_msg_text)
        assert element.text == 'test'
        # Перемещаемся к сообщению и наводимся на него
        element = element_to_find(driver, Locators.Chats_row_1)
        actionChains = ActionChains(driver)
        actionChains.move_to_element(element)
        actionChains.perform()
        element = element_to_find(driver, Locators.Erase_btn)  # Находим кнопку "Перенести в удалённые"
        element.click()
        sleep(2)
        element = element_to_find(driver, Locators.No_msg_text)
        assert element.text == 'У вас нет сообщений'  # Проверяем что сообщение удалилось
    except Exception as e:
        print(e)
    finally:
        driver.close()
        driver.quit()
