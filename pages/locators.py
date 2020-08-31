from selenium.webdriver.common.by import By


class MainPageLocators:
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
	LOGIN_URL = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"  # локаль нужно выносить в отдельный список и подставлять в урл
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
