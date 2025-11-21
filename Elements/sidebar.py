from selenium.webdriver.common.by import By

class Sidebar_Labels:
    def __init__(self, driver):
        self.driver = driver

    @property
    def Chronos(self):
        return self.driver.find_element(By.XPATH, "//h1[normalize-space()='Chronos']")
    
    @property
    def ChronosLogo(self):
        return self.driver.find_element(By.XPATH, "//div[@class='w-8 h-8 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center']")
    
    @property
    def UserName(self):
        return self.driver.find_element(By.XPATH, "//p[@class='font-medium text-sm']")
    
    @property
    def UserRole(self):
        return self.driver.find_element(By.XPATH, "//p[@class='text-xs text-slate-400']")
    
    @property
    def UserPhoto(self):
        return self.driver.find_element(By.XPATH, "//div[@class='w-10 h-10 bg-gradient-to-br from-green-400 to-blue-500 rounded-full flex items-center justify-center']")
    
    @property
    def Analytics(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Analytics']")
    
    @property
    def Projects(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Projects']")
    
    @property
    def PMAssignments(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='PM Assignments']")
    
    @property
    def TaskManagement(self):
        return self.driver.find_element(By.XPATH, "//span[@class='text-sm flex-1 text-left']")
    
    @property
    def Tasks(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Tasks']")
    
    @property
    def TaskNames(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Task Names']")
    
    @property
    def TaskExecution(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Task Execution']")
    
    @property
    def TaskLogs(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Task Logs']")
    
    @property
    def TimesheetApproval(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Timesheet Approval']")
    
    @property
    def Timesheet(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Timesheet']")
    
    @property
    def EngineerSalaryLevels(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Engineer Salary Levels']")
    
    @property
    def SalaryManagement(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Salary Management']")
    
    @property
    def HolidayCalendar(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Holiday Calendar']")
    
    @property
    def TrackProMilestone(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='TrackPro Milestone']")
    
    @property
    def UserManagement(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='User Management']")
    
    @property
    def Maintenance(self):
        return self.driver.find_element(By.XPATH, "//span[@class='text-sm flex-1 text-left']")
    
    @property
    def ClientCompany(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Client Company']")
    
    @property
    def AccountManagers(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Account Managers']")
    
    @property
    def Solutions(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Solutions']")
    
class Sidebar_Buttons:
    def __init__(self, driver):
        self.driver = driver

    @property
    def Chronos(self):
        return self.driver.find_element(By.XPATH, "//h1[normalize-space()='Chronos']")
    
    @property
    def ChronosLogo(self):
        return self.driver.find_element(By.XPATH, "//div[@class='w-8 h-8 bg-gradient-to-br from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center']")
    
    @property
    def UserName(self):
        return self.driver.find_element(By.XPATH, "//p[@class='font-medium text-sm']")
    
    @property
    def UserRole(self):
        return self.driver.find_element(By.XPATH, "//p[@class='text-xs text-slate-400']")
    
    @property
    def UserPhoto(self):
        return self.driver.find_element(By.XPATH, "//div[@class='w-10 h-10 bg-gradient-to-br from-green-400 to-blue-500 rounded-full flex items-center justify-center']")
    
    @property
    def Analytics(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Analytics']")
    
    @property
    def Projects(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Projects']")
    
    @property
    def PMAssignments(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='PM Assignments']")
    
    @property
    def TaskManagement(self):
        return self.driver.find_element(By.XPATH, "//span[@class='text-sm flex-1 text-left']")
    
    @property
    def Tasks(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Tasks']")
    
    @property
    def TaskNames(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Task Names']")
    
    @property
    def TaskExecution(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Task Execution']")
    
    @property
    def TaskLogs(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Task Logs']")
    
    @property
    def TimesheetApproval(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Timesheet Approval']")
    
    @property
    def Timesheet(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Timesheet']")
    
    @property
    def EngineerSalaryLevels(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Engineer Salary Levels']")
    
    @property
    def SalaryManagement(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Salary Management']")
    
    @property
    def HolidayCalendar(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Holiday Calendar']")
    
    @property
    def TrackProMilestone(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='TrackPro Milestone']")
    
    @property
    def UserManagement(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='User Management']")
    
    @property
    def Maintenance(self):
        return self.driver.find_element(By.XPATH, "//span[@class='text-sm flex-1 text-left']")
    
    @property
    def ClientCompany(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Client Company']")
    
    @property
    def AccountManagers(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Account Managers']")
    
    @property
    def Solutions(self):
        return self.driver.find_element(By.XPATH, "//span[normalize-space()='Solutions']")