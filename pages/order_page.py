import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    @allure.step('Нажимаем кнопку Согласие с куками')
    def click_on_cookie(self):
        self.click_on_element(OrderPageLocators.COOKIE_LOC)

    @allure.step('Переходим на страницу создания заказа и вводим данные')
    def order_step_1_data(self, name, last_name, address, num_tel):
        self.past_input_text(OrderPageLocators.INPUT_NAME_LOC, name)
        self.past_input_text(OrderPageLocators.INPUT_LAST_NAME_LOC, last_name)
        self.past_input_text(OrderPageLocators.INPUT_ADDRESS_LOC, address)
        self.click_on_element(OrderPageLocators.INPUT_METRO_STATION_LOC)
        self.click_on_element(OrderPageLocators.INPUT_STATION_LOC)
        self.past_input_text(OrderPageLocators.INPUT_TEL_LOC, num_tel)
        self.click_on_element(OrderPageLocators.BUTTON_NEXT_LOC)

    @allure.step('Продолжаем создание заказа и водим подробности аренды')
    def order_step_2_options(self, data_rent):
        self.click_on_element(OrderPageLocators.INPUT_DATA_GET_ORDER_LOC)
        self.past_input_text(OrderPageLocators.INPUT_DATA_GET_ORDER_LOC, data_rent)
        self.click_on_element(OrderPageLocators.INPUT_RENT_TIME_LOC)
        self.click_on_element(OrderPageLocators.TEXT_RENT_TIME_LOC)
        self.click_on_element(OrderPageLocators.CHECKBOX_COLOR_LOC)
        self.click_on_element(OrderPageLocators.BUTTON_ORDER_LOC)

    @allure.step('Подтверждаем создание заказа')
    def order_step_3_finish(self):
        self.click_on_element(OrderPageLocators.BUTTON_YES_LOC)
        return self.get_text(OrderPageLocators.BUTTON_STATUS_LOC)



