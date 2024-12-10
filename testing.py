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
                 "username": "134"
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




#----report click
    
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
        # Locate the button by ID and click it
        button = driver.find_element(By.ID, "idRedirectIndividualPartial")
        button.click()

        print("Button clicked successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(2)

    try:
        # Locate the button by ID and click it
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



    #--eye



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

    #--

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

#--

    try:
        # Locate the button by ID and click it
        button = driver.find_element(By.ID, "idRedirectIndividual")
        button.click()

        print("Button clicked successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(2)

    try:
        # Locate the button by ID and click it
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





    time.sleep(15)  # Wait for 15 seconds to view results
finally:
    # Close the browser
    driver.quit()  # Ensure the browser closes
