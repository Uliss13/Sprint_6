import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент: {locator}")
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Кликнуть по элементу: {locator}")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввести '{text}' в поле: {locator}")
    def send_keys(self, locator, text):
        field = self.wait.until(EC.visibility_of_element_located(locator))
        field.clear()
        field.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Прокрутить к элементу: {locator}")
    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить список окон браузера")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Получить текущее окно")
    def get_current_window(self):
        return self.driver.current_window_handle

    @allure.step("Переключиться на окно: {handle}")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step("Ждать, пока URL содержит: {substring}")
    def wait_url_contains(self, substring):
        self.wait.until(EC.url_contains(substring))