from selenium.webdriver.support.ui import Select
import time
from Elements.djangologin import *
from Elements.djangomain import *
from Elements.djangoaddcustomuser import *

def test_createDefaultUsers(driver): 
    driver.get("https://chronos.mgenesis.com/admin/login/?next=/admin/login")
    driver.maximize_window()
    djangoLoginFields = DjangoLoginPageFields(driver)
    djangoLoginButtons = DjangoLoginPageButtons(driver)
    djangoMainButtons = DjangoMainButtons(driver)
    djangoACUButtons = DjangoAddCustomUserButtons(driver)
    djangoACUFields = DjangoAddCustomUserFields(driver)

    djangoLoginFields.Email.send_keys('lovely@yopmail.com')
    djangoLoginFields.Password.send_keys('12345')
    djangoLoginButtons.LogIn.click()
    time.sleep(1.5)

    djangoMainButtons.AddCustomUsers.click()

    #TASS - Juan Dela Cruz
    djangoACUFields.Email.send_keys('tass.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Juan Dela Cruz')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Technical Admin Shared Services")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #PMO - Jose Mari Cruz
    djangoACUFields.Email.send_keys('pmo.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Jose Mari Cruz')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("PMO Admin")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #PM Dept. Head - Maria Kristina Lopez
    djangoACUFields.Email.send_keys('pmdh.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Maria Kristina Lopez')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("PM Dept. Head")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #TM Dept. Head - Ramon Isidro Dela Peña
    djangoACUFields.Email.send_keys('tmdh.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Ramon Isidro Dela Peña')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("TM Dept. Head")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #PM - Lorenzo Paolo Manalo
    djangoACUFields.Email.send_keys('pm.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Lorenzo Paolo Manalo')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Project Manager")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #TM - Ana Gabriela Navarro
    djangoACUFields.Email.send_keys('tm.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Ana Gabriela Navarro')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Technical Manager")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Marco Elijah Reyes
    djangoACUFields.Email.send_keys('engr.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Marco Elijah Reyes')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #EEM - Carmela Joyce Villanueva
    djangoACUFields.Email.send_keys('eem.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Carmela Joyce Villanueva')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Employee Experience Mgmt")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Executive - Jordan Alexis Ramos
    djangoACUFields.Email.send_keys('exec.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Jordan Alexis Ramos')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Executive")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)


    #Extras

    #PM - Juan Miguel Santos
    djangoACUFields.Email.send_keys('jmsantos.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Juan Miguel Santos')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Project Manager")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #PM - Patricia Anne Flores
    djangoACUFields.Email.send_keys('paflores.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Patricia Anne Flores')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Project Manager")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #PM - Maria Angelica Cruz
    djangoACUFields.Email.send_keys('macruz.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Juan Miguel Santos')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Project Manager")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #PM - Alejandro Gomez
    djangoACUFields.Email.send_keys('agomez.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Alejandro Gomez')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Project Manager")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #TM - Mark Anthony Reyes
    djangoACUFields.Email.send_keys('mareyes.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Mark Anthony Reyes')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Technical Manager")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #TM - Kristine Joy Ramos
    djangoACUFields.Email.send_keys('kjramos.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Kristine Joy Ramos')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Technical Manager")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #TM - Carlo Emmanuel Bautista
    djangoACUFields.Email.send_keys('cebautista.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Carlo Emmanuel Bautista')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Technical Manager")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #TM - Danielle Rose Torres
    djangoACUFields.Email.send_keys('drtorres.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Danielle Rose Torres')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Technical Manager")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Rafael Lorenzo Mendoza
    djangoACUFields.Email.send_keys('rlmendoza.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Rafael Lorenzo Mendoza')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Erika Mae Gutierrez
    djangoACUFields.Email.send_keys('emgutierrez.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Erika Mae Gutierrez')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Angelo Ramirez
    djangoACUFields.Email.send_keys('aramirez.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Angelo Ramirez')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Clarisse Nicole Aquino
    djangoACUFields.Email.send_keys('cnaquino.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Clarisse Nicole Aquino')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Paolo Dominic Garcia
    djangoACUFields.Email.send_keys('pdgarcia.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Paolo Dominic Garcia')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Janine Faith Morales
    djangoACUFields.Email.send_keys('jfmorales.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Janine Faith Morales')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Christian Paul Navarro
    djangoACUFields.Email.send_keys('cpnavarro.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Christian Paul Navarro')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Alyssa Marie Robles
    djangoACUFields.Email.send_keys('amrobles.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Alyssa Marie Robles')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Jerome Castillo
    djangoACUFields.Email.send_keys('jcastillo.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Jerome Castillo')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Shaira Mae Castillo
    djangoACUFields.Email.send_keys('smcastillo.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Shaira Mae Castillo')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Adrian Joseph Villanueva
    djangoACUFields.Email.send_keys('ajvillanueva.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Adrian Joseph Villanueva')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)

    #Engineer - Catherine Grace Lim
    djangoACUFields.Email.send_keys('cglim.chronos@yopmail.com')
    djangoACUFields.FullName.send_keys('Catherine Grace Lim')
    Role = Select(djangoACUFields.Role)
    Role.select_by_visible_text("Engineer")
    djangoACUFields.Password.send_keys('ChronosPa$$w0rd01')
    djangoACUFields.PasswordConfirmation.send_keys('ChronosPa$$w0rd01')
    djangoACUButtons.StaffCB.click()
    djangoACUButtons.SaveAndAdd.click()
    time.sleep(1)