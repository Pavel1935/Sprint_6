import allure
from pages.dzen_page import DzenPage


class TestDzenPage:
    @allure.title('Проверяем, если нажать на логотип Яндекса, '
                  'в новом окне через редирект откроется главная страница Дзена.')
    def test_click_yandex_button(self, driver):
        dzen_page = DzenPage(driver)
        result = dzen_page.click_yandex_button()
        assert result == 'Новости'

