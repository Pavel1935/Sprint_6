import allure
from pages.scooter_page import ScooterPage


class TestScooterButton:
    @allure.title('Проверяем если нажать на логотип «Самоката»,'
                  ' попадёшь на главную страницу «Самоката».')
    def test_order_steps(self, driver):
        scooter_page = ScooterPage(driver)
        scooter_page.click_scooter()
        result = scooter_page.click_scooter()
        assert result == 'Заказать'
