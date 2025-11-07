from selenium.webdriver.common.by import By

class DjangoMainButtons:
    def __init__(self, driver):
        self.driver = driver

    @property
    def AddCustomUsers(self):
        return self.driver.find_element(By.XPATH, "//a[@href='/admin/users/customuser/add/']")