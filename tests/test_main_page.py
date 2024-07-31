import allure
import pytest
from conftest import driver
from constants import ANSWER
from pages.main_page import MainPage



class TestMainPage:
    @pytest.mark.parametrize(
        "q_num, expected_result",
        [
         ("0", ANSWER[0]),
         ("1", ANSWER[1]),
         ("2", ANSWER[2]),
         ("3", ANSWER[3]),
         ("4", ANSWER[4]),
         ("5", ANSWER[5]),
         ("6", ANSWER[6]),
         ("7", ANSWER[7])
        ])
    @allure.title('Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def test_question_and_answer(self, driver, q_num, expected_result):
        main_page = MainPage(driver)
        result = main_page.click_on_question_and_get_answer(q_num)
        assert result == expected_result