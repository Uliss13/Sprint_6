import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data.urls import Urls


@allure.feature("Навигация по логотипам")
class TestNavigation:

    @allure.title("Логотип Самоката ведёт на главную страницу")
    def test_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.accept_cookies()
        main_page.click_order_button(MainPageLocators.ORDER_BUTTON_TOP)
        main_page.click_logo_scooter()
        current_url = main_page.get_current_url()
        assert current_url == Urls.BASE_URL, f"Ожидали главную, получили: {current_url}"

    @allure.title("Логотип Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.accept_cookies()
        main_page.click_logo_yandex()
        main_page.switch_to_new_window()
        main_page.wait_url_contains("dzen")
        assert "dzen" in main_page.get_current_url(), \
            f"Ожидали Дзен, получили: {main_page.get_current_url()}"