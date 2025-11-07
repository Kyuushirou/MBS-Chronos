from selenium.webdriver.common.by import By

class DjangoLoginPageFields:
    def __init__(self, driver):
        self.driver = driver

    @property
    def Email(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_username']")

    @property
    def Password(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_password']")

class DjangoLoginPageButtons:
    def __init__(self, driver):
        self.driver = driver

    @property
    def LogIn(self):
        return self.driver.find_element(By.XPATH, "//input[@value='Log in']")