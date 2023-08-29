import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Read the Excel file
excel_file = 'Raw Data.xlsx'
data = pd.read_excel(excel_file)

# insert in username as password
username = "reynosod"
password = "dpassword1!"

# Opens up Browser
browser = webdriver.Firefox()

# opens webpage
browser.get('https://berea-sss.studentaccess.com/login.aspx')

# finds username and password fields
username_field = browser.find_element(By.ID, 'txtUsername')
username_field.send_keys(username)

password_field = browser.find_element(By.ID, 'txtPassword')
password_field.send_keys(password)

# finds the login button and clicks it
login_button = browser.find_element(By.ID, 'cmdLogin')
login_button.click()

#Finds the link by its text and clicks on it
find_student_link= browser.find_element(By.LINK_TEXT, 'Find Student')
find_student_link.click()

#Iterate through each SID value in the Excel file
for sid_value in data['SID']:


# Click on the dropdown input to open the list
dropdown_input = browser.find_element(By.ID, 'ddlOption1_Input')
dropdown_input.click()

# Find the option with text "SID" and click on it
sid_option = browser.find_element(By.XPATH, '//li[text()="SID"]')
ActionChains(browser).move_to_element(sid_option).click(sid_option).perform()

# Get the first SID value from the "SID" column
first_sid_value = data['SID'].iloc[0]

# Find the text box by its ID
txt_option_field = browser.find_element(By.ID, 'txtOption1')

# Clear any existing value in the text box
txt_option_field.clear()

# Input the first SID value into the text box
txt_option_field.send_keys(str(first_sid_value))

# finds the find students button and clicks it
login_button = browser.find_element(By.ID, 'cmdQuickSearch_input')
login_button.click()

#finds the students SID and clicks it


# Wait for the SID link to become clickable
wait = WebDriverWait(browser, 10) # Adjust the waiting time as needed
sid_link = wait.until(EC.element_to_be_clickable((By.ID, 'gridSearchResults_ctl00_ctl04_cmdSID')))

# Click the link
sid_link.click()

#Find the link by its href attribute and clicks it
perm_info_link = browser.find_element(By.XPATH, '//a[@href="permdata.aspx?wid=3093"]')
perm_info_link.click()

# Click on the dropdown input to open the list
dropdown_input = browser.find_element(By.ID, 'ddlCounselor')

# Create a Select object
select_dropdown = Select(dropdown_input)

# Select the option by its visible text
select_dropdown.select_by_visible_text('Tionne Forrest')

# finds the save button and clicks it
save_button = browser.find_element(By.ID, 'cmdSave')
save_button.click()