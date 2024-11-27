from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # # Open the target website
    # driver.get("https://portal.iconaccounting.ie/")

    # email_input = driver.find_element(By.ID, "id_email")

    # # Type "hello" into the email input field
    # email_input.send_keys("harish@gmail.com")
    # time.sleep(3)

    #     # Locate the password input field using its ID (or other attributes if needed)
    # password_input = driver.find_element(By.ID, "id_password")

    # # Type "pass" into the password input field
    # password_input.send_keys("harish12345")

    #     # Locate the submit button using its class (or other attributes if needed)
    # submit_button = driver.find_element(By.CLASS_NAME, "btn-green")

    # # Click the submit button
    # submit_button.click()

   
 
#---------------- this field new;;;;--------------first------
 

        #-------------second------------
    data = {
        "login_data": {
            "username": "ashutosh615singh@gmail.com",
            "password": "Ashu@1234"
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
        "upcoming": {
            "username": "Jaya"
        },
        "technical": [      #-------technical code--upcomming-!
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
        }   #-------technical code--completed- eye-field--!
    }

##-----------------------------

    
    time.sleep(15)  # Wait for 15 seconds to view results
finally:
    # Close the browser
    driver.quit()  # Ensure the browser closes
