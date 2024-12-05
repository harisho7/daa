from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Open the target website
    driver.get("http://localhost:3000/test-login-cozmotec-dev")
    
    
    # Wait until the username field is present
    wait = WebDriverWait(driver, 20)  # Increase the wait time  
    
    # Find the username field and enter email
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("ashutosh615singh@gmail.com")
    
    # Find the password field and enter the password
    password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))
    password_field.send_keys("Ashu@1234")  
    
    # Submit the login form 
    password_field.submit()


                                                                              #---------click Technical link--------------#


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




# #                                                   #------------------- UPCOMING FILL THE ALL FORM----



 # Find the username field and enter email
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("Jaya")
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

        #-------#------# ------------  # /////// technical upcomming fill all the form for loop in the successfully in ARRAY


    # Sample list of dictionaries
    my_list = [
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
            "areaOfDevelopment": "I need to improve time  THANKS."
        },
        {
            "observation": "This is an PASSED.",
            "strength": "My strength is PERFECT.",
            "areaOfDevelopment": "I need to improve time CORRECTLY RUN."
        }
    ]

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)

    # ---- First Section ---- #
    try:
        first_section_data = my_list[0]  # First dictionary data
        for key, value in first_section_data.items():
            # Locate the textarea using its ID
            textarea = wait.until(EC.presence_of_element_located((By.ID, key)))

            # Scroll the textarea into view if necessary
            driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

            # Clear the field and input the value
            textarea.clear()
            time.sleep(3)  # Optional wait
            textarea.send_keys(value)
    except Exception as e:
        print(f"Error processing first section: {e}")

    # Handle radio button and save action to move to the second section
    try:
        # Locate the radio button and Save & Next button
        radio_button = wait.until(EC.element_to_be_clickable((By.ID, "score3")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button)
        time.sleep(3)
        radio_button.click()
        
        save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
        time.sleep(3)
        save_next_button.click()
        time.sleep(4)  # Wait for the second section to load
    except Exception as e:
        print(f"Error during radio button or save action: {e}")

    # ---- Second Section ---- #
    try:
        second_section_data = my_list[1]  # Second dictionary data
        for key, value in second_section_data.items():
            textarea = wait.until(EC.presence_of_element_located((By.ID, key)))
            driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
            textarea.clear()
            time.sleep(3)
            textarea.send_keys(value)
    except Exception as e:
        print(f"Error processing second section: {e}")

    # Handle Save & Next to move to the third section
    try:
        save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
        time.sleep(3)
        save_next_button.click()
        time.sleep(4)  # Wait for the third section to load
    except Exception as e:
        print(f"Error during save action for second section: {e}")

    # ---- Third Section ---- #
    try:
        third_section_data = my_list[2]  # Third dictionary data
        for key, value in third_section_data.items():
            textarea = wait.until(EC.presence_of_element_located((By.ID, key)))
            driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
            textarea.clear()
            time.sleep(3)
            textarea.send_keys(value)
    except Exception as e:
        print(f"Error processing third section: {e}")

    # Handle Save & Next to move to the fourth section
    try:
        save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
        time.sleep(3)
        save_next_button.click()
        time.sleep(4)  # Wait for the fourth section to load
    except Exception as e:
        print(f"Error during save action for third section: {e}")

    # ---- Fourth Section ---- #
    try:
        fourth_section_data = my_list[3]  # Fourth dictionary data
        for key, value in fourth_section_data.items():
            textarea = wait.until(EC.presence_of_element_located((By.ID, key)))
            driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
            textarea.clear()
            time.sleep(3)
            textarea.send_keys(value)
    except Exception as e:
        print(f"Error processing fourth section: {e}")

    # Handle Save & Next to move to the fifth section
    try:
        save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
        time.sleep(3)
        save_next_button.click()
        time.sleep(4)  # Wait for the fifth section to load
    except Exception as e:
        print(f"Error during save action for fourth section: {e}")

    # ---- Fifth Section ---- #
    try:
        fifth_section_data = my_list[4]  # Fifth dictionary data
        for key, value in fifth_section_data.items():
            textarea = wait.until(EC.presence_of_element_located((By.ID, key)))
            driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
            textarea.clear()
            time.sleep(3)
            textarea.send_keys(value)
    except Exception as e:
        print(f"Error processing fifth section: {e}")



##------------------



#                                                                  #---------click CV---success---*







#     # Locate the button using XPath and click it
#     button = driver.find_element(By.XPATH, "//button[@class='btn border-1 accent accentBorder']")
#     time.sleep(3)
#     button.click()


# # Wait for the notification message to appear
#     cv_error_element = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
#     )
    
#     # Print the CV error message
#     print("CV Error Message:", cv_error_element.text)


                    #------------------------------second click physcometric success but both code hit so this code error










    # Locate the button by XPath and click 2nd few success
    button = driver.find_element(By.XPATH, "//button[contains(.,'Psychometric')]")
    time.sleep(30)
    button.click()
    wait = WebDriverWait(driver, 10)    
    try:
        # Locate the notification message when it appears
        error_message_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.dmx-notify-message")))
        
        # Get and print the text of the message
        error_message = error_message_element.text
        print(f"Error Message: {error_message}")
        
    except Exception as e:
        print(f"Error locating the message: {e}")



    


#                     #submit all fields technical skills but submit is not allow


#     #  # Wait for the "Submit" button to be clickable and then click it
#     # submit_button = wait.until(
#     #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#conditional2 button[type="submit"]'))
#     # )
#     # submit_button.click()

                                            #fill completed required                    #click technical and completed------------success
                                                                #click completed Technical


    # Increase wait time to handle slower loading elements
    time.sleep(4)
    technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/technical"]')))
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    
    # Click the link
    technical_link.click()
    time.sleep(2)
        # Find the <a> element by its XPath
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






 # Find the username field and enter email
    time.sleep(2)
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("Aman")
    time.sleep(4)
        # Locate the button using XPath
    button = driver.find_element(By.XPATH, "//button[@data-bs-toggle='offcanvas' and @data-bs-target='#offcanvas1']")

    # Click the button
    time.sleep(3)
    button.click()
#     #                                                                 #fill the EYE plateform
# # #                      # Locate the <textarea> by its ID  OVERALLFEEDBACK  Technical Completed CODE


    time.sleep(3)
    textarea = driver.find_element(By.ID, "overallFeedback")
    # Clear any existing text in the textarea (optional)
    textarea.clear()
    # Fill the textarea with "hello"
    time.sleep(3)
    textarea.send_keys("hello")

#                                   #------------------------------technical eye fill  field  completed  success array patern  ------------------#

    # Sample list of dictionaries
    my_list = [
        {
            "observation": "This is an observation.",
            "areaofDev": "I need to improve time management.",
            "strength": "My strength is persistence."
            
        },
        {
            "observation": "This is an observation 1234.",
            "areaofDev": "I need to improve time management 23333.",
            "strength": "My strength is persistence 111."
        },
        {
            "observation": "This is an observation trainnnn.",
            "areaofDev": "I need to improve time management bus.",
            "strength": "My strength is persistence dddddddd."
        },
        {
             "observation": "This is an observation food.",
            "areaofDev": "I need to improve time management full.",
            "strength": "My strength is persistence dffds."
        },
        {
            "observation": "This is an observationdddd.",
            "areaofDev": "I need to improve time management fast.",
            "strength": "My strength is persistence success."
        }
    ]   

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)

    # Loop through the list of dictionaries (my_list) and process each section
    for index, section_data in enumerate(my_list):
        try:
            print(f"Processing section {index + 1}...")

            # Loop through each key-value pair in the current section's dictionary
            for key, value in section_data.items():
                # Build an XPath to locate the textarea for the current section by index
                # Assuming each section has its own set of textareas but the IDs are reused across sections
                # We use XPath to locate textareas by section index and ID or label
                
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
            print(f"Error processing section {index + 1}: {e}")


    # Locate the <textarea> using XPath
    time.sleep(3)
    textarea = driver.find_element(By.XPATH, "//textarea[@name='areaforDev']")
    # Clear and fill the textarea
    textarea.clear()
    time.sleep(3)
    textarea.send_keys("win")



    # Locate the <textarea> using XPath
    time.sleep(3)
    textarea = driver.find_element(By.XPATH, "//textarea[@name='recLearnInitiative']")
    # Clear and fill the textarea
    textarea.clear()
    time.sleep(3)
    textarea.send_keys("Perfect")





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
    time.sleep(3)
    button.click()



                                 #-------------click DOWNLOAD 2 options   #download both --------technical completed
                                      #-------click CV and phycology






    
            #----first click--cv-----------success
#    # Locate the <a> element inside the <button> using its class
    link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn']/a[@class='dropdown-item btn']"))
    )
    link.click()
    time.sleep(3)
    #print error message
    error_message_xpath = '//div[@class="dmx-notify-message"]'
    error_message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, error_message_xpath))
    )
    
    # Print the error message
    print(error_message_element.text)

#     #------------------second click is not working



#     button_xpath = '//button[contains(@dmx-on:click, "run({condition:{outputType:\'boolean\',if:`psyco_report_path==null`")]'

# # Wait for the button to be clickable and then click it

#     button_element = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, button_xpath))
#     )
#     button_element.click()
#     print("Button clicked successfully!")







# #                                                                     #       DOWNLOAD  Technical Completed field download Click  success


    # Wait for the dropdown button to be clickable and click it to open the dropdown ----------FIRST DOWNLOAD----success
    dropdown_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='btn' and @data-bs-toggle='dropdown']"))
    )
    time.sleep(3)
    dropdown_button.click()

    # Wait for the dropdown menu to be visible
    dropdown_menu = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//ul[@class='dropdown-menu show']"))
    )
    # Wait until the "Download With Comment" button is clickable
    download_with_comment_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "btnWithCmmt"))
    )
    # Click the "Download With Comment" button
    time.sleep(4)
    download_with_comment_button.click()



     # Wait for the dropdown button to be clickable and click it to open the dropdown ---------------SECOND DOWNLOAD---success
    dropdown_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='btn' and @data-bs-toggle='dropdown']"))
    )
    time.sleep(5)
    dropdown_button.click()

    button_xpath = '//button[@id="btnWithoutCmmt" and contains(text(), "Download Without Comment")]'
        # Wait for the button to be clickable
    button_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, button_xpath))
    )
    
    # Click the button
    time.sleep(5)
    button_element.click()
    time.sleep(15)














#                                                  # -------open leadership link   --------  # click leadership 




    

  # Increase wait time to handle slower loading elements
    time.sleep(5)
    leadership_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/leadership"]')))
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", leadership_link)
    
    # Click the link
    time.sleep(5)
    leadership_link.click()

#                                           ##   --------------     upcoming applying filter success leadership




    # Click the button
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





 # Find the username field and enter email
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("Rekha")
    time.sleep(4)
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

#                                                                              #1st Anaylitic-skills
         #----------------------#---------------# leadership upcoming------ fill the form all field with the for loop in ARRAY 




                         

    # Sample list of dictionaries
    my_list = [
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
            "areaOfDevelopment": "I need to improve time  THANKS."
        },
        {
            "observation": "This is an PASSED.",
            "strength": "My strength is PERFECT.",
            "areaOfDevelopment": "I need to improve time CORRECTLY 55555555."
        }
    ]

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)

    # ---- First Section ---- #
    try:
        first_section_data = my_list[0]  # First dictionary data
        for key, value in first_section_data.items():
            # Locate the textarea using its ID
            textarea = wait.until(EC.presence_of_element_located((By.NAME, key)))

            # Scroll the textarea into view if necessary
            driver.execute_script("arguments[0].scrollIntoView(true);", textarea)

            # Clear the field and input the value
            textarea.clear()
            time.sleep(3)  # Optional wait
            textarea.send_keys(value)
    except Exception as e:
        print(f"Error processing first section: {e}")

    # Handle radio button and save action to move to the second section
    try:
        # Locate the radio button and Save & Next button
        radio_button = wait.until(EC.element_to_be_clickable((By.ID, "score3")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button)
        time.sleep(3)
        radio_button.click()
        
        save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
        time.sleep(3)
        save_next_button.click()
        time.sleep(4)  # Wait for the second section to load
    except Exception as e:
        print(f"Error during radio button or save action: {e}")

    # ---- Second Section ---- #
    try:
        second_section_data = my_list[1]  # Second dictionary data
        for key, value in second_section_data.items():
            textarea = wait.until(EC.presence_of_element_located((By.NAME, key)))
            driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
            textarea.clear()
            time.sleep(3)
            textarea.send_keys(value)
    except Exception as e:
        print(f"Error processing second section: {e}")

    # Handle Save & Next to move to the third section
    try:
        save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
        time.sleep(3)
        save_next_button.click()
        time.sleep(4)  # Wait for the third section to load
    except Exception as e:
        print(f"Error during save action for second section: {e}")

    # ---- Third Section ---- #
    try:
        third_section_data = my_list[2]  # Third dictionary data
        for key, value in third_section_data.items():
            textarea = wait.until(EC.presence_of_element_located((By.NAME, key)))
            driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
            textarea.clear()
            time.sleep(3)
            textarea.send_keys(value)
    except Exception as e:
        print(f"Error processing third section: {e}")

    # Handle Save & Next to move to the fourth section
    try:
        save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
        time.sleep(3)
        save_next_button.click()
        time.sleep(4)  # Wait for the fourth section to load
    except Exception as e:
        print(f"Error during save action for third section: {e}")

    # ---- Fourth Section ---- #
    try:
        fourth_section_data = my_list[3]  # Fourth dictionary data
        for key, value in fourth_section_data.items():
            textarea = wait.until(EC.presence_of_element_located((By.NAME, key)))
            driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
            textarea.clear()
            time.sleep(3)
            textarea.send_keys(value)
    except Exception as e:
        print(f"Error processing fourth section: {e}")

    # Handle Save & Next to move to the fifth section
    try:
        save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
        time.sleep(3)
        save_next_button.click()
        time.sleep(4)  # Wait for the fifth section to load
    except Exception as e:
        print(f"Error during save action for fourth section: {e}")

    # ---- Fifth Section ---- #
    try:
        fifth_section_data = my_list[4]  # Fifth dictionary data
        for key, value in fifth_section_data.items():
            textarea = wait.until(EC.presence_of_element_located((By.NAME, key)))
            driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
            textarea.clear()
            time.sleep(3)
            textarea.send_keys(value)
    except Exception as e:
        print(f"Error processing fifth section: {e}")

#                                                                 #submit button leadership is not aalow


#     # # Wait until the button inside the div with id="conditional2" is clickable
#     # submit_button = WebDriverWait(driver, 10).until(
#     #     EC.element_to_be_clickable((By.XPATH, "//div[@id='conditional2']//button"))
#     # )

#     # # Click the submit button
#     # submit_button.click()

#     # # Locate the button using XPath
#     # submit_button = driver.find_element(By.XPATH, "//div[@id='conditional2']//button")

#     # # Click the submit button
#     # submit_button.click()


                                                                                #  click CV is not working




   
#     # Locate the button using XPath and click it
#     button = driver.find_element(By.XPATH, "//button[@class='btn border-1 accent accentBorder']")
#     time.sleep(3)
#     button.click()


# # Wait for the notification message to appear
#     cv_error_element = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
#     )
    
#     # Print the CV error message
#     print("CV Error Message:", cv_error_element.text)


                                                                     # second click physcometric is -------success

    # Wait for the button to be clickable and click it
    psychometric_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn') and .//div[text()='Psychometric']]"))
    )
    psychometric_button.click()  # Click the button



    # Wait for the notification message to appear
    error_message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
    )
    
    # Print the error message text
    time.sleep(3)
    print("Error Message:", error_message_element.text)

                                                                             

#                                                                         # --------------leadership  and completed click----






#                                 #-------Click Leadershi AND  COMPLETED click






    # Increase wait time to handle slower loading elements
    time.sleep(4)
    technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/leadership"]')))
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    
    # Click the link
    technical_link.click()
    time.sleep(2)
        # Find the <a> element by its XPath
    completed_button = driver.find_element(By.XPATH, "//div[@id='complete']//a[contains(text(),'Completed')]")

    # Click the "Completed" link
    time.sleep(3)
    completed_button.click()


#     ## click filter apply filters success




    # Click the button
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







 # Find the username field and enter email
    time.sleep(2)
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("Tara")
    time.sleep(4)




        # Locate the button using XPath
    button = driver.find_element(By.XPATH, "//button[@data-bs-toggle='offcanvas' and @data-bs-target='#offcanvas1']")

    # Click the button
    time.sleep(3)
    button.click()


    time.sleep(3)
    textarea = driver.find_element(By.ID, "overallFeedback")
    # Clear any existing text in the textarea (optional)
    textarea.clear()
    # Fill the textarea with "hello"
    time.sleep(3)
    textarea.send_keys("Welcome")


# ---------------------------#-----------------------------------#leadership fill the eye form with the array helps   --------------------------#

    # Sample list of dictionaries array
    my_list = [
        {
            "observation": "This is an observation.",
            "areaofDev": "I need to improve time management.",
            "strength": "My strength is persistence."
            
        },
        {
            "observation": "This is an observation 1234.",
            "areaofDev": "I need to improve time management 23333.",
            "strength": "My strength is persistence 111."
        },
        {
            "observation": "This is an observation trainnnn.",
            "areaofDev": "I need to improve time management bus.",
            "strength": "My strength is persistence don."
        },
        {
             "observation": "This is an observation food.",
            "areaofDev": "I need to improve time management full.",
            "strength": "My strength is persistence drift."
        },
        {
            "observation": "This is an observationdddd.",
            "areaofDev": "I need to improve time management fast.",
            "strength": "My strength is persistence success."
        }
    ]   

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)

    # Loop through the list of dictionaries (my_list) and process each section
    for index, section_data in enumerate(my_list):
        try:
            print(f"Processing section {index + 1}...")

            # Loop through each key-value pair in the current section's dictionary
            for key, value in section_data.items():
                # Build an XPath to locate the textarea for the current section by index
                # Assuming each section has its own set of textareas but the IDs are reused across sections
                # We use XPath to locate textareas by section index and ID or label
                
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
            print(f"Error processing section {index + 1}: {e}")

    # ----------------=--------Locate the <textarea> using XPath
    time.sleep(3)
    textarea = driver.find_element(By.XPATH, "//textarea[@name='areaforDev']")
    # Clear and fill the textarea
    textarea.clear()
    time.sleep(3)
    textarea.send_keys("Fixed")



    # Locate the <textarea> using XPath
    time.sleep(3)
    textarea = driver.find_element(By.XPATH, "//textarea[@name='recLearnInitiative']")
    # Clear and fill the textarea
    textarea.clear()
    time.sleep(3)
    textarea.send_keys("Correct")

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

#--------------cv is not working



##-----------click psyco------leadership------complete is not--------worked




    # try:
    #     # Wait until the button is clickable and then click it
    #     button = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn p-1') and contains(@dmx-on:click, 'psyco_report_path')]"))
    #     )
        
    #     # Click the button
    #     button.click()
    #     print("Button clicked successfully.")

    # except Exception as e:
    #     print(f"Error occurred: {e}")





                                                                    #------------mindset click success-----------#


                                
    try:
        # Wait until the link is clickable and then click it
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'nav-link') and contains(., 'Mindset')]"))
        )
        
        # Click the link
        link.click()
        print("Link clicked successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")   



        
 # Find the username field and enter email
    time.sleep(2)
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("Radhika")
    time.sleep(4)    



#---------------mindset DOWNLOAD PROCESS SUCCESSFULLY----------------#



    try:
        # Wait until the dropdown button is clickable and click it
        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn my-0 py-0' and @data-bs-toggle='dropdown']"))
        )
        time.sleep(3)
        dropdown_button.click()
        print("Dropdown button clicked successfully.")

        # Wait until the dropdown item "Download in English" is visible and click it
        download_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Download in English')]"))
        )
        time.sleep(3)
        download_link.click()
        print("Download link clicked successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")

    try:
        # Wait until the dropdown button is clickable and click it
        dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn my-0 py-0' and @data-bs-toggle='dropdown']"))
        )
        time.sleep(3)
        dropdown_button.click()
        print("Dropdown button clicked successfully.")

        # Wait until the dropdown item "تحميل باللغة العربية" is visible and click it
        download_link_arabic = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'تحميل باللغة العربية')]"))
        )
        time.sleep(3)
        download_link_arabic.click()
        print("Download link in Arabic clicked successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")








#             #-----------------REPORT DOWNLOAD PROCESS
#              ---------------    ----------------------------  #Click Report Link  # And COMPLETED CLICK and Download Process


   
    # Wait for the "Report" link to be clickable
    wait = WebDriverWait(driver, 10)
    report_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/report/reports']")))
#    Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", report_link)
    
    # Click the "Report" link
    time.sleep(3)
    report_link.click()


# Wait until the "Partial" link is visible and clickable
    partial_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Partial')]"))
    )
    partial_link.click()
#---------------click filter
    filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "collapseFilter"))
    )
    filter_button.click()



    try:
        # Wait until the dropdown is present
        dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nomPosIdFilter_ID"))  # Replace with your actual dropdown ID
        )
        
        # Create a Select object for the dropdown
        time.sleep(3)
        select = Select(dropdown)
        
   
        # Select the option "Data Scientist II"
        time.sleep(3)
        select.select_by_visible_text("Data Scientist II")
        print("Option 'Data Scientist II' selected successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")

    try:
        # Wait until the button is clickable
        apply_filters_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "applyFilterId"))  # Replace with the button's ID
        )
        
        # Click the "Apply Filters" button
        time.sleep(3)
        apply_filters_button.click()
        print("Clicked 'Apply Filters' button successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")


     # Find the username field and enter email
    time.sleep(3)
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("Shweta")
    time.sleep(3)

    #----click eye success

    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn' and @type='button']")))
    # Click the button
    time.sleep(3)
    button.click()

    
    # Wait for the button to be clickable and then click it--- --download with comment----first-----
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'daa_button') and @type='button']")))

    # Click the button
    time.sleep(3)
    button.click()
    time.sleep(10)



    # Wait for the button to be clickable and then click it--- --download without comment----second----
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'daa_button') and contains(., 'Download without Comment')]")))
        
        # Perform the click
    time.sleep(3)
    button.click()







    #--------------report click and complete-----click-------


    # Wait for the "Report" link to be clickable
    wait = WebDriverWait(driver, 10)
    report_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/report/reports']")))
#    Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", report_link)
    
    # Click the "Report" link
    time.sleep(3)
    report_link.click()


#-----------click filter completed

#---------------click filter
    filter_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "collapseFilter"))
    )
    filter_button.click()



    try:
        # Wait until the dropdown is present
        dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "nomPosIdFilter_ID"))  # Replace with your actual dropdown ID
        )
        
        # Create a Select object for the dropdown
        time.sleep(3)
        select = Select(dropdown)
        
   
        # Select the option "Data Scientist II"
        time.sleep(3)
        select.select_by_visible_text("Data Scientist II")
        print("Option 'Data Scientist II' selected successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")

    try:
        # Wait until the button is clickable
        apply_filters_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "applyFilterId"))  # Replace with the button's ID
        )
        
        # Click the "Apply Filters" button
        time.sleep(3)
        apply_filters_button.click()
        print("Clicked 'Apply Filters' button successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")



#-----

     # Find the username field and enter email
    time.sleep(3)
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("Tara")
    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn' and @type='button']")))
    # Click the button
    time.sleep(3)
    button.click()


    # Wait for the button to be clickable and then click it --------DOWNLOAD FIRST
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'daa_button') and @type='button']")))

    # Click the button
    time.sleep(3)
    button.click()
    time.sleep(10)


    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'daa_button') and contains(., 'Download without Comment')]")))
        
        # Perform the click
    time.sleep(3)
    button.click()




    #----------
    time.sleep(15)  # Wait for 15 seconds to view results
finally:
    # Close the browser
    driver.quit()  # Ensure the browser closes
