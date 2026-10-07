import pytest
import allure
from pages.main_page import MainPage
from data.faq_data import FaqData


@allure.feature("Вопросы о важном")
class TestFaq:

    @allure.title("Проверка ответа на вопрос FAQ №{index}")
    @pytest.mark.parametrize("index, expected_answer", FaqData.QUESTIONS_ANSWERS)
    def test_faq_answer(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.accept_cookies()
        main_page.click_faq_question(index)
        actual = main_page.get_faq_answer(index)
        assert actual == expected_answer, f"Ожидали: '{expected_answer}', получили: '{actual}'"