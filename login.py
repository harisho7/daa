from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains




# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the target website
    driver.get("http://localhost:3000/test-login-cozmotec-dev")
    
#---------------- this field new;;;;--------------first------
    data = {
            "login_data": {  #--credentials--!
                "username": "ashutosh615singh@gmail.com",
                "password": "Ashu@1234"
            },
            "upcoming": {  #-------technical code--upcoming- "jaya" search-!
                "username": "Jaya"
            },
            "technical": [      #-------technical code--upcoming-!
                {
                    "observation": "This is an observation.",
                    "strength": "My strength is persistence.",
                    "areaOfDevelopment": "I need to improve time management."
                },
                {
                    "observation": "This is an observation TRAIN.",
                    "strength": "My strength is persistence CAR.",
                    "areaOfDevelopment": "I need to improve time management BUS."
                },
                {
                    "observation": "This is an observation TRUE.",
                    "strength": "My strength is persistence FAIL.",
                    "areaOfDevelopment": "I need to improve time management PASSS."
                },
                {
                    "observation": "This is an observation SUCCESS.",
                    "strength": "My strength is persistence BEHAVIOUR.",
                    "areaOfDevelopment": "I need to improve time THANKS."
                },
                {
                    "observation": "This is a PASSED.",
                    "strength": "My strength is PERFECT.",
                    "areaOfDevelopment": "I need to improve time CORRECTLY RUN."
                }
            ],
            "user_complete": {   #-------technical code--completed-!
                "username": "Aman"
            },
            "fields_eye": {     #-------technical code--completed --eye -field-!
                "overallFeedback": "Best"
            },
            "complete_eye": [
                {
                    "observation": "falco.",
                    "areaofDev": "I need bat.",
                    "strength": "My strength is persistence."
                },
                {
                    "observation": "This is an environment.",
                    "areaofDev": "I need apna collage.",
                    "strength": "My strength is so powerful."
                },
                {
                    "observation": "That's god.",
                    "areaofDev": "finally.",
                    "strength": "My behaviour is the best."
                },
                {
                    "observation": "This is a book.",
                    "areaofDev": "I have a car.",
                    "strength": "Cricket."
                },
                {
                    "observation": "It's a car.",
                    "areaofDev": "I fantastic.",
                    "strength": "My strength is clear."
                }
            ],
            "textarea_eye": {
                "areaforDev": "win",
                "recLearnInitiative": "Perfect"
            },
            "user_data": {
                "username": "Rekha",
                "my_list": [    #-------leadership code my_list
                    {
                        "observation": "This is an observation.",
                        "strength": "My strength is persistence.",
                        "areaOfDevelopment": "I need to improve time management."
                    },
                    {
                        "observation": "This is an observation fantastic.",
                        "strength": "My strength is persistence 2222222.",
                        "areaOfDevelopment": "I need to improve time management 3333333."
                    },
                    {
                        "observation": "This is an observation 111111.",
                        "strength": "My strength is persistence 44444.",
                        "areaOfDevelopment": "I need to improve time management PASSS."
                    },
                    {
                        "observation": "This is an observation SUCCESS.",
                        "strength": "My strength is persistence BEHAVIOUR.",
                        "areaOfDevelopment": "I need to improve time THANKS."
                    },
                    {
                        "observation": "This is a PASSED.",
                        "strength": "My strength is PERFECT.",
                        "areaOfDevelopment": "I need to improve time CORRECTLY 55555555."
                    }
                ]
            },
             "complete_my_list_eye": {
             "#username": "Fawaz report"
             },
            "fields": {
                "overallFeedback": "Welcome"
            }, 
        
            "eye": [
                {
                    "observation": "This is advanced.",
                    "areaofDev": "I need to improve skills.",
                    "strength": "My strength is so weak."
                },
                {
                    "observation": "This is an array.",
                    "areaofDev": "I need to improve my skills.",
                    "strength": "My strength is powerful."
                },
                {
                    "observation": "This is an observation thunga.",
                    "areaofDev": "I need to improve time management bussan.",
                    "strength": "My strength is persistence danger."
                },
                {
                    "observation": "This is an observation success.",
                    "areaofDev": "I need to improve time management perfect.",
                    "strength": "My strength is persistence drafting."
                },
                {
                    "observation": "This is selenium.",
                    "areaofDev": "I need to improve python skills.",
                    "strength": "My strength is hard correctly."
                }
            ],
            "textarea": {
                "areaforDev": "Fixed",
                "recLearnInitiative": "Correct"
            },

            "mindset_user": {
                "#username": "Radhika"
            },
             "report_partial": {
                 "username": "Shweta"
             },
             "report_complete":{
                 "username":"Aman"
             }


        }




            #------------------------
    
##-----------------------------



        #--#---------------Technical_part----- --start-------


    # Wait until the username field is present
    wait = WebDriverWait(driver, 20)  # Increase the wait time  
    
 # Find the username field and enter the username from the data dictionary
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))  # Adjust the selector as needed
    username_field.send_keys(data["login_data"]["username"])  # Using the username from the data dictionary
    print(username_field.text)

    # Find the password field and enter the password from the data dictionary
    password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))  # Adjust the selector as needed
    password_field.send_keys(data["login_data"]["password"])  # Using the password from the data dictionary
    print(password_field.text)
 # Submit the login form 
    password_field.submit()
#---------------------------

   

    # Increase wait time to handle slower loading elements
    technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/technical"]')))
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    
    # Click the link
    technical_link.click()
    time.sleep(3)




#----department

    link_report = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/report/rac-report') and .//p[text()='Report']]"))
    )

    # Click the element
    time.sleep(2)
    link_report.click()

    department_card = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "departmentCardId"))
    )

    # Click the div element
    department_card.click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

    #---fill strength part 1

#     button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthDepBtn_0"))
#     )

#     # Click the button
#     time.sleep(3)
#     button.click()
#     time.sleep(3)

#     textarea = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthInput"))
#     )

#     # Now clear the textarea and send the input
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("textarea filled by DB")

#     time.sleep(2)

#     close_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idCloseBtn"))
#     )
#     close_button.click()
#     print("closed")
#     time.sleep(3)


#     button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthDepBtn_0"))
#     )

#     # Click the button
#     time.sleep(3)
#     button.click()
#     time.sleep(3)

#     textarea = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthInput"))
#     )

#     # Now clear the textarea and send the input
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("database management system")

#     time.sleep(2)


#     save_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idSaveBtn"))
#     )
#     time.sleep(2)
#     save_button.click()
#     print("save changes successfully")
#     time.sleep(5)


# #--------------



# #---start weakness -----1

#     weakness_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idEmpWeaknessDepBtn_"))
#     )
#     time.sleep(3)
#     weakness_button.click()
#     print("click weakness")


#     textarea = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
#     )
#     textarea.clear()
#     textarea.send_keys("This is a sample weakness.")


#     close_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idCloseBtn"))
#     )
#     time.sleep(3)
#     close_button.click()
#     print("closed btn")
#     time.sleep(3)



#     weakness_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idEmpWeaknessDepBtn_"))
#     )
#     time.sleep(3)
#     weakness_button.click()
#     print("click weakness")


#     textarea = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
#     )
#     textarea.clear()
#     textarea.send_keys("This is a part of weakness.")
#     time.sleep(5)
#     save_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idSaveBtn"))
#     )
#     save_button.click()
#     print("save changeses weakness")
#     time.sleep(5)


    #--------2nd


    #---fill strength part 2

    # button = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.ID, "idStrengthDepBtn_1"))
    # )

    # # Click the button
    # time.sleep(3)
    # button.click()
    # time.sleep(3)

    # textarea = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    # )

    # # Now clear the textarea and send the input
    # textarea.clear()
    # time.sleep(3)
    # textarea.send_keys("textarea filled by DB 2")

    # time.sleep(2)

    # close_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, "idCloseBtn"))
    # )
    # close_button.click()
    # print("closed")
    # time.sleep(3)


    # button = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.ID, "idStrengthDepBtn_1"))
    # )

    # # Click the button
    # time.sleep(3)
    # button.click()
    # time.sleep(3)

    # textarea = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    # )

    # # Now clear the textarea and send the input
    # textarea.clear()
    # time.sleep(3)
    # textarea.send_keys("database management system ")

    # time.sleep(2)


    # save_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.ID, "idSaveBtn"))
    # )
    # time.sleep(2)
    # save_button.click()
    # print("save changes successfully 2")
    # time.sleep(5)


#--------------



#---start weakness -----2

    weakness_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idEmpWeaknessDepBtn_"))
    )
    time.sleep(3)
    weakness_button.click()
    print("click weakness")


    textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
    )
    textarea.clear()
    textarea.send_keys("This is a sample weakness.2")


    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idCloseBtn"))
    )
    time.sleep(3)
    close_button.click()
    print("closed btn")
    time.sleep(3)



    weakness_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idEmpWeaknessDepBtn_"))
    )
    time.sleep(3)
    weakness_button.click()
    print("click weakness")


    textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
    )
    textarea.clear()
    textarea.send_keys("This is a part of weakness.2")
    time.sleep(5)
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idSaveBtn"))
    )
    save_button.click()
    print("save changeses weakness 2")
    time.sleep(5)


#--report

    link_report = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/report/rac-report') and .//p[text()='Report']]"))
    )

    # Click the element
    time.sleep(2)
    link_report.click()

    n_level_card = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "nLevelCardId"))
    )
    n_level_card.click()
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, 5000);")  # Scroll by 5000px



    # driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(5)


    # driver.execute_script("window.scrollBy(0, -1000);")


#     #---fill strength part 1 

#     button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_0"))
#     )

#     # Click the button
#     time.sleep(3)
#     button.click()
#     time.sleep(3)

#     textarea = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthInput"))
#     )

#     # Now clear the textarea and send the input
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("textarea filled by DB")

#     time.sleep(2)

#     close_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idCloseBtn"))
#     )
#     close_button.click()
#     print("closed")
#     time.sleep(3)


#     button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_0"))
#     )

#     # Click the button
#     time.sleep(3)
#     button.click()
#     time.sleep(3)

#     textarea = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthInput"))
#     )

#     # Now clear the textarea and send the input
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("database management system")

#     time.sleep(2)


#     save_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idSaveBtn"))
#     )
#     time.sleep(2)
#     save_button.click()
#     print("save changes successfully")
#     time.sleep(5)


# #--------------



# #---start weakness -----1

#     weakness_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
#     )
#     time.sleep(3)
#     weakness_button.click()
#     print("click weakness")


#     textarea = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
#     )
#     textarea.clear()
#     textarea.send_keys("This is a sample weakness.")


#     close_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idCloseBtn"))
#     )
#     time.sleep(3)
#     close_button.click()
#     print("closed btn")
#     time.sleep(3)



#     weakness_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
#     )
#     time.sleep(3)
#     weakness_button.click()
#     print("click weakness")


#     textarea = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
#     )
#     textarea.clear()
#     textarea.send_keys("This is a part of weakness.")
#     time.sleep(5)
#     save_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idSaveBtn"))
#     )
#     save_button.click()
#     print("save changeses weakness")
#     time.sleep(5)



    #---fill strength part 2

#     button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_1"))
#     )

#     # Click the button
#     time.sleep(3)
#     button.click()
#     time.sleep(3)

#     textarea = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthInput"))
#     )

#     # Now clear the textarea and send the input
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("textarea filled by DB 2")

#     time.sleep(2)

#     close_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idCloseBtn"))
#     )
#     close_button.click()
#     print("closed")
#     time.sleep(3)


#     button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_1"))
#     )

#     # Click the button
#     time.sleep(3)
#     button.click()
#     time.sleep(3)

#     textarea = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthInput"))
#     )

#     # Now clear the textarea and send the input
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("database management system")

#     time.sleep(2)


#     save_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idSaveBtn"))
#     )
#     time.sleep(2)
#     save_button.click()
#     print("save changes successfully 2")
#     time.sleep(5)


# #--------------



# #---start weakness -----2

#     weakness_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
#     )
#     time.sleep(3)
#     weakness_button.click()
#     print("click weakness 2")


#     textarea = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
#     )
#     textarea.clear()
#     textarea.send_keys("This is a sample weakness.2")


#     close_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idCloseBtn"))
#     )
#     time.sleep(3)
#     close_button.click()
#     print("closed btn")
#     time.sleep(3)



#     weakness_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
#     )
#     time.sleep(3)
#     weakness_button.click()
#     print("click weakness 2")


#     textarea = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
#     )
#     textarea.clear()
#     textarea.send_keys("This is a part of weakness.")
#     time.sleep(5)
#     save_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idSaveBtn"))
#     )
#     save_button.click()
#     print("save changeses weakness 2")
#     time.sleep(5)




#     #---fill strength part 3

#     button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_2"))
#     )

#     # Click the button
#     time.sleep(3)
#     button.click()
#     time.sleep(3)

#     textarea = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthInput"))
#     )

#     # Now clear the textarea and send the input
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("textarea filled by DB 3")

#     time.sleep(2)

#     close_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idCloseBtn"))
#     )
#     close_button.click()
#     print("closed")
#     time.sleep(3)


#     button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_2"))
#     )

#     # Click the button
#     time.sleep(3)
#     button.click()
#     time.sleep(3)

#     textarea = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idStrengthInput"))
#     )

#     # Now clear the textarea and send the input
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("database management system")

#     time.sleep(2)


#     save_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idSaveBtn"))
#     )
#     time.sleep(2)
#     save_button.click()
#     print("save changes successfully 3")
#     time.sleep(5)


# #--------------



# #---start weakness -----3

#     weakness_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
#     )
#     time.sleep(3)
#     weakness_button.click()
#     print("click weakness 2")


#     textarea = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
#     )
#     textarea.clear()
#     textarea.send_keys("This is a sample weakness.3")


#     close_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idCloseBtn"))
#     )
#     time.sleep(3)
#     close_button.click()
#     print("closed btn")
#     time.sleep(3)



#     weakness_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
#     )
#     time.sleep(3)
#     weakness_button.click()
#     print("click weakness 3")


#     textarea = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
#     )
#     textarea.clear()
#     textarea.send_keys("This is a part of weakness.3")
#     time.sleep(5)
#     save_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "idSaveBtn"))
#     )
#     save_button.click()
#     print("save changeses weakness 3")
#     time.sleep(5)




    #---fill strength part 4

    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_3"))
    )

    # Click the button
    time.sleep(3)
    button.click()
    time.sleep(3)

    textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    )

    # Now clear the textarea and send the input
    textarea.clear()
    time.sleep(3)
    textarea.send_keys("textarea filled by DB 4")

    time.sleep(2)

    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idCloseBtn"))
    )
    close_button.click()
    print("closed")
    time.sleep(3)


    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_3"))
    )

    # Click the button
    time.sleep(3)
    button.click()
    time.sleep(3)

    textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    )

    # Now clear the textarea and send the input
    textarea.clear()
    time.sleep(3)
    textarea.send_keys("database management system")

    time.sleep(2)


    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idSaveBtn"))
    )
    time.sleep(2)
    save_button.click()
    print("save changes successfully 4")
    time.sleep(5)


#--------------



#---start weakness -----4

    weakness_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
    )
    time.sleep(3)
    weakness_button.click()
    print("click weakness 4")


    textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
    )
    textarea.clear()
    textarea.send_keys("This is a sample weakness.4")


    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idCloseBtn"))
    )
    time.sleep(3)
    close_button.click()
    print("closed btn")
    time.sleep(3)



    weakness_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
    )
    time.sleep(3)
    weakness_button.click()
    print("click weakness 4")


    textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
    )
    textarea.clear()
    textarea.send_keys("This is a part of weakness.3")
    time.sleep(5)
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idSaveBtn"))
    )
    save_button.click()
    print("save changeses weakness 4")
    time.sleep(5)

    #-----scroll up
    driver.execute_script("window.scrollBy(0, -5000);")


    #--report

    link_report = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/report/rac-report') and .//p[text()='Report']]"))
    )

    # Click the element
    time.sleep(2)
    link_report.click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "orgCardId"))
    ).click()
    time.sleep(3)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "downloadBtn"))
    ).click()
    time.sleep(10)



    # time.sleep(4)



    time.sleep(15)  # Wait for 15 seconds to view results
finally:
    # Close the browser
    driver.quit()  # Ensure the browser closes
