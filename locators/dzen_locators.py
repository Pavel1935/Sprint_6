from selenium.webdriver.common.by import By


class DzenLocators:
    BUTTON_YANDEX_LOC = By.XPATH, "//img[@src='/assets/ya.svg']"
    # кнопка Яндекс
    BUTTON_MAIN_LOC = By.XPATH, "//div[contains(text(),'Новости')]"
    # кнопка войти