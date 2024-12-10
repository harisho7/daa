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
                 "username": "134"
             },
             "report_complete":{
                 "username":"Aman"
             }


        }


     

    wait = WebDriverWait(driver, 20) 
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))  
    username_field.send_keys(data["login_data"]["username"])  
    print(username_field.text)

    password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))  
    password_field.send_keys(data["login_data"]["password"])  
    print(password_field.text)

    password_field.submit()
#---------------------------

#--------------click technical link 
   
   
    iframes = driver.find_elements(By.TAG_NAME, 'iframe')
    if iframes:
        print(f"Found {len(iframes)} iframe(s), switching to the first one.")
        driver.switch_to.frame(iframes[0])

  
    technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/technical"]')))
    

    driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    
    
    technical_link.click()
    time.sleep(3)



#              #----------upcomming  click filter
#               #-------- and apply filter success


    filter_button = driver.find_element(By.XPATH, "//button[@id='collapseFilter']")
    time.sleep(3)
    filter_button.click()
    print(filter_button.text)
    
    android_option = driver.find_element(By.XPATH, "//select[@id='nomPosIdFilter_ID']/option[text()='Android Developer II']")
    time.sleep(3)
    android_option.click()
    print(android_option.text)

    apply_filter_button = driver.find_element(By.XPATH, "//button[@id='applyFilterId' and contains(text(), 'Apply Filters')]")
    time.sleep(3)
    apply_filter_button.click()
    print(apply_filter_button.text)


    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys(data["upcoming"]["username"])
    print(username_field.text)


    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.p-1")))
    
  
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    
    # Click the button
    time.sleep(3)
    button.click()
    time.sleep(4)

   
    close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "lb-close")))
    
   
    driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
    
   
    time.sleep(4)
    close_button.click()

#---------------------------
# ---- Process Technical Sections ---- #


    for section_index, technical_section in enumerate(data['technical']):
        print(f"Starting processing for technical section {section_index + 1}")

        try:
           
            for key, value in technical_section.items():
                print(f"Attempting to locate textarea with ID: {key} for value: {value}")
                try:
                    
                    textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, key)))
                except Exception as e:
                    print(f"Failed to locate element with ID: {key}. Error: {e}")
                    continue 

                driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
                textarea.clear()
                time.sleep(2)  
                textarea.send_keys(value)

                print(f"Successfully filled textarea with ID: {key}")

         
            try:
                score3_radio = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "score3")))
                driver.execute_script("arguments[0].scrollIntoView(true);", score3_radio)
                time.sleep(2) 
                score3_radio.click()
                print(f"Successfully clicked on score3 for technical section {section_index + 1}")
            except Exception as e:
                print(f"Error clicking on score3 for technical section {section_index + 1}: {e}")

            if section_index < len(data['technical']) - 1:
                try:
                    save_next_button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView(true);", save_next_button)
                    time.sleep(2)  
                    save_next_button.click()
                    print(f"Successfully clicked 'Save & Next' for technical section {section_index + 1}")
                    time.sleep(4)  
                except Exception as e:
                    print(f"Error clicking 'Save & Next' for technical section {section_index + 1}: {e}")
            else:
                print(f"Last technical section reached. Skipping 'Save & Next' button for section {section_index + 1}")

        except Exception as e:
            print(f"Error processing technical section {section_index + 1}: {e}")
            continue 


#          #fill completed required              
    time.sleep(4)
    technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/technical"]')))
    
 
    driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    

    time.sleep(2)
    technical_link.click()
    print(technical_link.text)
    time.sleep(2)
     
    try:
   
        link_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Completed')]")))
        

        time.sleep(3)
        link_element.click()
        print("Clicked on the 'Completed' link successfully.")

    except Exception as e:
        print("Error while clicking the 'Completed' link:", e)




                                            # completed click -------------apply filter success



    collapse_filter_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "collapseFilter"))
        )
    time.sleep(3)
    collapse_filter_button.click()
    print(collapse_filter_button.text)


    select_element = driver.find_element(By.XPATH, "//select[@id='nomPosIdFilter_ID']")
    time.sleep(3)
    select_element.click()
    print(select_element.text)



 
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='Full Stack Developer II']"))
    )
    option.click()
    print(option.text)



        
    apply_filters_button = driver.find_element(By.XPATH, "//button[@id='applyFilterId']")
    time.sleep(2)
    apply_filters_button.click()
    print(apply_filters_button.text)
 
    username_to_fill = data["user_complete"]["username"]

   
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys(username_to_fill)
    print(username_field.text)
   
    button = driver.find_element(By.XPATH, "//button[@data-bs-toggle='offcanvas' and @data-bs-target='#offcanvas1']")

    time.sleep(3)
    button.click()

    try:
    
        textarea = wait.until(EC.element_to_be_clickable((By.ID, "overallFeedback")))

     
        driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

     
        textarea.clear()

      
        time.sleep(2)

        textarea.send_keys(data["fields_eye"]["overallFeedback"]) 

    except Exception as e:
        print(f"Error filling overall feedback textarea: {e}")

    wait = WebDriverWait(driver, 10)

    # ----------------Process complete_eye
    complete_eye = data["complete_eye"]
    for index, section_data in enumerate(complete_eye):
        try:
            print(f"Processing complete_eye section {index + 1}...")

            for key, value in section_data.items():
                textarea_xpath = f"(//textarea[@id='{key}'])[{index + 1}]"
                textarea = wait.until(EC.presence_of_element_located((By.XPATH, textarea_xpath)))

       
                driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

                textarea.clear()
                time.sleep(2)
                textarea.send_keys(value)
                print(textarea.text)
                

        except Exception as e:
            print(f"Error processing complete_eye section {index + 1}: {e}")

   
    textarea_area_of_dev = driver.find_element(By.XPATH, "//textarea[@id='areaforDev']")
    textarea_area_of_dev.clear()
    time.sleep(2)  
    textarea_area_of_dev.send_keys(data["textarea_eye"]["areaforDev"])

 
    textarea_rec_learn_initiative = driver.find_element(By.XPATH, "//textarea[@id='recLearnInitiative']")
    textarea_rec_learn_initiative.clear()
    time.sleep(2)  
    textarea_rec_learn_initiative.send_keys(data["textarea_eye"]["recLearnInitiative"])


    submit_button = driver.find_element(By.XPATH, "//button[@id='submitResponse']")

    # Click the submit button
    time.sleep(3)
    submit_button.click()


    try:
        # Wait until the div with class 'dmx-notify-message' becomes visible
        response_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
        )
        
        # Print the message inside the div
        print("Message:", response_element.text)
        
    except Exception as e:
        print(f"Error occurred: {e}")


    
    button = driver.find_element(By.XPATH, "//button[@type='button' and @class='btn-close text-reset' and @aria-label='Close']")
    # Click the button
    time.sleep(10)
    button.click()
    print(button.text)





              #--------#--- CV----//--- button process----------click to ho raha but error aa rahi hai


    # try:
    #     # Find the <a> element using its XPath
    #     dropdown_item = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//a[@class='dropdown-item btn']"))
    #     )

    #     # Perform a click action
    #     dropdown_item.click()

    #     # Print a message to confirm the click
    #     print("Clicked the link of cv")

    #     # Wait for the notification message to appear
    #     notification_element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "dmx-notify-message"))
    #     )

    #     # Get and print the message text
    #     notification_message = notification_element.text
    #     print(f"Notification Message: {notification_message}")

    # except Exception as e:
    #     print(f"Error: {e}")




    #                             #--#---------psyco_report----------------;


    # try:
    #     # Find the <a> element using XPath
    #     dropdown_item = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//a[@class='dropdown-item btn']"))
    #     )

    #     # Perform a click action
    #     dropdown_item.click()
    #     print("Clicked the link of physco")

    #     # Wait for the notification message to appear after clicking
    #     notify_element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "dmx-notify-message"))
    #     )

    #     # Extract the text from the notification element
    #     notify_message = notify_element.text

    #     # Check if the message is related to the "Psychometric report"
    #     if "Psychometric report" in notify_message:
    #         print(f"Psychometric Notify Message: {notify_message}")
    #     else:
    #         print("Notification message is not related to the Psychometric report.")

    # except Exception as e:
    #     print(f"Error: {e}")


                         ##-----------------------download process--------------------


    # # Locate the path element inside the SVG and click it
    # svg_element = driver.find_element(By.XPATH, "//svg//path[@fill='#646464']")
    # time.sleep(2)
    # svg_element.click()

    # # Print confirmation message
    # print("SVG element clicked successfully.")


    #     ##-----------'Download With Comment'-----

    # # Locate the button by its text and click it
    # button = driver.find_element(By.XPATH, "//button[text()='Download With Comment']")
    # time.sleep(2)
    # button.click()

    # # Print confirmation message
    # print("Button clicked successfully.")

    #             ##-----------'Download Without Comment'----

    #     # Locate the button by its text and click it
    # button = driver.find_element(By.XPATH, "//button[text()='Download Without Comment']")
    # time.sleep(5)
    # button.click()

    # # Print confirmation message
    # print("Button clicked successfully.")






#     #----------------------------Leadership_part--------------start---------


    
    leadership_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/leadership"]')))
    
    driver.execute_script("arguments[0].scrollIntoView(true);", leadership_link)
    
    leadership_link.click()

    print("Leadership link clicked successfully.")

    # Wait until the button is clickable
    wait = WebDriverWait(driver, 10)
    print('Till Heere******************')
    time.sleep(50)
    button = wait.until(EC.element_to_be_clickable((By.ID, 'collapseFilter')))
    print(button)
    # Click the button
    button.click()

  
    print("Clicked the filter button")


    dropdown = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//select[@id='asserNameFilter_ID']"))
    )
    time.sleep(2)
    dropdown.click()
    print(dropdown.text)

    
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='Ashutosh']"))
    )
    time.sleep(3)
    option.click()
    print(option.text)

     
   
    print("Clicked the dropdown option Ashutosh")

      
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'nomPosIdFilter_ID'))
    )
    time.sleep(3)
    dropdown.click()  
    print(dropdown.text)
  
    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='Data Scientist II']"))
    )
    time.sleep(3)
    option.click()  
    print(option)

    apply_filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'applyFilterId'))
    )
    time.sleep(3)
    apply_filter_button.click() 
    print(apply_filter_button.text)



    username = data["user_data"]["username"]
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys(username) 
    time.sleep(2)
    print(username)

    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.p-1")))
    
    driver.execute_script("arguments[0].scrollIntoView(true);", button)
    

    time.sleep(3)
    button.click()

    time.sleep(4)


    close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "lb-close")))
    
 
    driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
    

    time.sleep(4)
    close_button.click()
    print(close_button.text)




  
    for i, section_data in enumerate(data["user_data"]["my_list"]):
        try:
            print(f"Processing section {i + 1}")

          
            for key, value in section_data.items():
                try:
                   
                    textarea = wait.until(EC.presence_of_element_located((By.NAME, key)))

                    
                    driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

                 
                    textarea.clear()
                    time.sleep(2) 
                    textarea.send_keys(value)
                except Exception as e:
                    print(f"Error while filling '{key}' in section {i + 1}: {e}")

           
            if i < len(data["user_data"]["my_list"]) - 1: 
                try:
               
                    radio_button = wait.until(EC.element_to_be_clickable((By.ID, "score3")))  
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button)
                    time.sleep(2)
                    radio_button.click()

                    save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
                    time.sleep(2) 
                    save_next_button.click()

             
                    time.sleep(3)
                except Exception as e:
                    print(f"Error during radio button or save action for section {i + 1}: {e}")
            else:
                print(f"Last section reached, skipping Save & Next button for section {i + 1}")

        except Exception as e:
            print(f"Error processing section {i + 1}: {e}")




# #------------------click leadership---
   


    try:
    
        leadership_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/rac_assessment/leadership')]"))
        )


        print("Clicking the Leadership link...")


        time.sleep(3)
        leadership_link.click()


        print("Leadership link clicked!")

    except Exception as e:
        print(f"An error occurred: {e}")


        #   ------#click---- complete ------leadership
    try:

        completed_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'nav-link') and text()='Completed']"))
        )


        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", completed_button)


        button_text = completed_button.text
        print(f"Button Text: {button_text}")

  
        time.sleep(3)


        completed_button.click()
        print("Completed button clicked successfully!")

    except Exception as e:
        print(f"Error clicking the 'Completed' button: {e}")
    

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'collapseFilter')) 
    )
    time.sleep(2)
    button.click()


  
    wait = WebDriverWait(driver, 10)
    dropdown_element = wait.until(EC.element_to_be_clickable((By.ID, 'asserNameFilter_ID')))

    select = Select(dropdown_element)

 
    select.select_by_visible_text("Ashutosh")

    print("Selected the option Ashutosh")

       
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'nomPosIdFilter_ID'))
    )
    time.sleep(3)
    dropdown.click() 

    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='Data Scientist II']"))
    )
    time.sleep(3)
    option.click()  


    apply_filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'applyFilterId'))
    )
    time.sleep(3)
    apply_filter_button.click()  



    try:
        username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
        username_value = data["complete_my_list_eye"]["#username"]

     
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", username_field)

       
        username_field.clear()
        username_field.send_keys(username_value)
        print(f"Sent value '{username_value}' to the username field.")
    except Exception as e:
        print(f"Error sending value to the username field: {e}")

      
    button = driver.find_element(By.XPATH, "//button[@data-bs-toggle='offcanvas' and @data-bs-target='#offcanvas1']")

    time.sleep(3)
    button.click()

        #--------------json---start 
    try:

        textarea = wait.until(EC.element_to_be_clickable((By.ID, "overallFeedback")))

    
        driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

        textarea.clear()

        time.sleep(1)  

        
        textarea.send_keys(data["fields"]["overallFeedback"])  # Use the value associated with the key

    except Exception as e:
        print(f"Error filling overall feedback: {e}")


#         #-------------fill eye form-----------#
        


   
    for index, section_data in enumerate(data["eye"]):
        try:
            print(f"Processing eye section {index + 1}...")

            
            for key, value in section_data.items():
                try:
                   
                    textarea_xpath = f"//textarea[@id='{key}']"  

                 
                    textarea = wait.until(EC.presence_of_element_located((By.XPATH, textarea_xpath)))

                  
                    driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

                    
                    textarea.clear() 
                    time.sleep(2) 
                    textarea.send_keys(value)  
                    time.sleep(1)  

                except Exception as e:
                    print(f"Error processing key '{key}' in eye section {index + 1}: {e}")

        except Exception as e:
            print(f"Error processing eye section {index + 1}: {e}")




#  # ----------------=--------Locate the <textarea> using XPath


  
    textarea_areaforDev = driver.find_element(By.XPATH, "//textarea[@id='areaforDev']")
    textarea_areaforDev.clear()  
    time.sleep(3)
    textarea_areaforDev.send_keys(data["textarea"]["areaforDev"])  

 
    textarea_recLearnInitiative = driver.find_element(By.XPATH, "//textarea[@id='recLearnInitiative']")
    textarea_recLearnInitiative.clear()  # Clear the textarea
    time.sleep(3)
    textarea_recLearnInitiative.send_keys(data["textarea"]["recLearnInitiative"])  


# # #                              # --------------------------------leadership completed code with submit code
   

 
    submit_button = driver.find_element(By.XPATH, "//button[@id='submitResponse']")

    time.sleep(3)
    submit_button.click()


  
    try:
       
        response_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
        )
        
        # Print the message inside the div
        print("Message:", response_element.text)

    except Exception as e:
        print(f"Error occurred: {e}")


#                                           ##---leadership complet label close successfully----;;;

   # Locate the button using XPath close button completed
    time.sleep(10)
    button = driver.find_element(By.XPATH, "//button[@type='button' and @class='btn-close text-reset' and @aria-label='Close']")
    # Click the button
    time.sleep(3)
    button.click()


    ##-----------cv-is not working------ and ----pyscho----click

    # # Find the <a> element using XPath
    # dropdown_item = driver.find_element(By.XPATH, "//a[@class='dropdown-item btn']")

    # # Perform a click action
    # time.sleep(3)
    # dropdown_item.click()

    # # Print a message to confirm the click
    # print("click physco")
    # # Locate the div element by class name
    # message_element = driver.find_element(By.CLASS_NAME, "dmx-notify-message")

    # # Extract and print the message text
    # print("Message:", message_element.text)




#     #----------------------------Leadership_part--------------End----



# # #------------mindset click success-----------#

                                
    try:
       
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'nav-link') and contains(., 'Mindset')]"))
        )
        
        
        link.click()
        print("Link clicked successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")   


    time.sleep(2)
        
    
    try:
        username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
        
    
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", username_field)
        
      
        username_field.clear() 
        username_field.send_keys(data["mindset_user"]["#username"])
        print("Value sent successfully:", data["mindset_user"]["#username"])
    except Exception as e:
        print("Error sending value to username field:", e)  




    try:
       
        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn my-0 py-0' and @data-bs-toggle='dropdown']"))
        )
        time.sleep(3)
        dropdown_button.click()
        print("Dropdown button clicked successfully.")

        
        download_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Download in English')]"))
        )
        time.sleep(3)
        download_link.click()
        print("Download link clicked successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")

    try:
       
        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn my-0 py-0' and @data-bs-toggle='dropdown']"))
        )
        time.sleep(3)
        dropdown_button.click()
        print("Dropdown button clicked successfully.")

       
        download_link_arabic = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'تحميل باللغة العربية')]"))
        )
        time.sleep(3)
        download_link_arabic.click()
        print("Download link in Arabic clicked successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")


# ##-----------------report_start click link-----

    
    try:
       
        report_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[./p[text()='Report']]"))
        )
        
      
        report_link.click()

    except Exception as e:
        print(f"Error: {e}")

    
    try:
      
        partial_complete_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'partialCompleteId'))
        )
        
        time.sleep(2)
        partial_complete_element.click()

    except Exception as e:
        print(f"Error: {e}")

    filter = driver.find_element(By.ID,"collapseFilter")
    filter.click()
    time.sleep(3)


   
    time.sleep(3)
        
    dropdown_element = driver.find_element(By.ID, "nomPosIdFilter_ID")

    select = Select(dropdown_element)

    select.select_by_visible_text("Data Scientist II")


    time.sleep(3)

    click_applyfilter = driver.find_element(By.ID,"applyFilterId")
    time.sleep(2)
    click_applyfilter.click()
  
            
    
    username = data["report_partial"]["username"]
    input_field = driver.find_element(By.ID, "username")
    input_field.click()
    time.sleep(2)
    input_field.send_keys(username)
    print(username)
    time.sleep(3)
   


    try:
     
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "eyeReportId"))
        )

       
        button.click()

    except Exception as e:
        print(f"Error occurred: {e}")

        


    
    print("clicked eye_report")
    time.sleep(2)
    download_with_comment = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "downloadWithCmmtBtn"))
    )

    download_with_comment.click()
  

    time.sleep(15)
    download_without_comment = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'downloadWithOutCmmtBtn'))
    )

    time.sleep(5)
    download_without_comment.click()
    time.sleep(10)


    back_button = driver.find_element(By.XPATH, '//*[@id="backButtonId "]')
    back_button.click()

    #------------apply filter

    filter = driver.find_element(By.ID,"collapseFilter")
    filter.click()
    time.sleep(3)


   
    time.sleep(3)
        
    dropdown_element = driver.find_element(By.ID, "nomPosIdFilter_ID")

    select = Select(dropdown_element)

    select.select_by_visible_text("Data Scientist II")


    time.sleep(3)

    click_applyfilter = driver.find_element(By.ID,"applyFilterId")
    time.sleep(2)
    click_applyfilter.click()
  
            
    
    username = data["report_partial"]["username"]
    input_field = driver.find_element(By.ID, "username")
    input_field.click()
    time.sleep(2)
    input_field.send_keys(username)
    print(username)
    time.sleep(3)
    
#-----

    try:
      
        button = driver.find_element(By.ID, "idRedirectIndividualPartial")
        button.click()

        print("Button clicked successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(2)

    try:
     
        button = driver.find_element(By.ID, "idIndividualDownload")
        time.sleep(2)
        button.click()
        time.sleep(10)

        print("Button clicked successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        

    try:
      
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idbackButton"))
        )
        time.sleep(2)
        button.click()
        time.sleep(2)

        print("Back button clicked successfully after wait!")
    except Exception as e:
        print(f"An error occurred: {e}")
        




#download--------



    filter = driver.find_element(By.ID,"collapseFilter")
    filter.click()
    time.sleep(3)


   
    time.sleep(3)
        
    dropdown_element = driver.find_element(By.ID, "nomPosIdFilter_ID")

    select = Select(dropdown_element)

    select.select_by_visible_text("Data Scientist II")


    time.sleep(3)

    click_applyfilter = driver.find_element(By.ID,"applyFilterId")
    time.sleep(2)
    click_applyfilter.click()
  
            
    
    username = data["report_partial"]["username"]
    input_field = driver.find_element(By.ID, "username")
    input_field.click()
    time.sleep(2)
    input_field.send_keys(username)
    print(username)
    time.sleep(3)
    button = driver.find_element(By.ID, "downloadReportBtnId")
    button.click()

    print("Button clicked successfully!")

    download_with_comment = driver.find_element(By.ID, "btnWithCmmtP")
    time.sleep(3)
    download_with_comment.click()

    print("Button clicked successfully!") 
    time.sleep(15)

    button = driver.find_element(By.ID, "downloadReportBtnId")
    button.click()
    time.sleep(3)

    download_without_comment = driver.find_element(By.XPATH, "//button[@id='btnWithoutCmmtP']")
    
    download_without_comment.click()
    time.sleep(10)

#--completed

    div_element_completed = driver.find_element(By.ID, "complete")
    div_element_completed.click()
    time.sleep(10)


    try:
       
        collapse_filter_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "collapseFilter"))
        )
        collapse_filter_btn.click()
        print("Collapse Filter button clicked successfully!")
    except Exception as e:
        print(f"An error occurred while clicking 'collapseFilter': {e}")

    time.sleep(1) 

    try:
       
        select_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "nomPosIdFilter_ID"))
        )
     
        select = Select(select_element)
        select.select_by_visible_text("Full Stack Developer II")
        print("Option 'Full Stack Developer II' selected successfully!")
    except Exception as e:
        print(f"An error occurred while selecting the option: {e}")

    time.sleep(1)  

    try:
     
        apply_filter_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "applyFilterId"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", apply_filter_btn) 
        apply_filter_btn.click()
        print("Apply Filter button clicked successfully!")
    except Exception as e:
        print(f"An error occurred while clicking 'applyFilterId': {e}")

    time.sleep(1)  
                
    
    username = data["report_complete"]["username"]
    input_field = driver.find_element(By.ID, "username")
    input_field.click()
    time.sleep(2)
    input_field.send_keys(username)
    print(username)
    time.sleep(3)


    eye_report_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "eyeReportID"))
    )

    eye_report_button.click()

  
        
    print("clicked eye_report")
    time.sleep(2)
    download_with_comment = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "downloadWithCmmtBtn"))
    )

    download_with_comment.click()
  

    time.sleep(15)
    download_without_comment = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'downloadWithOutCmmtBtn'))
    )

    time.sleep(5)
    download_without_comment.click()
    time.sleep(10)


    back_button = driver.find_element(By.XPATH, '//*[@id="backButtonId "]') 
    time.sleep(5)
    back_button.click()


    filter = driver.find_element(By.ID,"collapseFilter")
    filter.click()
    time.sleep(3)


   
    time.sleep(3)
        
    dropdown_element = driver.find_element(By.ID, "nomPosIdFilter_ID")

    select = Select(dropdown_element)

    select.select_by_visible_text("Full Stack Developer II")


    time.sleep(3)

    click_applyfilter = driver.find_element(By.ID,"applyFilterId")
    time.sleep(2)
    click_applyfilter.click()
  
            
    
    username = data["report_complete"]["username"]
    input_field = driver.find_element(By.ID, "username")
    input_field.click()
    time.sleep(2)
    input_field.send_keys(username)
    print(username)
    time.sleep(3)


    try:
       
        button = driver.find_element(By.ID, "idRedirectIndividual")
        button.click()

        print("Button clicked successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(2)

    try:
      
        button = driver.find_element(By.ID, "idIndividualDownload")
        time.sleep(2)
        button.click()
        time.sleep(10)

        print("Button clicked successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        

    try:
        # Wait until the button is clickable
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idbackButton"))
        )
        time.sleep(2)
        button.click()
        time.sleep(2)

        print("Back button clicked successfully after wait!")
    except Exception as e:
        print(f"An error occurred: {e}")
        



#download--------



    filter = driver.find_element(By.ID,"collapseFilter")
    filter.click()
    time.sleep(3)


   
    time.sleep(3)
        
    dropdown_element = driver.find_element(By.ID, "nomPosIdFilter_ID")

    select = Select(dropdown_element)

    select.select_by_visible_text("Full Stack Developer II")


    time.sleep(3)

    click_applyfilter = driver.find_element(By.ID,"applyFilterId")
    time.sleep(2)
    click_applyfilter.click()
  
            
    
    username = data["report_complete"]["username"]
    input_field = driver.find_element(By.ID, "username")
    input_field.click()
    time.sleep(2)
    input_field.send_keys(username)
    print(username)
    time.sleep(3)


    button = driver.find_element(By.ID, "doownloadReportBtnId") 
    button.click()

    print("Button clicked successfully!")

    download_with_comment_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnWithCmmt"))
    )
    download_with_comment_button.click()
    print("download with comment")

    time.sleep(15)

    button = driver.find_element(By.ID, "doownloadReportBtnId")
    button.click()
    time.sleep(3)

    download_without_comment_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnWithoutCmmt"))
    )
    download_without_comment_button.click()

    time.sleep(10)


#----complete assesment

    link_report = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/report/rac-report') and .//p[text()='Report']]"))
    )


    time.sleep(2)
    link_report.click()

    completed_card = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "completedCardId"))
    )
    time.sleep(2)
    completed_card.click()
    print("completed card")

    time.sleep(2)
    click_filter = driver.find_element(By.ID,"collapseFilter")
    click_filter.click()
    time.sleep(2)
        
    try:

        click_nominated = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "nomPosIdFilter_ID"))
        )
        
      
        select = Select(click_nominated)
        select.select_by_visible_text("Full Stack Developer II")
        
    except Exception as e:
        print(f"Error occurred: {e}")

        
    time.sleep(2)
    click_apply_filter = driver.find_element(By.ID, "applyFilterId")
    click_apply_filter.click()

   
    time.sleep(5)
    complete_username = data["report_complete"]["username"]
    complete_input = driver.find_element(By.ID, "username")
    complete_input.click()
    time.sleep(3)
    complete_input.send_keys(complete_username)
    time.sleep(3)
    

    eye_report_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "eyeReportID"))
    )

    eye_report_button.click()

  
        
    print("clicked eye_report")
    time.sleep(2)
    download_with_comment = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "downloadWithCmmtBtn"))
    )

    download_with_comment.click()
  

    time.sleep(15)
    download_without_comment = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'downloadWithOutCmmtBtn'))
    )

    time.sleep(5)
    download_without_comment.click()
    time.sleep(10)


    back_button = driver.find_element(By.XPATH, '//*[@id="backButtonId "]')
    time.sleep(5)
    back_button.click()


#----department

    link_report = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/report/rac-report') and .//p[text()='Report']]"))
    )

    time.sleep(2)
    link_report.click()

    department_card = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "departmentCardId"))
    )

    department_card.click()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

    #---fill strength part 1

    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthDepBtn_0"))
    )

    # Click the button
    time.sleep(3)
    button.click()
    time.sleep(3)

    textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    )

    textarea.clear()
    time.sleep(3)
    textarea.send_keys("textarea filled by DB")

    time.sleep(2)

    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idCloseBtn"))
    )
    close_button.click()
    print("closed")
    time.sleep(3)


    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthDepBtn_0"))
    )

    time.sleep(3)
    button.click()
    time.sleep(3)

    textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    )

    textarea.clear()
    time.sleep(3)
    textarea.send_keys("database management system")

    time.sleep(2)


    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idSaveBtn"))
    )
    time.sleep(2)
    save_button.click()
    print("save changes successfully")
    time.sleep(5)


#---start weakness -----1

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
    textarea.send_keys("This is a sample weakness.")


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
    textarea.send_keys("This is a part of weakness.")
    time.sleep(5)
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idSaveBtn"))
    )
    save_button.click()
    print("save changeses weakness")
    time.sleep(5)

    
    #--------2nd


    #---fill strength part 2

    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthDepBtn_1"))
    )

    time.sleep(3)
    button.click()
    time.sleep(3)

    textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    )

    textarea.clear()
    time.sleep(3)
    textarea.send_keys("textarea filled by DB 2")

    time.sleep(2)

    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idCloseBtn"))
    )
    close_button.click()
    print("closed")
    time.sleep(3)


    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthDepBtn_1"))
    )

    time.sleep(3)
    button.click()
    time.sleep(3)

    textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    )

    textarea.clear()
    time.sleep(3)
    textarea.send_keys("database management system ")

    time.sleep(2)


    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idSaveBtn"))
    )
    time.sleep(2)
    save_button.click()
    print("save changes successfully 2")
    time.sleep(5)




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

    time.sleep(2)
    link_report.click()

    n_level_card = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "nLevelCardId"))
    )
    n_level_card.click()
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, 5000);")

    time.sleep(2)


    #---fill strength part 1 

    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_0"))
    )

    
    time.sleep(3)
    button.click()
    time.sleep(3)

    textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    )

    textarea.clear()
    time.sleep(3)
    textarea.send_keys("textarea filled by DB")

    time.sleep(2)

    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idCloseBtn"))
    )
    close_button.click()
    print("closed")
    time.sleep(3)


    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_0"))
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
    print("save changes successfully")
    time.sleep(5)


#--------------



#---start weakness -----1

    weakness_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
    )
    time.sleep(3)
    weakness_button.click()
    print("click weakness")


    textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
    )
    textarea.clear()
    textarea.send_keys("This is a sample weakness.")


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
    print("click weakness")


    textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
    )
    textarea.clear()
    textarea.send_keys("This is a part of weakness.")
    time.sleep(5)
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idSaveBtn"))
    )
    save_button.click()
    print("save changeses weakness")
    time.sleep(5)

    
    #---fill strength part 2

    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_1"))
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
    textarea.send_keys("textarea filled by DB 2")

    time.sleep(2)

    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idCloseBtn"))
    )
    close_button.click()
    print("closed")
    time.sleep(3)


    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_1"))
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
    print("save changes successfully 2")
    time.sleep(5)


#--------------



#---start weakness -----2

    weakness_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
    )
    time.sleep(3)
    weakness_button.click()
    print("click weakness 2")


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
        EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
    )
    time.sleep(3)
    weakness_button.click()
    print("click weakness 2")

    time.sleep(4)
    textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
    )
    textarea.clear()
    time.sleep(2)
    textarea.send_keys("This is a part of weakness.")
    time.sleep(5)
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idSaveBtn"))
    )
    save_button.click()
    print("save changeses weakness 2")
    time.sleep(5)



    #---fill strength part 3

    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_2"))
    )

    # Click the button
    time.sleep(3)
    button.click()
    time.sleep(3)

    textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    )

   
    textarea.clear()
    time.sleep(3)
    textarea.send_keys("textarea filled by DB 3")

    time.sleep(2)

    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idCloseBtn"))
    )
    close_button.click()
    print("closed")
    time.sleep(3)


    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_2"))
    )

    
    time.sleep(3)
    button.click()
    time.sleep(3)

    textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    )

   
    textarea.clear()
    time.sleep(3)
    textarea.send_keys("database management system")

    time.sleep(2)


    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idSaveBtn"))
    )
    time.sleep(2)
    save_button.click()
    print("save changes successfully 3")
    time.sleep(5)

#---start weakness -----3

    weakness_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idEmpWeaknessNLVLBtn_"))
    )
    time.sleep(3)
    weakness_button.click()
    print("click weakness 2")


    textarea = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "idWeaknessInput"))
    )
    textarea.clear()
    textarea.send_keys("This is a sample weakness.3")


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
    print("click weakness 3")


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
    print("save changeses weakness 3")
    time.sleep(5)



    #---fill strength part 4

    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "idStrengthNLVLBtn_3"))
    )

    time.sleep(3)
    button.click()
    time.sleep(3)

    textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    )

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

    time.sleep(3)
    button.click()
    time.sleep(3)

    textarea = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "idStrengthInput"))
    )

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



    
    driver.execute_script("window.scrollBy(0, -5000);")


    #--report click

    link_report = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/report/rac-report') and .//p[text()='Report']]"))
    )

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





    









    time.sleep(15)
finally:
    # Close the browser
    driver.quit()
