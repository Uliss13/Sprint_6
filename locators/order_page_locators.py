from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Шаг 1: "Для кого самокат"
    NAME_INPUT = [By.XPATH, "//input[@placeholder='* Имя']"]
    SURNAME_INPUT = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS_INPUT = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO_INPUT = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    METRO_OPTION = "//div[@class='select-search__select']//div[text()='{}']"   # .format(metro)
    PHONE_INPUT = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]

    # Шаг 2: "Про аренду"
    DATE_INPUT = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    CALENDAR_DAY = "//div[contains(@class,'react-datepicker__day') and text()='{}']"   # .format(day)
    RENTAL_DROPDOWN = [By.XPATH, "//div[contains(@class,'Dropdown-control')]"]
    RENTAL_OPTION = "//div[contains(@class,'Dropdown-option') and text()='{}']"        # .format(text)
    COLOR_BLACK = [By.ID, "black"]
    COLOR_GREY = [By.ID, "grey"]
    COMMENT_INPUT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

    # Кнопки и модалки
    ORDER_BUTTON = [By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']"]
    CONFIRM_YES = [By.XPATH, "//button[text()='Да']"]
    SUCCESS_MODAL = [By.XPATH, "//div[contains(text(), 'Заказ оформлен')]"]