from selenium.webdriver.common.by import By

class DjangoAddCustomUserFields:
    def __init__(self, driver):
        self.driver = driver

    @property
    def Email(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_email']")

    @property
    def FullName(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_full_name']")
    
    @property
    def Role(self):
        return self.driver.find_element(By.XPATH, "//select[@id='id_role']")
    
    @property
    def Password(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_password1']")
    
    @property
    def PasswordConfirmation(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_password2']")

class DjangoAddCustomUserButtons:
    def __init__(self, driver):
        self.driver = driver

    @property
    def StaffCB(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_is_staff']")
    
    @property
    def SuperuserCB(self):
        return self.driver.find_element(By.XPATH, "//input[@id='id_is_superuser']")
    
    @property
    def Save(self):
        return self.driver.find_element(By.XPATH, "//input[@name='_save']")
    
    @property
    def SaveAndAdd(self):
        return self.driver.find_element(By.XPATH, "//input[@name='_addanother']")
    
    @property
    def SaveAndEdit(self):
        return self.driver.find_element(By.XPATH, "//input[@name='_continue']")