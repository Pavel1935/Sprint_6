from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, "//div[@id='accordion__heading-{num}']"
    ANSWER_LOCATOR = By.XPATH, "//div[@id='accordion__panel-{num}']"
    LAST_QUESTION_LOCATOR = By.XPATH, "//div[@id='accordion__heading-7']"
    COOKIE_LOCATOR = By.XPATH, "//button[@id='rcc-confirm-button']"


