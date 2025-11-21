from Elements.djangologin import *
from Elements.djangomain import *
from Elements.sidebar import *
import time

def test_login(driver): #Sign in to CHRONOS using django
    driver.get("https://chronos.mgenesis.com/admin/login/?next=/admin/login")
    driver.maximize_window()
    djangoLoginFields = DjangoLoginPageFields(driver)
    djangoLoginButtons = DjangoLoginPageButtons(driver)
    djangoMainButtons = DjangoMainButtons(driver)
    sbLabels = Sidebar_Labels(driver)
    sbButtons = Sidebar_Buttons(driver)

    #TASS Test Account Credentials
    djangoLoginFields.Email.send_keys('tass.chronos@yopmail.com')
    djangoLoginFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoLoginButtons.LogIn.click()
    time.sleep(1)
    djangoMainButtons.ViewSite.click()
    time.sleep(2)
    #Verify Sidebar by Role (TASS)
    assert 'Analytics' in sbLabels.Analytics.text
    assert 'Projects' in sbLabels.Projects.text
    assert 'Task Logs' in sbLabels.TaskLogs.text
    assert 'TrackPro Milestone' in sbLabels.TrackProMilestone.text
    assert 'User Management' in sbLabels.UserManagement.text
    assert 'Maintenance' in sbLabels.Maintenance.text
    sbButtons.Maintenance.click()
    assert 'Client Company' in sbLabels.ClientCompany.text
    assert 'Account Managers' in sbLabels.AccountManagers.text
    assert 'Solutions' in sbLabels.Solutions.text

def run_login(driver): #Sign in to CHRONOS using django
    test_login(driver)   