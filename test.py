from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get("https://succession-planning.onrender.com/")

# driver.set_context("chrome")
# driver.maximize_window()
# win = driver.find_element(By.TAG_NAME, "html")
# win.send_keys(Keys.CONTROL + '-')
# win.send_keys(Keys.CONTROL + '-')
# driver.set_context("content")
email = 'john.doe@example.com'
password = 'password123'

admin_email = 'bob.brown@lums.edu.pk'
admin_password = 'password123'


def login(EMAIL, PASSWORD):
    email = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[1]/input")
    email.send_keys(EMAIL)

    password = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[2]/input")
    password.send_keys(PASSWORD)

    print('Select security image')
    input()

    login_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[4]/button")
    login_button.click()

    print('Logging in ....')

    sleep(5)

def update_profile():
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/div[4]/a")))
    settings = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/div[4]/a")
    settings.click()

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/aside/button")))
    edit_profile_btn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/aside/button')
    edit_profile_btn.click()

    about_me_edit = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/main/section/div[2]/div/p[1]/h3/svg')

def update_password_logged_in(email, current_password, new_password):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/div[4]/a")))
    settings = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[2]/div[4]/a")
    settings.click()

    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/main/section/div[1]/button[2]")))
    change_pwd_btn = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/main/section/div[1]/button[2]")
    change_pwd_btn.click()

    current_password_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/main/section/div[2]/form/div[1]/div/input')
    current_password_input.send_keys(current_password)

    new_password_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/main/section/div[2]/form/div[2]/div/input')
    new_password_input.send_keys(new_password)

    confirm_password_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/main/section/div[2]/form/div[4]/div/input')
    confirm_password_input.send_keys(new_password)

    reset_btn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/main/section/div[2]/form/div[5]/button')
    reset_btn.click()

    sleep(2)

    log_out_btn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[1]/button')
    log_out_btn.click()

    login(email, password)

    driver.get("https://succession-planning.onrender.com/")

    login(email, new_password)

def update_password_without_login(empID, security_answer, email, new_password):
    forgot_password_link = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div[6]/a')
    forgot_password_link.click()

    employee_id_input = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[1]/input')
    employee_id_input.send_keys(empID)

    search_btn = driver.find_element(By.CSS_SELECTOR, 'body > div > div > form > div:nth-child(1) > span > svg')
    search_btn.click()

    security_ans_input = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[3]/input')
    security_ans_input.send_keys(security_answer)

    print('Select security image')
    input()

    next_btn = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[5]/button')
    next_btn.click()

    sleep(3)

    new_paswword_input = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[1]/input')
    new_paswword_input.send_keys(new_password)

    confirm_password_input = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[3]/input')
    confirm_password_input.send_keys(new_password)

    reset_btn = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[4]/button')
    reset_btn.click()

    sleep(2)

    login(email, new_password)

def block_account(EMAIL, PASSWORD):
    email = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[1]/input")
    email.send_keys(EMAIL)

    password = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[2]/input")
    password.send_keys(PASSWORD)

    for i in range(3):
        print('Select security image')
        input()

        login_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[4]/button")
        login_button.click()

        print('Logging in ....')
    
    print('Account blocked successfully')


def search_employee(SEARCH_ID):
        WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[2]/div[3]/div[1]/div/input")))
        search_box = driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[3]/div[1]/div/input")

        search_box.send_keys(SEARCH_ID)
        sleep(5)

def filter_position(POSITION_ID):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[2]/div[3]/div[1]/div/input")))
    filter_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[3]/div[1]/button[1]")
    filter_button.click()
    positions_button = Select(driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div/select"))
    positions_button.select_by_value(POSITION_ID)
    done_button = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div/button")
    done_button.click()
    sleep(3)

def filter_threshold(THRESHOLD_VALUE):
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[2]/div[3]/div[1]/div/input")))
    filter_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[2]/div[3]/div[1]/button[1]")
    filter_button.click()
    threshold_input = (driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div/input"))
    threshold_input.clear()
    threshold_input.send_keys(THRESHOLD_VALUE)
    done_button = driver.find_element(By.XPATH,"/html/body/div/div[2]/div[2]/div/button")
    done_button.click()
    sleep(3)


def view_high_potential():
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/label")))
    high_potential_button = driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/label")
    high_potential_button.click()
    sleep(3)

def view_at_risk():
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#root > div.overlay > div > div.contentAdminDash > div.employeeFunctions > div:nth-child(3) > div.countAndView > div.iconAndView > label")))
    high_potential_button = driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[2]/label")
    high_potential_button.click()
    sleep(3)


def search_for_all_filtered(): #search for all filtered positions
    login(admin_email, admin_password)
    search_employee(1021)

def search_for_managerial(): #Filter for managerial positions
    login(admin_email, admin_password)
    filter_position("P004")


def search_for_IT(): #filter and search for IT positions
    login(admin_email, admin_password)
    filter_position("P010")
    search_employee(1021)

def set_threshold_and_high_potential(): #set threshold to 0 and view high potential
    login(admin_email, admin_password)
    filter_threshold(0)
    view_high_potential()

def set_threshold_and_low_potential(): #set threshold to 1 and view employees at risk
    login(admin_email, admin_password)
    filter_threshold(1)
    view_at_risk()

def set_threshold_low_potential_and_search(): #set threshold to 1, view employees at risk, and search
    login(admin_email, admin_password)
    filter_threshold(0)
    view_at_risk()
    search_employee(1003)

def set_threshold_high_potential_and_search(): #set threshold to 1, view employees at risk, and search
    login(admin_email, admin_password)
    filter_threshold(0)
    view_high_potential()
    search_employee(1003)


def signup_already_registered_employee():

    driver.get("https://succession-planning.onrender.com/signup")

    employee_id = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[1]/input')
    employee_id.send_keys('1001')

    search_employee = driver.find_element(By.CSS_SELECTOR, 'div.signup-input-group:nth-child(1) > svg:nth-child(2)')
    search_employee.click()

    sleep(3)

    email = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[3]/input')
    email.send_keys('shera@lums.edu.pk')

    password = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[4]/input')
    password.send_keys('Abc1234.')

    s_img = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[6]/div[1]/img[3]')
    s_img.click()

    next_btn = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[7]/button') 
    next_btn.click()


def login_valid_credientials():

    login('batool@lums.edu.pk', 'Abc1234.')

def login_invalid_security_image():

    login('batool@lums.edu.pk', 'Abc1234.')

def login_invalid_password():

    login('batool@lums.edu.pk', 'password1234')

def login_non_existant_user():

    login('shera@lums.edu.pk', 'password1234')

def signup_new_user():

    driver.get("https://succession-planning.onrender.com/signup")
    employee_id = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[1]/input')
    employee_id.send_keys('1033')

    search_employee = driver.find_element(By.CSS_SELECTOR, 'div.signup-input-group:nth-child(1) > svg:nth-child(2)')
    search_employee.click()

    sleep(3)

    email = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[3]/input')
    email.send_keys('iqbal_sheikh@lums.edu.pk')

    password = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[4]/input')
    password.send_keys('Abc1234.')

    print("Enter Security Images")
    input()

    next_btn = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[7]/button') 
    next_btn.click()

    sleep(1)

    phone = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[1]/input')
    phone.send_keys('03004542307')

    dob = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[2]/input')
    dob.send_keys('2003-02-19')

    education = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[3]/select')
    education_select = Select(education)
    education_select.select_by_value('Bachelors')

    driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[5]/div/button').click()
    driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[6]/div/button').click()

    proceed_btn = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[7]/button')
    proceed_btn.click()

    sleep(1)

    seq_quest = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[1]/select')
    seq_quest_select = Select(seq_quest)
    seq_quest_select.select_by_value('What is your mother\'s maiden name?')

    seq_answer = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[2]/input')
    seq_answer.send_keys('Batool')

    register_btn = driver.find_element(By.XPATH, '/html/body/div/body/div/div/form/div[3]/button')
    register_btn.click()

    sleep(1)

    driver.get('https://succession-planning.onrender.com/')

    login('iqbal_sheikh@lums.edu.pk', 'Abc1234.')



# login_valid_credientials()
# login_invalid_security_image()
# login_invalid_password()
# login_non_existant_user()
# signup_new_user()
# block_account(email,password)
# update_password_logged_in(email,password,"sarimbhaiking")
# update_password_without_login(1012,"Batool","batool@lums.edu.pk","sarimbhaiking")
# update_profile()
# signup_already_registered_employee()
# search_for_all_filtered()
# search_for_managerial()
# search_for_IT()
# set_threshold_and_high_potential()
# set_threshold_and_low_potential()
# set_threshold_low_potential_and_search()
# set_threshold_high_potential_and_search()







