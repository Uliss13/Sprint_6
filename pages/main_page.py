import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.urls import Urls


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main(self):
        self.open(Urls.BASE_URL)

    @allure.step("Принять cookie-баннер, если он есть")
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step("Нажать кнопку 'Заказать' по локатору: {locator}")
    def click_order_button(self, locator):
        self.scroll_to(locator)
        self.click(locator)

    @allure.step("Нажать на вопрос FAQ №{index}")
    def click_faq_question(self, index):
        locator = [By.ID, MainPageLocators.FAQ_HEADING.format(index)]
        self.click(locator)

    @allure.step("Получить ответ FAQ №{index}")
    def get_faq_answer(self, index):
        locator = [By.ID, MainPageLocators.FAQ_PANEL.format(index)]
        return self.get_text(locator)

    @allure.step("Нажать логотип Самоката")
    def click_logo_scooter(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Нажать логотип Яндекса")
    def click_logo_yandex(self):
        self.click(MainPageLocators.LOGO_YANDEX)

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        original = self.get_current_window()
        self.wait.until(lambda d: len(d.window_handles) > 1)
        for handle in self.get_window_handles():
            if handle != original:
                self.switch_to_window(handle)
                break