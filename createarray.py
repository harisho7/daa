from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the target website
    driver.get("http://localhost:3000/test-login-cozmotec-dev")
    
    
#---------------- this field new;;;;--------------first------
 

#-------------second------------


        #-------------thats a Json--------
    data = {
        "login_data": {
            "username": "ashutosh615singh@gmail.com",
            "password": "Ashu@1234"
        },
        "user_data": {
            "username": "Rekha",  
            "my_list": [
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
                    "observation": "This is an PASSED.",
                    "strength": "My strength is PERFECT.",
                    "areaOfDevelopment": "I need to improve time CORRECTLY 55555555."
                }
            ]
        },
        "fields": {
            "overallFeedback": "Welcome"  # Field name as key and value to be filled
        },
        "eye": [  # Added the eye list here
            {
                "observation": "This is advanced",
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
            "areaforDev": "Fixed",  # Added areaforDev field
            "recLearnInitiative": "Correct"  # Added recLearnInitiative field
        }
    }


##-----------------------------



#-----------------


    # Wait until the username field is present
    wait = WebDriverWait(driver, 20)  # Increase the wait time  
    
 # Find the username field and enter the username from the data dictionary
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))  # Adjust the selector as needed
    username_field.send_keys(data["login_data"]["username"])  # Using the username from the data dictionary
    
    # Find the password field and enter the password from the data dictionary
    password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))  # Adjust the selector as needed
    password_field.send_keys(data["login_data"]["password"])  # Using the password from the data dictionary
 # Submit the login form 
    password_field.submit()





#---------------------------

##click leadership

 # Increase wait time to handle slower loading elements
    time.sleep(5)
    leadership_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/leadership"]')))
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", leadership_link)
    
    # Click the link
    time.sleep(5)
    leadership_link.click()

    # Click the button -------------------filter appy---------upcoming

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'collapseFilter'))  # Using ID directly
    )
    time.sleep(2)
    button.click()

        # Wait for the dropdown to be clickable and click it to expand
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'asserNameFilter_ID'))
    )
    time.sleep(2)
    dropdown.click()

    # Wait for the "Ashutosh" option to be clickable and click it
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='Ashutosh']"))
    )
    time.sleep(3)
    option.click()



        # Wait for the dropdown to be clickable and click it to expand
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'nomPosIdFilter_ID'))
    )
    time.sleep(3)
    dropdown.click()  # Click the dropdown to show options

    # Wait for the "Data Scientist II" option to be clickable and click it
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='Data Scientist II']"))
    )
    time.sleep(3)
    option.click()  # Click the "Data Scientist II" option

    # Wait for the button to be clickable and click it
    apply_filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'applyFilterId'))
    )
    time.sleep(3)
    apply_filter_button.click()  # Click the "Apply Filters" button


#---------------------------------------------#
  


 # Find the username field and enter email-------------json
    username = data["user_data"]["username"]
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys(username)  # Use the username from the data
    time.sleep(4)
    # Optional: keep the window open for a few seconds to view results-------------------
 # Wait for the button with class 'btn' and 'p-1' to be clickable
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.p-1")))
    
    # Scroll the button into view (if necessary)
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    
    # Click the button
    time.sleep(3)
    button.click()

    time.sleep(4)


       # Locate the anchor tag with the class 'lb-close'
    close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "lb-close")))
    
    # Scroll the element into view if necessary
    driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
    
    # Click the anchor element
    time.sleep(4)
    close_button.click()

#--------------------create arrray--------------#
# Import necessary modules

    # Set up WebDriverWait
    wait = WebDriverWait(driver, 10)
        # Iterate through each section in 'my_list'
    for i, section_data in enumerate(data["user_data"]["my_list"]):
        try:
            print(f"Processing section {i + 1}")

            # Fill in the fields for the current section
            for key, value in section_data.items():
                # Locate the textarea using its NAME attribute
                textarea = wait.until(EC.presence_of_element_located((By.NAME, key)))

                # Scroll the textarea into view if necessary
                driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

                # Clear the field and input the value
                textarea.clear()
                time.sleep(2)  # Optional wait before sending keys
                textarea.send_keys(value)

            # Handle radio button and Save & Next button, except for the last section
            if i < len(data["user_data"]["my_list"]) - 1:  # Check if not the last section
                try:
                    # Locate and click the radio button (adjust ID if needed)
                    radio_button = wait.until(EC.element_to_be_clickable((By.ID, "score3")))  # Change ID as necessary
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button)
                    time.sleep(2)  # Wait for the radio button to be in view
                    radio_button.click()

                    # Locate and click the Save & Next button
                    save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
                    time.sleep(2)  # Wait for the button to be in view
                    save_next_button.click()

                    # Wait for the next section to load
                    time.sleep(4)
                except Exception as e:
                    print(f"Error during radio button or save action for section {i + 1}: {e}")
            else:
                print(f"Last section reached, skipping Save & Next button for section {i + 1}")

        except Exception as e:
            print(f"Error processing section {i + 1}: {e}")

#------------------
   

#----------------


 # Increase wait time to handle slower loading elements
    
    try:
        # Wait for the element to be clickable
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.nav-link.py-75.iconSpacer.active"))
        )
        
        # Scroll the element into view if necessary
        driver.execute_script("arguments[0].scrollIntoView(true);", link)

        # Click the link
        link.click()

        # Optional: wait for a few seconds to observe the result
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")
    #click complete ------leadership

    completed_button = driver.find_element(By.XPATH, "//div[@id='complete']//a[contains(text(),'Completed')]")

    # Click the "Completed" link
    time.sleep(3)
    completed_button.click()



    # Click the button------apply filter
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'collapseFilter'))  # Using ID directly
    )
    time.sleep(2)
    button.click()

        # Wait for the dropdown to be clickable and click it to expand
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'asserNameFilter_ID'))
    )
    time.sleep(2)
    dropdown.click()

    # Wait for the "Ashutosh" option to be clickable and click it
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='Ashutosh']"))
    )
    time.sleep(3)
    option.click()



        # Wait for the dropdown to be clickable and click it to expand
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'nomPosIdFilter_ID'))
    )
    time.sleep(3)
    dropdown.click()  # Click the dropdown to show options

    # Wait for the "Data Scientist II" option to be clickable and click it
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='Data Scientist II']"))
    )
    time.sleep(3)
    option.click()  # Click the "Data Scientist II" option

    # Wait for the button to be clickable and click it
    apply_filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'applyFilterId'))
    )
    time.sleep(3)
    apply_filter_button.click()  # Click the "Apply Filters" button

#-----username-------
    time.sleep(2)
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("Tara")
    time.sleep(4)




        # Locate the button using XPath-----eye------
    button = driver.find_element(By.XPATH, "//button[@data-bs-toggle='offcanvas' and @data-bs-target='#offcanvas1']")

    # Click the button
    time.sleep(3)
    button.click()

    #--------------json---start 

    try:
        # Locate the textarea using its ID
        textarea = wait.until(EC.presence_of_element_located((By.ID, "overallFeedback")))

        # Clear any existing text in the textarea (optional)
        textarea.clear()

        # Optional wait to ensure the field is ready for input
        time.sleep(3)

        # Fill the textarea with the value from the data structure
        textarea.send_keys(data["fields"]["overallFeedback"])  # Using the value associated with the key

    except Exception as e:
        print(f"Error filling overall feedback: {e}")

        #-------------fill eye form-----------#


    for index, section_data in enumerate(data["eye"]):
        try:
            print(f"Processing eye section {index + 1}...")

            # Loop through each key-value pair in the current section's dictionary
            for key, value in section_data.items():
                # Build an XPath to locate the textarea for the current section by index
                textarea_xpath = f"(//textarea[@id='{key}'])[{index + 1}]"

                textarea = wait.until(EC.presence_of_element_located((By.XPATH, textarea_xpath)))

                # Scroll the textarea into view if necessary
                driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

                # Clear the field and input the value
                time.sleep(3)
                textarea.clear()
                time.sleep(4)  # Optional wait
                textarea.send_keys(value)
                time.sleep(3)

        except Exception as e:
            print(f"Error processing eye section {index + 1}: {e}")



 # ----------------=--------Locate the <textarea> using XPath


    # Locate the first <textarea> and fill it with the 'areaforDev' value
    textarea_areaforDev = driver.find_element(By.XPATH, "//textarea[@name='areaforDev']")
    textarea_areaforDev.clear()  # Clear the textarea
    time.sleep(3)
    textarea_areaforDev.send_keys(data["textarea"]["areaforDev"])  # Fill with value from JSON

 

    # Locate the second <textarea> and fill it with the 'recLearnInitiative' value
    textarea_recLearnInitiative = driver.find_element(By.XPATH, "//textarea[@name='recLearnInitiative']")
    textarea_recLearnInitiative.clear()  # Clear the textarea
    time.sleep(3)
    textarea_recLearnInitiative.send_keys(data["textarea"]["recLearnInitiative"])  # Fill with value from JSON


# #                              # --------------------------------leadership completed code with submit code
   

 # Locate the button using XPath
    submit_button = driver.find_element(By.XPATH, "//button[@id='submitResponse']")

    # Click the submit button
    time.sleep(3)
    submit_button.click()


    # Wait for the div with class 'dmx-notify-message' to appear and capture the text------print success message
    try:
        # Wait until the div with the class 'dmx-notify-message' becomes visible
        response_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
        )
        
        # Print the message inside the div
        print("Message:", response_element.text)

    except Exception as e:
        print(f"Error occurred: {e}")


                                                                        ##---leadership complet label close successfully----;;;

   # Locate the button using XPath close button completed
    time.sleep(10)
    button = driver.find_element(By.XPATH, "//button[@type='button' and @class='btn-close text-reset' and @aria-label='Close']")
    # Click the button
    time.sleep(3)
    button.click()

##------------------------------------END------------------#




    # Fill in the textarea for areaOfDevelopment in textarea_eye
    textarea_area_of_dev = driver.find_element(By.XPATH, "//textarea[@name='areaforDev']")
    textarea_area_of_dev.clear()
    time.sleep(1)  # Shorter wait time for better performance
    textarea_area_of_dev.send_keys(data["textarea"]["areaforDev"])

    # Fill in the textarea for recLearnInitiative in textarea_eye
    textarea_rec_learn_initiative = driver.find_element(By.XPATH, "//textarea[@name='recLearnInitiative']")
    textarea_rec_learn_initiative.clear()
    time.sleep(1)  # Shorter wait time for better performance
    textarea_rec_learn_initiative.send_keys(data["textarea"]["recLearnInitiative"])





# #                              # --------------------------------leadership completed code with submit code
   

 # Locate the button using XPath
    submit_button = driver.find_element(By.XPATH, "//button[@id='submitResponse']")

    # Click the submit button
    time.sleep(3)
    submit_button.click()



    # Wait for the div with class 'dmx-notify-message' to appear and capture the text------print success message
    try:
        # Wait until the div with the class 'dmx-notify-message' becomes visible
        response_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
        )
        
        # Print the message inside the div
        print("Message:", response_element.text)

    except Exception as e:
        print(f"Error occurred: {e}")


                                                                        ##---leadership complet label close successfully----;;;

   # Locate the button using XPath close button completed
    time.sleep(10)
    button = driver.find_element(By.XPATH, "//button[@type='button' and @class='btn-close text-reset' and @aria-label='Close']")
    # Click the button
    time.sleep(3)
    button.click()



#----------------#
    time.sleep(15)  # Wait for 15 seconds to view results
finally:
    # Close the browser
    driver.quit()  # Ensure the browser closes
