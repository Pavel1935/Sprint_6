import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.dzen_locators import DzenLocators
from pages.base_page import BasePage


class DzenPage(BasePage):
    @allure.step('Нажимаем на слово "Яндекс" и попадаем на страницу Дзена')
    def click_yandex_button(self):
        orig_window = self.driver.current_window_handle
        self.click_on_element(DzenLocators.BUTTON_YANDEX_LOC)
        WebDriverWait(self.driver, 10).until(expected_conditions.new_window_is_opened([orig_window]))
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        self.find_element_wait(DzenLocators.BUTTON_MAIN_LOC)
        return self.get_text(DzenLocators.BUTTON_MAIN_LOC)
