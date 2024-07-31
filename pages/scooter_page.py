import allure

from locators.scooter_locators import ScooterLocators
from pages.base_page import BasePage


class ScooterPage(BasePage):
    @allure.step('Нажимаем на логотип самоката и редиректимся на морду')
    def click_scooter(self):
        self.click_on_element(ScooterLocators.ORDER_BUTTON_UP_LOC)
        self.click_on_element(ScooterLocators.BUTTON_SCOOTER_LOC)
        self.find_element_wait(ScooterLocators.ORDER_BUTTON_UP_LOC)
        return self.get_text(ScooterLocators.ORDER_BUTTON_UP_LOC)
