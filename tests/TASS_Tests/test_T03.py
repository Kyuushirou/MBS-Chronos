from Elements.sidebar import Sidebar_Buttons
from Elements.projects import *
from test_djangoLogin import run_login
import time
import random
from selenium.webdriver.support.ui import Select
from dateutil.relativedelta import relativedelta
import datetime

#For Generating Project Names
prefixes = [
    "Project", "App", "Website", "Platform", "System", "Tool", "Service", "Solution", "Initiative", "Campaign",
    "Program", "Framework", "API", "Infrastructure", "Automation", "Migration", "Upgrade", "Development", "Build"
]

adjectives = [
    "Alpha", "Beta", "Pre-launch", "Post-launch", "Redesign", "Revamp", "Update", "New", "Internal", "Final", 
    "Ongoing", "Prototype", "Experimental", "Complete", "Initial", "Long-term", "Strategic", "Advanced", "Critical", 
    "High-priority"
]

industries = [
    "CRM", "E-commerce", "Mobile", "Web", "Finance", "Healthcare", "Marketing", "Retail", "AI", "Machine Learning", 
    "Blockchain", "Data Analytics", "Cybersecurity", "Infrastructure", "Cloud", "Enterprise", "Business", "Automation", 
    "Technology", "IoT", "Education", "SaaS", "Gaming", "Media", "Energy", "Supply Chain"
]

# Function to generate a project name
def generate_project_name():
    # Randomly choose a prefix, adjective, and industry
    prefix = random.choice(prefixes)
    adjective = random.choice(adjectives)
    industry = random.choice(industries)
    
    # Optional: Add a year or random number to the name
    # year = datetime.now().year
    # number = random.randint(1, 999) {year}-{number}
    
    # Combine these elements into a realistic project name
    project_name = f"{prefix} {adjective} {industry}"
    return project_name

def test_T03_01(driver): #Navigate to Projects

    sbButtons = Sidebar_Buttons(driver)
    projectLabel = Projects_Labels(driver)
    
    #Login
    run_login(driver)

    sbButtons.Projects.click()
    assert driver.current_url == 'https://chronos.mgenesis.com/projects'
    assert projectLabel.Projects.is_displayed()

def test_T03_02(driver): #View Projects by Blocks/List

    projectView = Projects_View(driver)
    projectButtons = Projects_Buttons(driver)

    test_T03_01(driver)

    projectButtons.ListView.click()
    time.sleep(1.5)
    assert projectView.ListView.is_displayed()

    projectButtons.BlocksView.click()
    time.sleep(1.5)
    assert projectView.BlocksView.is_displayed()

def test_T03_03(driver): #Create Project with valid data

    projectButtons = Projects_Buttons(driver)
    NPmodalLabels = Projects_NewProjectModal_Label(driver)
    NPmodalFields = Projects_NewProjectModal_Fields(driver)

    test_T03_01(driver)

    projectButtons.NewProject.click()
    time.sleep(1)

    assert "Create New Project" in NPmodalLabels.CreateNewProject.text
    time.sleep (3)

    #SO Number -----------------------------------------------------------------------------------------------------------------------------------
    # Generate 6 random digits (unique digits)
    random_six_digits = random.sample(range(0, 9), 6)

    # Convert the list of digits to a string
    random_digits_str = ''.join(map(str, random_six_digits))

    # Send the random digits as a string
    NPmodalFields.SONo.send_keys(random_digits_str)

    #Client Company Name -------------------------------------------------------------------------------------------------------------------------

    NPmodalFields.Company.send_keys('a')
    dropdown_items = driver.find_elements(By.XPATH, "//ul[contains(@class, 'absolute')]//li")

    
    # Select a random option from the dropdown
    random_option = random.choice(dropdown_items)
    
    # Click the randomly selected option
    random_option.click()

    # Optional: Wait a bit to let the action complete
    time.sleep(0.5)
    

    #Project Name --------------------------------------------------------------------------------------------------------------------------------
    
    project_name = generate_project_name()
    NPmodalFields.Project.send_keys(project_name)
    time.sleep(0.5)

    #Account Manager -----------------------------------------------------------------------------------------------------------------------------

    AM = Select(NPmodalFields.AM) 
    AMOptions = AM.options 
    AMRandom = random.choice(AMOptions) 
    AM.select_by_visible_text(AMRandom.text) 

    #SSCF Reference No. --------------------------------------------------------------------------------------------------------------------------

    NPmodalFields.SSCF.send_keys(random_digits_str)

    #Start Date ----------------------------------------------------------------------------------------------------------------------------------

    # Generate a random start date (Year, Month, Day)
    s_year = random.randint(2023, 2028)  # Random year between 2023 and 2028
    s_month = random.randint(1, 12)      # Random month between 1 and 12
    s_day = random.randint(1, 28)        # Random day between 1 and 28 (this avoids problems with months that have less than 30 days)

    # Correct way to create a date object using datetime.date
    start_date = datetime.date(s_year, s_month, s_day)

    # Format the start date in MM-DD-YYYY format
    random_start_date = start_date.strftime('%m-%d-%Y')

    # Locate the Start Date input field and send the randomly generated date
    NPmodalFields.StartDate.send_keys(random_start_date)

    #End Date ------------------------------------------------------------------------------------------------------------------------------------

    # Calculate the end date (at least 6 months after the start date)
    end_date = start_date + relativedelta(months=6)

    # Format the end date in MM-DD-YYYY format
    random_end_date = end_date.strftime('%m-%d-%Y')

    # Locate the End Date input field and send the randomly generated date
    NPmodalFields.EndDate.send_keys(random_end_date)

    #SOW Mandays ---------------------------------------------------------------------------------------------------------------------------------

    # Generate 6 random digits (unique digits)
    random_three_digits = random.sample(range(0, 9), 3)

    # Convert the list of digits to a string
    random_three_digits_str = ''.join(map(str, random_three_digits))

    # Send the random digits as a string
    NPmodalFields.Mandays.send_keys(random_three_digits_str)

    #Solution ------------------------------------------------------------------------------------------------------------------------------------
    # List of checkbox indices. Always +1
    all_indices = list(range(1, 16))

    # Randomly select 2-5 checkboxes
    num_to_select = random.randint(2, 5)
    selected_indices = random.sample(all_indices, num_to_select)

    # Loop through the randomly selected indices
    for i in selected_indices:
        xpath = f"(//input[@type='checkbox'])[ {i} ]"
        
        checkbox = driver.find_element(By.XPATH, xpath)
        
        # Scroll checkbox into view
        driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
        time.sleep(0.3)  # small delay to allow scrolling

        # Click if not already selected
        if not checkbox.is_selected():
            checkbox.click()

    time.sleep(5)

    #Assign PMOs/TM -------------------------------------------------------------------------------------------------------------------------------

    # List of the two choices (PMO and TM)
    choices = ['PMO', 'TM']

    # Randomly select one of the choices
    selected_choice = random.choice(choices)

    # Check which choice was selected and perform actions accordingly
    if selected_choice == 'PMO':
        NPmodalFields.AssignPMOs.click()

    else:
        TM = Select(NPmodalFields.AssignTM) 
        TMOptions = TM.options 
        TMRandom = random.choice(TMOptions) 
        TM.select_by_visible_text(TMRandom.text) 

    
    time.sleep(3)