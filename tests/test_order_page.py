import allure
import pytest
from constants import Data
from locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage


class TestOrderPage:
    @pytest.mark.parametrize(
        "button, name, last_name, address, num_tel, data_rent",
        [
            (OrderPageLocators.ORDER_BUTTON_UP, Data.NAME,
             Data.LAST_NAME, Data.ADDRESS, Data.NUM_TEL, Data.DATA_RENT),
            (OrderPageLocators.ORDER_BUTTON_DOWN, Data.NAME_1, Data.LAST_NAME_1, Data.ADDRESS_1,
             Data.NUM_TEL_1, Data.DATA_RENT_1)
        ])
    @allure.title('Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def test_order_steps(self, driver, button, name, last_name, address, num_tel, data_rent):
        order_page = OrderPage(driver)
        order_page.click_on_cookie()
        order_page.click_on_element(button)
        order_page.order_step_1_data(name, last_name, address, num_tel)
        order_page.order_step_2_options(data_rent)
        result = order_page.order_step_3_finish()
        assert result == 'Посмотреть статус'

