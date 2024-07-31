import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
class MainPage(BasePage):
    @allure.step('Нажимаем на стрелочку, открывается соответствующий текст')
    def click_on_question_and_get_answer(self, num):
        self.scroll_to_element_located(MainPageLocators.LAST_QUESTION_LOCATOR)
        self.click_on_element(MainPageLocators.COOKIE_LOCATOR)
        question_form_loc = self.format_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.click_on_element(question_form_loc)
        answer_form_loc = self.format_locator(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text(answer_form_loc)
