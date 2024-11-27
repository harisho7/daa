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
            }
        }




            #-------------second------------
    
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

    # Try switching to the iframe, if necessary
   









#--------------click technical link 
   
    # Optional: Switch to iframe if necessary
    iframes = driver.find_elements(By.TAG_NAME, 'iframe')
    if iframes:
        print(f"Found {len(iframes)} iframe(s), switching to the first one.")
        driver.switch_to.frame(iframes[0])

    # Increase wait time to handle slower loading elements
    technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/technical"]')))
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    
    # Click the link
    technical_link.click()
    time.sleep(3)

#--------------click technical and apply upcomming filter

#                                                                     #----------upcomming  click filter
#                                                                       #-------- and apply filter success

    # Locate the button using XPath and click it
    filter_button = driver.find_element(By.XPATH, "//button[@id='collapseFilter']")
    time.sleep(3)
    filter_button.click()

    
    # Locate the option "Android Developer II" using XPath and click it
    android_option = driver.find_element(By.XPATH, "//select[@id='nomPosIdFilter_ID']/option[text()='Android Developer II']")
    time.sleep(3)
    android_option.click()

        # Locate the button using XPath and click Apply Filters it
    apply_filter_button = driver.find_element(By.XPATH, "//button[@id='applyFilterId' and contains(text(), 'Apply Filters')]")
    time.sleep(3)
    apply_filter_button.click()



    # Wait for the username field and input the username from JSON
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys(data["upcoming"]["username"])

    # Optional: keep the window open for a few seconds to view results
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

#---------------------------
# ---- Process Technical Sections ---- #

    # ---- Fill Technical Sections ---- #
    # ---- Fill Technical Sections ---- #
    for section_index, technical_section in enumerate(data['technical']):
        print(f"Starting processing for technical section {section_index + 1}")

        # Attempt to fill in the text areas
        try:
            for key, value in technical_section.items():
                print(f"Attempting to locate textarea with ID: {key} for value: {value}")
                try:
                    textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, key)))
                except Exception as e:
                    print(f"Failed to locate element with ID: {key}. Error: {e}")
                    continue  # Skip to the next item if this fails

                # Scroll the textarea into view
                driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

                # Clear the field and input the value
                textarea.clear()
                time.sleep(2)  # Adjust wait as necessary
                textarea.send_keys(value)
                print(f"Successfully filled textarea with ID: {key}")

        except Exception as e:
            print(f"Error processing technical section {section_index + 1}: {e}")
            continue  # Continue to next section even if there's an error

        # Click on the radio button (score3) if needed
        try:
            score3_radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "score3")))
            driver.execute_script("arguments[0].scrollIntoView(true);", score3_radio)
            time.sleep(2)  # Optional wait
            score3_radio.click()
            print(f"Successfully clicked on score3 for technical section {section_index + 1}")
        except Exception as e:
            print(f"Error clicking on score3 for technical section {section_index + 1}: {e}")







    # ---- Fill Technical Sections ---- #






#          #fill completed required                    #click technical and completed---------successfully

#                                           #--/--click completed Technical


    # Increase wait time to handle slower loading elements
    time.sleep(4)
    technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/technical"]')))
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    
    # Click the link
    time.sleep(2)
    technical_link.click()
    time.sleep(2)
        # Find the <a> element by its XPath  --click completed--
    completed_button = driver.find_element(By.XPATH, "//div[@id='complete']//a[contains(text(),'Completed')]")

    # Click the "Completed" link
    time.sleep(3)
    completed_button.click()


                                            # completed click -------------apply filter success



    collapse_filter_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "collapseFilter"))
        )
    time.sleep(3)
    collapse_filter_button.click()



        # Click the select element to open the dropdown
    select_element = driver.find_element(By.XPATH, "//select[@id='nomPosIdFilter_ID']")
    time.sleep(3)
    select_element.click()


    # Now select the desired option by its visible text
    option = driver.find_element(By.XPATH, "//option[text()='Full Stack Developer II']")
    time.sleep(2)
    option.click()

        # Click the "Apply Filters" button using XPath
    apply_filters_button = driver.find_element(By.XPATH, "//button[@id='applyFilterId']")
    time.sleep(2)
    apply_filters_button.click()
    # Assuming 'data' is defined as per your previous structure
    username_to_fill = data["user_complete"]["username"]

    # Wait for the username field to be present and then send the username
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys(username_to_fill)

        # Locate the button using XPath
    button = driver.find_element(By.XPATH, "//button[@data-bs-toggle='offcanvas' and @data-bs-target='#offcanvas1']")

    # Click the button
    time.sleep(3)
    button.click()

    # Locate the textarea for overallFeedback
    try:
        # Locate the textarea using its ID and wait until it's clickable
        textarea = wait.until(EC.element_to_be_clickable((By.ID, "overallFeedback")))

        # Scroll the textarea into view
        driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

        # Clear any existing text in the textarea
        textarea.clear()

        # Optionally wait a moment
        time.sleep(2)

        # Fill the textarea with the value from the data structure
        textarea.send_keys(data["fields_eye"]["overallFeedback"])  # Adjusting to use fields_eye instead

    except Exception as e:
        print(f"Error filling overall feedback textarea: {e}")



    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)

    # Process complete_eye
    complete_eye = data["complete_eye"]
    for index, section_data in enumerate(complete_eye):
        try:
            print(f"Processing complete_eye section {index + 1}...")

            for key, value in section_data.items():
                textarea_xpath = f"(//textarea[@id='{key}'])[{index + 1}]"
                textarea = wait.until(EC.presence_of_element_located((By.XPATH, textarea_xpath)))

                # Scroll the textarea into view if necessary
                driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

                # Clear the field and input the value
                time.sleep(3)
                textarea.clear()
                time.sleep(4)
                textarea.send_keys(value)
                time.sleep(3)

        except Exception as e:
            print(f"Error processing complete_eye section {index + 1}: {e}")

    

    # Fill in the textarea for areaOfDevelopment in textarea_eye
    textarea_area_of_dev = driver.find_element(By.XPATH, "//textarea[@id='areaforDev']")
    textarea_area_of_dev.clear()
    time.sleep(2)  # Shorter wait time for better performance
    textarea_area_of_dev.send_keys(data["textarea_eye"]["areaforDev"])

    # Fill in the textarea for recLearnInitiative in textarea_eye
    textarea_rec_learn_initiative = driver.find_element(By.XPATH, "//textarea[@id='recLearnInitiative']")
    textarea_rec_learn_initiative.clear()
    time.sleep(2)  # Shorter wait time for better performance
    textarea_rec_learn_initiative.send_keys(data["textarea_eye"]["recLearnInitiative"])

    # Optionally, add

                                     #----------Technical completed code submit code and ---------print submit success 
    # Locate the button using XPath
    submit_button = driver.find_element(By.XPATH, "//button[@id='submitResponse']")

    # Click the submit button
    time.sleep(3)
    submit_button.click()

    
    # Wait for the notification message to appear and capture the text
    try:
        # Wait until the div with class 'dmx-notify-message' becomes visible
        response_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
        )
        
        # Print the message inside the div
        print("Message:", response_element.text)
        
    except Exception as e:
        print(f"Error occurred: {e}")

   #----------Locate the button using XPath---------- close button completed

    time.sleep(10)
    button = driver.find_element(By.XPATH, "//button[@type='button' and @class='btn-close text-reset' and @aria-label='Close']")
    # Click the button
    time.sleep(10)
    button.click()






    # Wait until the "CV" button is visible and clickable
    try:
        # Use class name and text to locate the element
        cv_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'dropdown-item btn') and contains(@dmx-bind:href, 's3-file-download')]"))
        )

        # Scroll the element into view (optional if it's off-screen)
        driver.execute_script("arguments[0].scrollIntoView(true);", cv_button)

        # Click the button
        time.sleep(3)
        cv_button.click()
        print("Successfully clicked the CV button!")

    except Exception as e:
        print(f"Error clicking the CV button: {e}")

        #--CV --notification_message;;

    try:
        # Wait for the notification message to appear
        wait = WebDriverWait(driver, 10)
        notification_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "dmx-notify-message"))
        )

        # Get and print the message text
        notification_message = notification_element.text
        print(f"Notification Message: {notification_message}")

    except Exception as e:
        print(f"Error: Unable to retrieve the notification message. {e}")




        #---psyco_report;
    try:
        # Wait for the clickable element
        wait = WebDriverWait(driver, 10)
        element_to_click = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(@class, 'dropdown-item') and contains(@dmx-bind:href, 'psyco_report_path')]")
        ))

        # Click the element
        time.sleep(2)
        element_to_click.click()
        print("Element clicked successfully!")

    except Exception as e:
        print(f"Error: Unable to click the element. {e}")


                                                 #---psyco notification_message--
    try:
        # Wait for the notification element to appear
        wait = WebDriverWait(driver, 10)
        notify_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "dmx-notify-message"))
        )

        # Extract the text from the notification element
        notify_message = notify_element.text

        # Check if the message is related to the "Psychometric report"
        if "Psychometric report" in notify_message:
            print(f"Psychometric Notify Message: {notify_message}")
        else:
            print("Notification message is not related to the Psychometric report.")

    except Exception as e:
        print(f"Error: Unable to retrieve the notification message. {e}")


# #----------cv is not working------but-----


    # # Locate the button by XPath and click ------2nd few --------success psychometrics

    # button = driver.find_element(By.XPATH, "//button[contains(.,'Psychometric')]")
    
    # button.click()
    # wait = WebDriverWait(driver, 10)    
    # try:
    #     # Locate the notification message when it appears
    #     time.sleep(30)
    #     error_message_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.dmx-notify-message")))
        
    #     # Get and print the text of the message
    #     error_message = error_message_element.text
    #     print(f"Error Message: {error_message}")
        
    # except Exception as e:
    #     print(f"Error locating the message: {e}")








                                        #-----#---click ---download section--------------



    try:
        # Wait for the button with the download icon to be clickable
        wait = WebDriverWait(driver, 10)
        download_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and contains(@class, 'btn show')]"))
        )
        
        # Click the download button
        time.sleep(2)
        download_button.click()
        print("Download icon clicked successfully.")

        # If needed, click one of the dropdown items (e.g.,---- Download With Comment)


        download_with_comment = wait.until(
            EC.element_to_be_clickable((By.ID, "btnWithCmmt"))
        )
        time.sleep(5)
        download_with_comment.click()
        print("Download With Comment clicked successfully.")

    except Exception as e:
        print(f"Error clicking the download icon or dropdown: {e}")


            # drop down item----download without comment
    try:
        # Wait for the "Download Without Comment" button to be clickable
        wait = WebDriverWait(driver, 10)
        download_without_comment_button = wait.until(
            EC.element_to_be_clickable((By.ID, "btnWithoutCmmt"))
        )
        
        # Click the button
        time.sleep(5)
        download_without_comment_button.click()
        print("Download Without Comment clicked successfully.")

    except Exception as e:
        print(f"Error clicking the 'Download Without Comment' button: {e}")















    #----------------------------leadership start--------------

    
# #---------------------------

# ##click leadership

 # Increase wait time to handle slower loading elements
    time.sleep(5)
    leadership_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/leadership"]')))
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", leadership_link)
    
    # Click the link
    time.sleep(5)
    leadership_link.click()

    # Print a success message
    print("Leadership link clicked successfully.")


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
    print("Ashutosh")



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
    print("Data Scientist II")

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

# #------------------click leadership---
    
    time.sleep(5)
    leadership_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/leadership"]')))
        
        # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", leadership_link)
        
        # Click the link
    time.sleep(5)
    leadership_link.click()
    # #----------------


    #click complete ------leadership

    completed_button = driver.find_element(By.XPATH, "//div[@id='complete']//a[contains(text(),'Completed')]")

    # Click the "Completed" link
    time.sleep(3)
    completed_button.click()



    # ---Click the button------apply filter


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

#         #--------------json---start 
#     try:
#         # Locate the textarea using its ID and wait until it's clickable
#         textarea = wait.until(EC.element_to_be_clickable((By.ID, "overallFeedback")))

#         # Scroll the textarea into view
#         driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

#         # Clear any existing text in the textarea (optional)
#         textarea.clear()

#         # Optional wait to ensure the field is ready for input
#         time.sleep(1)  # Adjust time as necessary

#         # Fill the textarea with the value from the data structure
#         textarea.send_keys(data["fields"]["overallFeedback"])  # Use the value associated with the key

#     except Exception as e:
#         print(f"Error filling overall feedback: {e}")


#         #-------------fill eye form-----------#
        


#     # Loop through the list of dictionaries (eye) and process each section
#     for index, section_data in enumerate(data["eye"]):
#         try:
#             print(f"Processing eye section {index + 1}...")

#             # Loop through each key-value pair in the current section's dictionary
#             for key, value in section_data.items():
#                 try:
#                     # Adjust the XPath to locate the textarea by the correct identifier
#                     textarea_xpath = f"//textarea[@id='{key}']"  # Use 'name' or 'id' as appropriate

#                     # Wait until the textarea is present and interactable
#                     textarea = wait.until(EC.presence_of_element_located((By.XPATH, textarea_xpath)))

#                     # Scroll the textarea into view if necessary
#                     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

#                     # Clear the field and input the value
#                     textarea.clear()  # Clear the field
#                     time.sleep(1)  # Optional wait before sending keys
#                     textarea.send_keys(value)  # Input the value
#                     time.sleep(1)  # Optional wait after sending keys

#                 except Exception as e:
#                     print(f"Error processing key '{key}' in eye section {index + 1}: {e}")

#         except Exception as e:
#             print(f"Error processing eye section {index + 1}: {e}")








#  # ----------------=--------Locate the <textarea> using XPath


#     # Locate the first <textarea> and fill it with the 'areaforDev' value
#     textarea_areaforDev = driver.find_element(By.XPATH, "//textarea[@id='areaforDev']")
#     textarea_areaforDev.clear()  # Clear the textarea
#     time.sleep(3)
#     textarea_areaforDev.send_keys(data["textarea"]["areaforDev"])  # Fill with value from JSON

 

#     # Locate the second <textarea> and fill it with the 'recLearnInitiative' value
#     textarea_recLearnInitiative = driver.find_element(By.XPATH, "//textarea[@id='recLearnInitiative']")
#     textarea_recLearnInitiative.clear()  # Clear the textarea
#     time.sleep(3)
#     textarea_recLearnInitiative.send_keys(data["textarea"]["recLearnInitiative"])  # Fill with value from JSON


# # #                              # --------------------------------leadership completed code with submit code
   

#  # Locate the button using XPath
#     submit_button = driver.find_element(By.XPATH, "//button[@id='submitResponse']")

#     # Click the submit button
#     time.sleep(3)
#     submit_button.click()


#     # Wait for the div with class 'dmx-notify-message' to appear and capture the text------print success message
#     try:
#         # Wait until the div with the class 'dmx-notify-message' becomes visible
#         response_element = WebDriverWait(driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
#         )
        
#         # Print the message inside the div
#         print("Message:", response_element.text)

#     except Exception as e:
#         print(f"Error occurred: {e}")


#                                                                         ##---leadership complet label close successfully----;;;

#    # Locate the button using XPath close button completed
#     time.sleep(10)
#     button = driver.find_element(By.XPATH, "//button[@type='button' and @class='btn-close text-reset' and @aria-label='Close']")
#     # Click the button
#     time.sleep(3)
#     button.click()

# ##------------------------------------END------------------#


 




# # #                              # --------------------------------leadership completed code with submit code
   


# #----------------#

#                                                                     #------------mindset click success-----------#


                                
#     try:
#         # Wait until the link is clickable and then click it
#         link = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'nav-link') and contains(., 'Mindset')]"))
#         )
        
#         # Click the link
#         link.click()
#         print("Link clicked successfully.")

#     except Exception as e:
#         print(f"Error occurred: {e}")   



        
#  # Find the username field and enter email
#     time.sleep(2)
#     username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
#     username_field.send_keys("Radhika")
#     time.sleep(4)    

# #---------------mindset DOWNLOAD PROCESS SUCCESSFULLY----------------#



#     try:
#         # Wait until the dropdown button is clickable and click it
#         dropdown_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[@class='btn my-0 py-0' and @data-bs-toggle='dropdown']"))
#         )
#         time.sleep(3)
#         dropdown_button.click()
#         print("Dropdown button clicked successfully.")

#         # Wait until the dropdown item "Download in English" is visible and click it
#         download_link = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Download in English')]"))
#         )
#         time.sleep(3)
#         download_link.click()
#         print("Download link clicked successfully.")

#     except Exception as e:
#         print(f"Error occurred: {e}")

#     try:
#         # Wait until the dropdown button is clickable and click it
#         dropdown_button = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//button[@class='btn my-0 py-0' and @data-bs-toggle='dropdown']"))
#         )
#         time.sleep(3)
#         dropdown_button.click()
#         print("Dropdown button clicked successfully.")

#         # Wait until the dropdown item "تحميل باللغة العربية" is visible and click it
#         download_link_arabic = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'تحميل باللغة العربية')]"))
#         )
#         time.sleep(3)
#         download_link_arabic.click()
#         print("Download link in Arabic clicked successfully.")

#     except Exception as e:
#         print(f"Error occurred: {e}")


#------------------end--------





#             #-----------------REPORT DOWNLOAD PROCESS
#              ---------------    ----------------------------  #Click Report Link  # And COMPLETED CLICK and Download Process


        
    # try:
    #     # Wait for the link to be clickable
    #     link = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/report/reports')]"))
    #     )

    #     # Optional: Scroll the link into view
    #     driver.execute_script("arguments[0].scrollIntoView(true);", link)

    #     # Click the link
    #     time.sleep(5)
    #     link.click()

    # except Exception as e:
    #     print(f"Error clicking the link: {e}")



    # try:
    #     # Wait for the link to be clickable
    #     link = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Partial')]"))
    #     )

    #     # Optional: Scroll the link into view
    #     driver.execute_script("arguments[0].scrollIntoView(true);", link)

    #     # Click the link
    #     link.click()

    # except Exception as e:
    #     print(f"Error clicking the link: {e}")
    # #---------------click filter
        
    # try:
    #     # Wait for the button to be clickable
    #     button = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, "collapseFilter"))
    #     )

    #     # Optional: Scroll the button into view
    #     driver.execute_script("arguments[0].scrollIntoView(true);", button)

    #     # Click the button
    #     button.click()

    # except Exception as e:
    #     print(f"Error clicking the button: {e}")


        
    # try:
    #     # Wait for the dropdown to be present
    #     dropdown = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, "nomPosIdFilter_ID"))
    #     )

    #     # Click the dropdown to open it
    #     dropdown.click()

    #     # Create a Select object
    #     select = Select(dropdown)

    #     # Select the option "Data Scientist II"
    #     select.select_by_visible_text("Data Scientist II")

    # except Exception as e:
    #     print(f"Error selecting option: {e}")
            
    #     try:
    #         # Wait for the button to be clickable
    #         apply_button = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.ID, "applyFilterId"))
    #         )

    #         # Click the "Apply Filters" button
    #         apply_button.click()

    #     except Exception as e:
    #         print(f"Error clicking the Apply Filters button: {e}")


    #     # Find the username field and enter email
    #     time.sleep(3)
    #     username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    #     username_field.send_keys("Shweta")
    #     time.sleep(3)

    #     #----click eye success

    #     wait = WebDriverWait(driver, 10)
    #     button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn' and @type='button']")))
    #     # Click the button
    #     time.sleep(3)
    #     button.click()

        
    #     # Wait for the button to be clickable and then click it--- --download with comment----first-----
    #     wait = WebDriverWait(driver, 10)
    #     button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'daa_button') and @type='button']")))

    #     # Click the button
    #     time.sleep(3)
    #     button.click()
    #     time.sleep(10)



    #     # Wait for the button to be clickable and then click it--- --download without comment----second----
    #     wait = WebDriverWait(driver, 10)
    #     button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'daa_button') and contains(., 'Download without Comment')]")))
            
    #         # Perform the click
    #     time.sleep(3)
    #     button.click()







    #     #--------------report click and complete-----click-------


    #     # Wait for the "Report" link to be clickable
    #     wait = WebDriverWait(driver, 10)
    #     report_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/report/reports']")))
    # #    Scroll the element into view
    #     driver.execute_script("arguments[0].scrollIntoView(true);", report_link)
        
    #     # Click the "Report" link
    #     time.sleep(3)
    #     report_link.click()


    # #-----------click filter completed

    # #---------------click filter
    #     filter_button = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.ID, "collapseFilter"))
    #     )
    #     filter_button.click()



    #     try:
    #         # Wait until the dropdown is present
    #         dropdown = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.ID, "nomPosIdFilter_ID"))  # Replace with your actual dropdown ID
    #         )
            
    #         # Create a Select object for the dropdown
    #         time.sleep(3)
    #         select = Select(dropdown)
            
    
    #         # Select the option "Data Scientist II"
    #         time.sleep(3)
    #         select.select_by_visible_text("Data Scientist II")
    #         print("Option 'Data Scientist II' selected successfully.")

    #     except Exception as e:
    #         print(f"Error occurred: {e}")

    #     try:
    #         # Wait until the button is clickable
    #         apply_filters_button = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.ID, "applyFilterId"))  # Replace with the button's ID
    #         )
            
    #         # Click the "Apply Filters" button
    #         time.sleep(3)
    #         apply_filters_button.click()
    #         print("Clicked 'Apply Filters' button successfully.")

    #     except Exception as e:
    #         print(f"Error occurred: {e}")



    # #-----

    #     # Find the username field and enter email
    #     time.sleep(3)
    #     username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    #     username_field.send_keys("Tara")
    #     time.sleep(3)

    #     wait = WebDriverWait(driver, 10)
    #     button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn' and @type='button']")))
    #     # Click the button
    #     time.sleep(3)
    #     button.click()


    #     # Wait for the button to be clickable and then click it --------DOWNLOAD FIRST
    #     wait = WebDriverWait(driver, 10)
    #     button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'daa_button') and @type='button']")))

    #     # Click the button
    #     time.sleep(3)
    #     button.click()
    #     time.sleep(10)


    #     wait = WebDriverWait(driver, 10)
    #     button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'daa_button') and contains(., 'Download without Comment')]")))
            
    #         # Perform the click
    #     time.sleep(3)
    #     button.click()






    time.sleep(15)  # Wait for 15 seconds to view results
finally:
    # Close the browser
    driver.quit()  # Ensure the browser closes