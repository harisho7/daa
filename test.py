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

                                                        #click Technical link


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
                                                                          # UPCOMING FILL THE ALL FORM
 # Find the username field and enter email
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("Neha")
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


#                                                                 #1st Coading knowlwdge



#       # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "observation")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()

#     # Send the text "hello" to the textarea
#     time.sleep(3)
#     textarea.send_keys("Hello")
#      # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "strength")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "thanks" to the textarea
#     time.sleep(3)
#     textarea.send_keys("World")

#         # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "areaOfDevelopment")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()

#     # Send the text "people" to the textarea
#     time.sleep(3)
#     textarea.send_keys("people")
#     time.sleep(3)
#     radio_button = wait.until(EC.element_to_be_clickable((By.ID, "score3")))

#     # Scroll the radio button into view
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button)
#     time.sleep(3)  # Wait for a 3 second
#     radio_button.click()
#     time.sleep(3)
#     save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))

#     # Scroll the button into view if needed
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)

#     # Click the button
#     time.sleep(3)
#     save_next_button.click()
#     time.sleep(4)

# #                                                             # 2nd Concept knowledge





#      # Locate the textarea by its ID
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "observation")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "hello" to the textarea
#     time.sleep(3)
#     textarea.send_keys("Enjoy")

#      # Locate the textarea by its ID
#     time.sleep(2)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "strength")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "thanks" to the textarea
#     time.sleep(3)
#     textarea.send_keys("Happy")

#         # Locate the textarea by its ID
#     time.sleep(2)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "areaOfDevelopment")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "people" to the textarea
#     time.sleep(3)
#     textarea.send_keys("Sad")


  
#     time.sleep(3)
#     radio_button = wait.until(EC.element_to_be_clickable((By.ID, "score3")))
#     # Scroll the radio button into view
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button)
#     time.sleep(3)  # Wait for a second
#     radio_button.click()
#     time.sleep(3)
#     save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
#     # Scroll the button into view if needed
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
#     # Click the button
#     time.sleep(3)
#     save_next_button.click()
    

# #                                                                               # 3rd project knowlwdge



#      # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "observation")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "hello" to the textarea
#     time.sleep(3)
#     textarea.send_keys("Python")

#      # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "strength")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "thanks" to the textarea
#     time.sleep(3)
#     textarea.send_keys("killer")

#         # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "areaOfDevelopment")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "people" to the textarea
#     time.sleep(3)
#     textarea.send_keys("Selenium")


  
#     time.sleep(3)
#     radio_button = wait.until(EC.element_to_be_clickable((By.ID, "score3")))
#     # Scroll the radio button into view
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button)
#     time.sleep(3)  # Wait for a second
#     radio_button.click()
#     time.sleep(3)
#     save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
#     # Scroll the button into view if needed
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
#     # Click the button
#     time.sleep(3)
#     save_next_button.click()
   

# #                                                                            # 4th Team collabration





#      # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "observation")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "hello" to the textarea
#     time.sleep(3)
#     textarea.send_keys("W3school")
  

#      # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "strength")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "thanks" to the textarea
#     time.sleep(3)
#     textarea.send_keys("HTML")
    

#         # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "areaOfDevelopment")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "people" to the textarea
#     time.sleep(3)
#     textarea.send_keys("PHP")
   
#     time.sleep(3)
#     radio_button = wait.until(EC.element_to_be_clickable((By.ID, "score3")))
#     # Scroll the radio button into view
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button)
#     time.sleep(3)  # Wait for a second
#     radio_button.click()
#     time.sleep(3)
#     save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
#     # Scroll the button into view if needed
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)
#     # Click the button
#     time.sleep(3)
#     save_next_button.click()
   

# #                                                                       # 5th technical skill



#      # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "observation")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "hello" to the textarea
#     time.sleep(3)
#     textarea.send_keys("Joker")
    

#      # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "strength")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "thanks" to the textarea
#     time.sleep(3)
#     textarea.send_keys("Poter")


#         # Locate the textarea by its ID
#     time.sleep(3)
#     textarea = wait.until(EC.presence_of_element_located((By.ID, "areaOfDevelopment")))
#     # Scroll the textarea into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
#     textarea.clear()
#     # Send the text "people" to the textarea
#     time.sleep(3)
#     textarea.send_keys("Run")
    


  
#     time.sleep(3)
#     radio_button = wait.until(EC.element_to_be_clickable((By.ID, "score3")))
#     # Scroll the radio button into view
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_button)

#     time.sleep(3)  # Wait for a second
#     radio_button.click()




                                                                #  #click CV
                                                                #  first click

    # Locate the button using XPath and click it
    button = driver.find_element(By.XPATH, "//button[@class='btn border-1 accent accentBorder']")
    time.sleep(3)
    button.click()


# Wait for the notification message to appear
    cv_error_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
    )
    
    # Print the CV error message
    print("CV Error Message:", cv_error_element.text)
    


    #                                                                   second click physcometric

    # # Find the element by XPath and click
    # psychometric_element = driver.find_element(By.XPATH, "//a[contains(@class, 'dropdown-item') and contains(., 'Psychometric')]")
    # psychometric_element.click()

    
    # # Click the button
    # time.sleep(3)
    # psychometric_element.click()

    # error_message_element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
    #     )
    #     # Print the error message text
    # print("Error message:", error_message_element.text)



   

 
    # # Wait for the notification message to appear
    # error_message_element = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.XPATH, "//div[@class='dmx-notify-message']"))
    # )
    
    # # Print the error message text  
    # time.sleep(3)
    # print("Error Message:", error_message_element.text)

    


#                     #submit all fields technical skills


#     #  # Wait for the "Submit" button to be clickable and then click it
#     # submit_button = wait.until(
#     #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'div#conditional2 button[type="submit"]'))
#     # )
#     # submit_button.click()


#                            # open leadership link                                                  # click leadership 



#   # Increase wait time to handle slower loading elements
#     technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/leadership"]')))
    
#     # Scroll the element into view
#     driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    
#     # Click the link
#     time.sleep(3)
#     technical_link.click()



#  # Find the username field and enter email
#     username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
#     username_field.send_keys("Tina")
#     time.sleep(4)
#     # Optional: keep the window open for a few seconds to view results
#  # Wait for the button with class 'btn' and 'p-1' to be clickable
#     button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.p-1")))
    
#     # Scroll the button into view (if necessary)
#     driver.execute_script("arguments[0].scrollIntoView(true);", button)
    
#     # Click the button
#     time.sleep(3)
#     button.click()

#     time.sleep(4)


#        # Locate the anchor tag with the class 'lb-close'
#     close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "lb-close")))
    
#     # Scroll the element into view if necessary
#     driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
    
#     # Click the anchor element
#     time.sleep(4)
#     close_button.click()

#                                                                              #1st Anaylitic-skills

#      # Wait until the textarea is visible (in case it takes time to load)
#     textarea = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='observation']"))
#     )

#     textarea.clear()
    
#     # Fill in the textarea with the desired text
#     time.sleep(2)
#     textarea.send_keys("box")
#     time.sleep(3)

   
#     # Wait until the textarea is visible
#     textarea_strength = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='strength']"))
#     )

#     # Clear any existing text in the textarea (optional)
#     textarea_strength.clear()

#     # Fill in the textarea with the desired text
#     time.sleep(2)
#     textarea_strength.send_keys("fill")

#         # Wait until the textarea is visible
#     textarea_area_of_dev = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='areaOfDevelopment']"))
#     )

#     # Clear any existing text in the textarea (optional)
#     textarea_area_of_dev.clear()

#     # Fill in the textarea with the desired text
#     time.sleep(3)
#     textarea_area_of_dev.send_keys("Full")


  

#  # Wait until the radio button is visible and clickable
#     radio_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "score3"))
#     )
#     # Click the radio button
#     time.sleep(3)
#     radio_button.click()

#     save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))

#     # Scroll the button into view if needed
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)

#     # Click the button
#     time.sleep(3)
#     save_next_button.click()
#     time.sleep(3)


# #                                             # 2nd Communication-skills





#      # Wait until the textarea is visible (in case it takes time to load)
#     textarea = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='observation']"))
#     )
#     textarea.clear()
#     # Fill in the textarea with the desired text
#     time.sleep(3)
#     textarea.send_keys("Elephant")
#     time.sleep(3)

   
#     # Wait until the textarea is visible
#     textarea_strength = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='strength']"))
#     )

#     # Clear any existing text in the textarea (optional)
#     textarea_strength.clear()

#     # Fill in the textarea with the desired text
#     time.sleep(3)
#     textarea_strength.send_keys("Arrow")
#     time.sleep(3)

#         # Wait until the textarea is visible
#     textarea_area_of_dev = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='areaOfDevelopment']"))
#     )

#     # Clear any existing text in the textarea (optional)
#     textarea_area_of_dev.clear()

#     # Fill in the textarea with the desired text
#     time.sleep(3)
#     textarea_area_of_dev.send_keys("Rock")
#     time.sleep(3)


  

#  # Wait until the radio button is visible and clickable
#     radio_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "score3"))
#     )
#     # Click the radio button
#     time.sleep(3)
#     radio_button.click()
#     time.sleep(2)

#     save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))

#     # Scroll the button into view if needed
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)

#     # Click the button
#     time.sleep(3)
#     save_next_button.click()
#     time.sleep(3)

# #                                                                  # 3rd Leadership-skills



#      # Wait until the textarea is visible (in case it takes time to load)
#     textarea = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='observation']"))
#     )
#     textarea.clear()
#     # Fill in the textarea with the desired text
#     time.sleep(3)
#     textarea.send_keys("Lion")
#     time.sleep(3)

   
#     # Wait until the textarea is visible
#     textarea_strength = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='strength']"))
#     )

#     # Clear any existing text in the textarea (optional)
#     textarea_strength.clear()

#     # Fill in the textarea with the desired text
#     time.sleep(3)
#     textarea_strength.send_keys("Jack")
#     time.sleep(3)

#         # Wait until the textarea is visible
#     textarea_area_of_dev = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='areaOfDevelopment']"))
#     )

#     # Clear any existing text in the textarea (optional)
#     textarea_area_of_dev.clear()

#     # Fill in the textarea with the desired text
#     time.sleep(3)
#     textarea_area_of_dev.send_keys("Kill")
#     time.sleep(3)


  

#  # Wait until the radio button is visible and clickable
#     radio_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "score3"))
#     )
#     # Click the radio button
#     time.sleep(3)
#     radio_button.click()
#     time.sleep(2)

#     save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))

#     # Scroll the button into view if needed
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)

#     # Click the button
#     time.sleep(2)
#     save_next_button.click()
    


# #                                                                              # 4th Problem-solving-skills



#      # Wait until the textarea is visible (in case it takes time to load)
#     time.sleep(3)
#     textarea = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='observation']"))
#     )
#     textarea.clear()
#     # Fill in the textarea with the desired text
#     time.sleep(2)
#     textarea.send_keys("Shadow")

   
#     # Wait until the textarea is visible
#     time.sleep(3)
#     textarea_strength = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='strength']"))
#     )
#     # Clear any existing text in the textarea (optional)
#     textarea_strength.clear()
#     # Fill in the textarea with the desired text
#     time.sleep(2)
#     textarea_strength.send_keys("Perfect")

#         # Wait until the textarea is visible
#     time.sleep(3)
#     textarea_area_of_dev = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='areaOfDevelopment']"))
#     )
#     # Clear any existing text in the textarea (optional)
#     textarea_area_of_dev.clear()
#     # Fill in the textarea with the desired text
#     time.sleep(2)
#     textarea_area_of_dev.send_keys("Trigger")


  

#  # Wait until the radio button is visible and clickable
#     time.sleep(3)
#     radio_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "score3"))
#     )
#     # Click the radio button
#     time.sleep(2)
#     radio_button.click()
#     time.sleep(3)
#     save_next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save & Next')]")))
#     # Scroll the button into view if needed
#     driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_next_button)

#     # Click the button
#     time.sleep(2)
#     save_next_button.click()
    


# #                                                                      # 5th Innovation-skill



#      # Wait until the textarea is visible (in case it takes time to load)
#     time.sleep(3)
#     textarea = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='observation']"))
#     )
#     textarea.clear()
#     # Fill in the textarea with the desired text
#     time.sleep(2)
#     textarea.send_keys("Horror")

   
#     # Wait until the textarea is visible
#     time.sleep(3)
#     textarea_strength = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='strength']"))
#     )
#     # Clear any existing text in the textarea (optional)
#     textarea_strength.clear()
#     # Fill in the textarea with the desired text
#     time.sleep(3)
#     textarea_strength.send_keys("Thrill")

#         # Wait until the textarea is visible
#     time.sleep(3)
#     textarea_area_of_dev = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[name='areaOfDevelopment']"))
#     )
#     # Clear any existing text in the textarea (optional)
#     textarea_area_of_dev.clear()
#     # Fill in the textarea with the desired text
#     time.sleep(3)
#     textarea_area_of_dev.send_keys("Crime")


#  # Wait until the radio button is visible and clickable
#     time.sleep(3)
#     radio_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.ID, "score3"))
#     )
#     # Click the radio button
#     time.sleep(3)
#     radio_button.click()
    
#                                                                 #submit button leadership


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


#                                                                         # click technical and completed click




#     # Increase wait time to handle slower loading elements
#     time.sleep(4)
#     technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/technical"]')))
    
#     # Scroll the element into view
#     driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    
#     # Click the link
#     technical_link.click()
#     time.sleep(2)
#         # Find the <a> element by its XPath
#     completed_button = driver.find_element(By.XPATH, "//div[@id='complete']//a[contains(text(),'Completed')]")

#     # Click the "Completed" link
#     time.sleep(3)
#     completed_button.click()


#  # Find the username field and enter email
#     time.sleep(2)
#     username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
#     username_field.send_keys("Aman")
#     time.sleep(4)
#         # Locate the button using XPath
#     button = driver.find_element(By.XPATH, "//button[@data-bs-toggle='offcanvas' and @data-bs-target='#offcanvas1']")

#     # Click the button
#     time.sleep(3)
#     button.click()

# #                      # Locate the <textarea> by its ID  OVERALLFEEDBACK  Technical Completed CODE


#     time.sleep(3)
#     textarea = driver.find_element(By.ID, "overallFeedback")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "hello"
#     time.sleep(3)
#     textarea.send_keys("hello")

# #         # Locate the <textarea> by its ID                   1st Coading Knowledge

#     time.sleep(3)
#     textarea = driver.find_element(By.ID, "observation")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "world"
#     time.sleep(3)
#     textarea.send_keys("world")

#     time.sleep(3)
#     textarea = driver.find_element(By.ID, "areaofDev")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "world"
#     time.sleep(3)
#     textarea.send_keys("small")


#     time.sleep(3)
#     textarea = driver.find_element(By.ID, "strength")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "world"
#     time.sleep(3)
#     textarea.send_keys("large")

#                                                 # 2nd Concept Knowledge


    

#     # Locate the unique <textarea> using the 'name' attribute with 'responseRepeat[1]'
#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[1][repeat2][0][observation]']")

#     # Clear any existing text in the textarea (optional)
#     textarea.clear()

#     # Fill the textarea with "aquaman"
#     time.sleep(3)
#     textarea.send_keys("Aquaman")

#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute with 'responseRepeat[1][repeat2][0][areaofDev]'
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[1][repeat2][0][areaofDev]']")

#     # Clear any existing text in the textarea (optional)
#     textarea.clear()

#     # Fill the textarea with "spider"
#     time.sleep(3)
#     textarea.send_keys("spider")



#     time.sleep(3)
#    # Locate the unique <textarea> using the 'name' attribute
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[1][repeat2][0][strength]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "captain"
#     time.sleep(3)
#     textarea.send_keys("Captain")



#     #                                                         # 3rd Project Knowledge






#     time.sleep(3)
    
#     # Locate the unique <textarea> using the 'name' attribute
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[2][repeat2][0][observation]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "Fantastic"
#     time.sleep(3)
#     textarea.send_keys("Fantastic")
#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute with 'responseRepeat[1][repeat2][0][areaofDev]'
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[2][repeat2][0][areaofDev]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "spider"
#     time.sleep(3)
#     textarea.send_keys("Hellin")



#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[2][repeat2][0][strength]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "captain"
#     time.sleep(3)
#     textarea.send_keys("Jung")







#     #                                                 # 4th Team Collabration





#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[3][repeat2][0][observation]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "Fantastic"
#     time.sleep(3)
#     textarea.send_keys("Lie")
#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute with 'responseRepeat[1][repeat2][0][areaofDev]'
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[3][repeat2][0][areaofDev]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "spider"
#     time.sleep(3)
#     textarea.send_keys("Lion")



#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[3][repeat2][0][strength]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "captain"
#     time.sleep(3)
#     textarea.send_keys("Link")


#     #                                                             # 5th Technical Skills






#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[4][repeat2][0][observation]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "Fantastic"
#     time.sleep(3)
#     textarea.send_keys("Area")
#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute with 'responseRepeat[1][repeat2][0][areaofDev]'
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[4][repeat2][0][areaofDev]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "spider"
#     time.sleep(3)
#     textarea.send_keys("Public")



#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[4][repeat2][0][strength]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "captain"
#     time.sleep(3)
#     textarea.send_keys("yellow")

#     # Locate the <textarea> using XPath
#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='areaforDev']")
#     # Clear and fill the textarea
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("win")



#     # Locate the <textarea> using XPath
#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='recLearnInitiative']")
#     # Clear and fill the textarea
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("Perfect")





#                                             #Technical completed code submit code
#     # Locate the button using XPath
#     submit_button = driver.find_element(By.XPATH, "//button[@id='submitResponse']")

#     # Click the submit button
#     time.sleep(3)
#     submit_button.click()

#    # Locate the button using XPath close button completed
#     time.sleep(10)
#     button = driver.find_element(By.XPATH, "//button[@type='button' and @class='btn-close text-reset' and @aria-label='Close']")
#     # Click the button
#     time.sleep(3)
#     button.click()






#                                 #Click Leadershi AND  COMPLETED click






#     # Increase wait time to handle slower loading elements
#     time.sleep(4)
#     technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/leadership"]')))
    
#     # Scroll the element into view
#     driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    
#     # Click the link
#     technical_link.click()
#     time.sleep(2)
#         # Find the <a> element by its XPath
#     completed_button = driver.find_element(By.XPATH, "//div[@id='complete']//a[contains(text(),'Completed')]")

#     # Click the "Completed" link
#     time.sleep(3)
#     completed_button.click()


#  # Find the username field and enter email
#     time.sleep(2)
#     username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
#     username_field.send_keys("Tara")
#     time.sleep(4)
#         # Locate the button using XPath
#     button = driver.find_element(By.XPATH, "//button[@data-bs-toggle='offcanvas' and @data-bs-target='#offcanvas1']")

#     # Click the button
#     time.sleep(3)
#     button.click()


#     time.sleep(3)
#     textarea = driver.find_element(By.ID, "overallFeedback")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "hello"
#     time.sleep(3)
#     textarea.send_keys("Welcome")


#          # Locate the <textarea> by its ID                   1st Coading Knowledge

#     time.sleep(3)
#     textarea = driver.find_element(By.ID, "observation")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "world"
#     time.sleep(3)
#     textarea.send_keys("India")

#     time.sleep(3)
#     textarea = driver.find_element(By.ID, "areaofDev")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "world"
#     time.sleep(3)
#     textarea.send_keys("Large")


#     time.sleep(3)
#     textarea = driver.find_element(By.ID, "strength")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "world"
#     time.sleep(3)
#     textarea.send_keys("Small")

#                                                 # 2nd Concept Knowledge


    

#     # Locate the unique <textarea> using the 'name' attribute with 'responseRepeat[1]'
#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[1][repeat2][0][observation]']")

#     # Clear any existing text in the textarea (optional)
#     textarea.clear()

#     # Fill the textarea with "aquaman"
#     time.sleep(3)
#     textarea.send_keys("Thing")

#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute with 'responseRepeat[1][repeat2][0][areaofDev]'
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[1][repeat2][0][areaofDev]']")

#     # Clear any existing text in the textarea (optional)
#     textarea.clear()

#     # Fill the textarea with "spider"
#     time.sleep(3)
#     textarea.send_keys("France")



#     time.sleep(3)
#    # Locate the unique <textarea> using the 'name' attribute
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[1][repeat2][0][strength]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "captain"
#     time.sleep(3)
#     textarea.send_keys("America")



#     #                                                         # 3rd Project Knowledge






#     time.sleep(3)
    
#     # Locate the unique <textarea> using the 'name' attribute
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[2][repeat2][0][observation]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "Fantastic"
#     time.sleep(3)
#     textarea.send_keys("Train")
#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute with 'responseRepeat[1][repeat2][0][areaofDev]'
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[2][repeat2][0][areaofDev]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "spider"
#     time.sleep(3)
#     textarea.send_keys("Bus")



#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[2][repeat2][0][strength]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "captain"
#     time.sleep(3)
#     textarea.send_keys("Car")







#     #                                                 # 4th Team Collabration





#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[3][repeat2][0][observation]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "Fantastic"
#     time.sleep(3)
#     textarea.send_keys("Like")
#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute with 'responseRepeat[1][repeat2][0][areaofDev]'
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[3][repeat2][0][areaofDev]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "spider"
#     time.sleep(3)
#     textarea.send_keys("Look")



#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[3][repeat2][0][strength]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "captain"
#     time.sleep(3)
#     textarea.send_keys("Linkdin")


#                                                 # 5th Technical Skills






#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[4][repeat2][0][observation]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "Fantastic"
#     time.sleep(3)
#     textarea.send_keys("Queen")
#     time.sleep(3)
#     # Locate the unique <textarea> using the 'name' attribute with 'responseRepeat[1][repeat2][0][areaofDev]'
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[4][repeat2][0][areaofDev]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "spider"
#     time.sleep(3)
#     textarea.send_keys("Fox")



#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='responseRepeat[4][repeat2][0][strength]']")
#     # Clear any existing text in the textarea (optional)
#     textarea.clear()
#     # Fill the textarea with "captain"
#     time.sleep(3)
#     textarea.send_keys("Well")

#     # Locate the <textarea> using XPath
#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='areaforDev']")
#     # Clear and fill the textarea
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("Fixed")



#     # Locate the <textarea> using XPath
#     time.sleep(3)
#     textarea = driver.find_element(By.XPATH, "//textarea[@name='recLearnInitiative']")
#     # Clear and fill the textarea
#     textarea.clear()
#     time.sleep(3)
#     textarea.send_keys("Correct")

# #                                             # leadership completed code with submit code
   

#  # Locate the button using XPath
#     submit_button = driver.find_element(By.XPATH, "//button[@id='submitResponse']")

#     # Click the submit button
#     time.sleep(3)
#     submit_button.click()

#    # Locate the button using XPath close button completed
#     time.sleep(10)
#     button = driver.find_element(By.XPATH, "//button[@type='button' and @class='btn-close text-reset' and @aria-label='Close']")
#     # Click the button
#     time.sleep(3)
#     button.click()



#                                              #     #       #       DOWNLOAD PROCESS START for TECHNICAL 



#                                                    #     # click Technical link 


#     # Optional: Switch to iframe if necessary
#     iframes = driver.find_elements(By.TAG_NAME, 'iframe')
#     if iframes:
#         print(f"Found {len(iframes)} iframe(s), switching to the first one.")
#         driver.switch_to.frame(iframes[0])

#     # Increase wait time to handle slower loading elements
#     technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/technical"]')))
    
#     # Scroll the element into view
#     driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    
#     # Click the link
#     time.sleep(5)
#     technical_link.click()
#     time.sleep(3)
    
#        # Find the <a> element by its XPath                              #Click Technical Completed

#     completed_button = driver.find_element(By.XPATH, "//div[@id='complete']//a[contains(text(),'Completed')]")

#     # Click the "Completed" link
#     time.sleep(3)
#     completed_button.click()
#     time.sleep(3)

#  # Find the username field and enter email
#     username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
#     username_field.send_keys("Aman")
#     time.sleep(3)

#                                                                     #       DOWNLOAD  Technical Completed click and  field download Click download


#     # Wait for the dropdown button to be clickable and click it to open the dropdown
#     dropdown_button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='btn' and @data-bs-toggle='dropdown']"))
#     )
#     time.sleep(3)
#     dropdown_button.click()

#     # Wait for the dropdown menu to be visible
#     dropdown_menu = WebDriverWait(driver, 20).until(
#         EC.visibility_of_element_located((By.XPATH, "//ul[@class='dropdown-menu show']"))
#     )
#     # Wait until the "Download With Comment" button is clickable
#     download_with_comment_button = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "btnWithCmmt"))
#     )
#     # Click the "Download With Comment" button
#     time.sleep(4)
#     download_with_comment_button.click()
#     time.sleep(10)


#             #   REPORT DOWNLOAD PROCESS
#                                                                     #Click Report Link  # And COMPLETED CLICK and Download Process


   
#     # Wait for the "Report" link to be clickable
#     wait = WebDriverWait(driver, 10)
#     report_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/report/reports']")))
# #    Scroll the element into view
#     driver.execute_script("arguments[0].scrollIntoView(true);", report_link)
    
#     # Click the "Report" link
#     time.sleep(3)
#     report_link.click()


#      # Find the username field and enter email
#     time.sleep(3)
#     username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
#     username_field.send_keys("Rohit")
#     time.sleep(3)

#     wait = WebDriverWait(driver, 10)
#     button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn' and @type='button']")))
#     # Click the button
#     time.sleep(3)
#     button.click()


#     # Wait for the button to be clickable and then click it
#     wait = WebDriverWait(driver, 10)
#     button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'daa_button') and @type='button']")))

#     # Click the button
#     time.sleep(3)
#     button.click()
#     time.sleep(10)



    time.sleep(15)  # Wait for 15 seconds to view results
finally:
    # Close the browser
    driver.quit()  # Ensure the browser closes
