import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step("Заполнить шаг 1 формы заказа")
    def fill_first_form(self, data):
        self.send_keys(OrderPageLocators.NAME_INPUT, data["name"])
        self.send_keys(OrderPageLocators.SURNAME_INPUT, data["surname"])
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, data["address"])
        self._select_metro(data["metro"])
        self.send_keys(OrderPageLocators.PHONE_INPUT, data["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбрать станцию метро: {metro}")
    def _select_metro(self, metro):
        self.click(OrderPageLocators.METRO_INPUT)
        option = [By.XPATH, OrderPageLocators.METRO_OPTION.format(metro)]
        self.click(option)

    @allure.step("Заполнить шаг 2 формы заказа")
    def fill_second_form(self, data):
        self._select_date(data["date"])
        self._select_rental(data["rental_period"])
        self._select_color(data["color"])
        self.send_keys(OrderPageLocators.COMMENT_INPUT, data["comment"])

    @allure.step("Выбрать дату: {day}")
    def _select_date(self, day):
        self.click(OrderPageLocators.DATE_INPUT)
        day_locator = [By.XPATH, OrderPageLocators.CALENDAR_DAY.format(day)]
        self.click(day_locator)

    @allure.step("Выбрать срок аренды: {period}")
    def _select_rental(self, period):
        self.click(OrderPageLocators.RENTAL_DROPDOWN)
        option = [By.XPATH, OrderPageLocators.RENTAL_OPTION.format(period)]
        self.click(option)

    @allure.step("Выбрать цвет: {color}")
    def _select_color(self, color):
        locator = OrderPageLocators.COLOR_BLACK if color == "black" else OrderPageLocators.COLOR_GREY
        self.click(locator)

    @allure.step("Нажать 'Заказать' на шаге 2")
    def click_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Подтвердить заказ кнопкой 'Да'")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_YES)

    @allure.step("Получить текст модалки об успешном заказе")
    def get_success_text(self):
        return self.get_text(OrderPageLocators.SUCCESS_MODAL)