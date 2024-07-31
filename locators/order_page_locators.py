from selenium.webdriver.common.by import By


class OrderPageLocators:
    COOKIE_LOC = By.XPATH, "//button[@id='rcc-confirm-button']"
    # кнопка "Принять cookies"
    ORDER_BUTTON_UP = By.XPATH, "//button[@class='Button_Button__ra12g']"
    # кнопка "Заказать" сверху
    ORDER_BUTTON_DOWN = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    # кнопка "Заказать" снизу
    PAGE_TITLE_LOC = By.XPATH, "//div[@class='Order_Header__BZXOb']"
    #заголовок страница заказа
    INPUT_NAME_LOC = By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and @placeholder='* Имя']"
    # инпут имя
    INPUT_LAST_NAME_LOC = By.XPATH, "//input[contains(@class, 'Input_Input__1iN_Z') and @placeholder='* Фамилия']"
    # инпут фамилия
    INPUT_ADDRESS_LOC = By.XPATH, ("//input[contains(@class, 'Input_Input__1iN_Z')"
                                       " and @placeholder='* Адрес: куда привезти заказ']")
    # инпут адрес
    INPUT_METRO_STATION_LOC = By.XPATH, "//input[@placeholder='* Станция метро']"
    # инпут открывающий дроп даун станций
    INPUT_STATION_LOC = By.XPATH, "//div[text()='Черкизовская']"
    # выбор станции
    INPUT_TEL_LOC = By.XPATH, ("//input[contains(@class, 'Input_Input__1iN_Z')"
                           " and @placeholder='* Телефон: на него позвонит курьер']")
    # инпут телефон
    BUTTON_NEXT_LOC = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    # кнопка "Далее"
    INPUT_DATA_GET_ORDER_LOC = By.XPATH, ("//input[contains(@class, 'Input_Input__1iN_Z')"
                           " and @placeholder='* Когда привезти самокат']")
    # инпут когда привезти самокат
    INPUT_RENT_TIME_LOC = By.XPATH, "//span[@class='Dropdown-arrow']"
    # дроп даун срок аренды
    TEXT_RENT_TIME_LOC = By.XPATH, "//div[contains(text(),'сутки')]"
    # текст выбранного срока аренды
    CHECKBOX_COLOR_LOC = By.XPATH, "//input[@id='black']"
    # чекбокс цвета
    BUTTON_BACK_LOC = ("//button[@class='Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i']")
    # кнопка назад
    BUTTON_ORDER_LOC = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
    # кнопка заказать
    BUTTON_YES_LOC = By.XPATH, "//button[contains(text(),'Да')]"
    # кнопка "да" в окне "хотите оформить заказ"
    BUTTON_STATUS_LOC = By.XPATH, "//button[contains(text(),'Посмотреть статус')]"
    # локатор кнопки "посмотреть статус"
    NAME_TEXT_LOC = By.XPATH, "//div[contains(text(),'Имя')]"
    # текст "имя" на странице заказа



