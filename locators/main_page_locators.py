from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки "Заказать"
    ORDER_BUTTON_TOP = [By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']"]
    ORDER_BUTTON_BOTTOM = [By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']"]

    # Логотипы
    LOGO_SCOOTER = [By.XPATH, "//a[contains(@class,'Header_LogoScooter')]"]
    LOGO_YANDEX = [By.XPATH, "//a[contains(@class,'Header_LogoYandex')]"]

    # Cookie-баннер
    COOKIE_BUTTON = [By.ID, "rcc-confirm-button"]

    # FAQ: заголовки
    FAQ_HEADING = "accordion__heading-{}"
    # FAQ: панели
    FAQ_PANEL = "accordion__panel-{}"