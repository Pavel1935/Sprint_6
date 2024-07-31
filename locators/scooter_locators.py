from selenium.webdriver.common.by import By


class ScooterLocators:
    ORDER_BUTTON_UP_LOC = By.XPATH, "//button[@class='Button_Button__ra12g']"
    # кнопка "Заказать" сверху
    BUTTON_SCOOTER_LOC = By.XPATH, "//img[@src='/assets/scooter.svg']"
    # кнопка "Самокат"
    