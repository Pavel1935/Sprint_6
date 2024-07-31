from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:


    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, MAIN_URL):
        return self.driver.get(MAIN_URL)

    def find_element_wait(self, locator, time=12):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))

    def scroll_to_element_located(self, locator):
        element = self.find_element_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_on_element(self, locator):
        return self.find_element_wait(locator).click()


    def format_locator(self, locator, num):
        method, loc = locator
        formatted_loc = loc.format(num=num)
        return (method, formatted_loc)

    def past_input_text(self, locator, text):
        element = self.find_element_wait(locator)
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_element_wait(locator).text



