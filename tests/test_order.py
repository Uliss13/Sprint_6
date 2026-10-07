import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from data.order_data import OrderData


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Позитивный сценарий заказа")
    @pytest.mark.parametrize("data", [OrderData.DATASET_1, OrderData.DATASET_2], ids=["dataset_1", "dataset_2"])
    @pytest.mark.parametrize("order_button", [MainPageLocators.ORDER_BUTTON_TOP, MainPageLocators.ORDER_BUTTON_BOTTOM],
                             ids=["top", "bottom"])
    def test_order_success(self, driver, data, order_button):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.accept_cookies()
        main_page.click_order_button(order_button)

        order_page = OrderPage(driver)
        order_page.fill_first_form(data)
        order_page.fill_second_form(data)
        order_page.click_order()
        order_page.confirm_order()

        success_text = order_page.get_success_text()
        assert "Заказ оформлен" in success_text, f"Модалка успеха не появилась. Текст: {success_text}"