from selenium.webdriver.common.by import By

class Projects_Labels:
    def __init__(self, driver):
        self.driver = driver

    @property
    def Projects(self):
        return self.driver.find_element(By.XPATH, "//h1[normalize-space()='Projects']")
    
    @property
    def All(self):
        return self.driver.find_element(By.XPATH, "//p[normalize-space()='All']")
    
    @property
    def Completed(self):
        return self.driver.find_element(By.XPATH, "//p[normalize-space()='Completed']")
    
    @property
    def Ongoing(self):
        return self.driver.find_element(By.XPATH, "//h1[normalize-space()='Ongoing']")
    
    @property
    def Pending(self):
        return self.driver.find_element(By.XPATH, "//h1[normalize-space()='Pending']")
    
class Projects_View:
    def __init__(self, driver):
        self.driver = driver

    @property
    def BlocksView(self):
        return self.driver.find_element(By.XPATH, "//div[@class='grid grid-cols-1 lg:grid-cols-2 gap-6']")
    
    @property
    def ListView(self):
        return self.driver.find_element(By.XPATH, "//div[@class='bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden']")
    
class Projects_Buttons:
    def __init__(self, driver):
        self.driver = driver

    @property
    def BlocksView(self):
        return self.driver.find_element(By.XPATH, "//button[@title='Grid View']")
    
    @property
    def ListView(self):
        return self.driver.find_element(By.XPATH, "//button[@title='List View']")
    
    @property
    def NewProject(self):
        return self.driver.find_element(By.XPATH, "//button[@class='flex items-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-medium transition-colors']")
    
class Projects_NewProjectModal_Label:
    def __init__(self, driver):
        self.driver = driver

    @property
    def CreateNewProject(self):
        return self.driver.find_element(By.XPATH, "//h2[normalize-space()='Create New Project']")   

class Projects_NewProjectModal_Fields:
    def __init__(self, driver):
        self.driver = driver

    @property
    def SONo(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Enter 6-digit Sales Order No.']")   
    
    @property
    def Company(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Enter or select client company']")   
    
    @property
    def Project(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Enter project name']")   
    
    @property
    def AM(self):
        return self.driver.find_element(By.XPATH, "//select[@class='w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors border-gray-300']")   
    
    @property
    def SSCF(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Enter SSCF Reference No.']")   
    
    @property
    def StartDate(self):
        return self.driver.find_element(By.XPATH, "(//input[@type='date'])[1]")   
    
    @property
    def EndDate(self):
        return self.driver.find_element(By.XPATH, "(//input[@type='date'])[2]")   
    
    @property
    def Mandays(self):
        return self.driver.find_element(By.XPATH, "//input[@placeholder='Enter mandays']")   
    
    @property
    def CheckboxContainer(self):
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'border-gray-300')]")   
    
    @property
    def Checkbox(self):
        return self.driver.find_elements(By.XPATH, "(//input[@type='checkbox'])")   
    
    @property
    def AssignPMOs(self):
        return self.driver.find_element(By.XPATH, "//input[@class='mr-3 text-purple-600 focus:ring-purple-500']")   
    
    @property
    def AssignTM(self):
        return self.driver.find_element(By.XPATH, "//select[@id='tm-assignment']")   