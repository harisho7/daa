from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


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
    time.sleep(3)
    password_field.submit()



#                                                         #click Technical link


# #     # Optional: Switch to iframe if necessary
# #     iframes = driver.find_elements(By.TAG_NAME, 'iframe')
# #     if iframes:
# #         print(f"Found {len(iframes)} iframe(s), switching to the first one.")
# #         driver.switch_to.frame(iframes[0])

# #     # Increase wait time to handle slower loading elements
# #     technical_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/technical"]')))
    
# #     # Scroll the element into view
# #     driver.execute_script("arguments[0].scrollIntoView(true);", technical_link)
    
# #     # Click the link
# #     technical_link.click()
# #     time.sleep(3)
# #        # Find the <a> element by its XPath                              #Click Technical Completed
# #     completed_button = driver.find_element(By.XPATH, "//div[@id='complete']//a[contains(text(),'Completed')]")

# #     # Click the "Completed" link
# #     time.sleep(3)
# #     completed_button.click()
# #     time.sleep(3)

# #  # Find the username field and enter email
# #     username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
# #     username_field.send_keys("Aman")
# #     time.sleep(3)

# #                                                                     #       DOWNLOAD  Technical Completed field download Click


# #     # Wait for the dropdown button to be clickable and click it to open the dropdown
# #     dropdown_button = WebDriverWait(driver, 20).until(
# #         EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='btn' and @data-bs-toggle='dropdown']"))
# #     )
# #     time.sleep(3)
# #     dropdown_button.click()

# #     # Wait for the dropdown menu to be visible
# #     dropdown_menu = WebDriverWait(driver, 20).until(
# #         EC.visibility_of_element_located((By.XPATH, "//ul[@class='dropdown-menu show']"))
# #     )
# #     # Wait until the "Download With Comment" button is clickable
# #     download_with_comment_button = WebDriverWait(driver, 20).until(
# #         EC.element_to_be_clickable((By.ID, "btnWithCmmt"))
# #     )
# #     # Click the "Download With Comment" button
# #     time.sleep(4)
# #     download_with_comment_button.click()

#                                                                     #Click Mindset Link


   

#     # # Increase wait time to handle slower loading elements
#     # mindset_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/mindset"]')))
    
#     # # Scroll the element into view
#     # driver.execute_script("arguments[0].scrollIntoView(true);", mindset_link)
    
#     # # Click the link
#     # time.sleep(3)
#     # mindset_link.click()

#     #  # Find the username field and enter email
#     # time.sleep(3)
#     # username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
#     # username_field.send_keys("Disha")
#     # time.sleep(3)



#     # # Wait for the button to be clickable and then click it
#     # wait = WebDriverWait(driver, 10)
#     # button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='btn my-0 py-0 show']")))
#     # time.sleep(3)
#     # button.click()

#     # # Wait for the dropdown to appear and click the "Download in English" option
#     # download_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Download in English']")))
#     # time.sleep(3)
#     # download_link.click()



#     #  # Find the username field and enter email
#     # time.sleep(3)
#     # username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
#     # username_field.send_keys("Radhika")
#     # time.sleep(3)


#     # # Wait for the dropdown button to be clickable and click it to open the dropdown
#     # dropdown_button = WebDriverWait(driver, 20).until(
#     #     EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='btn' and @data-bs-toggle='dropdown']"))
#     # )
#     # time.sleep(3)
#     # dropdown_button.click()

#     # # Wait for the dropdown menu to be visible
#     # dropdown_menu = WebDriverWait(driver, 20).until(
#     #     EC.visibility_of_element_located((By.XPATH, "//ul[@class='dropdown-menu show']"))
#     # )
#     # # Wait until the "Download With Comment" button is clickable
#     # download_with_comment_button = WebDriverWait(driver, 20).until(
#     #     EC.element_to_be_clickable((By.ID, "btnWithCmmt"))
#     # )
#     # # Click the "Download With Comment" button
#     # time.sleep(4)
#     # download_with_comment_button.click()





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

                                                        # # Partisl CLICK and Download Process
                                                        

                                                        # Wait until the <a> tag is clickable using XPath

#                                                         # Wait for the "Report" link to be clickable
#     wait = WebDriverWait(driver, 10)
#     report_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/report/reports']")))
# #    Scroll the element into view
#     driver.execute_script("arguments[0].scrollIntoView(true);", report_link)
    
#     # Click the "Report" link
#     time.sleep(3)
#     report_link.click()
#     wait = WebDriverWait(driver, 10)
#     link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'nav-link') and text()='Partial']")))

#     # Click the <a> tag
#     time.sleep(3)
#     link.click()

#     username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
#     username_field.send_keys("Sana")
#     time.sleep(3)

    

                                                #   Start click CV process of code


#                                                         #click Technical link and Upcomming  search click :: CV :: Click


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

    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("Sana")
    time.sleep(3)
                                                                                #click CV


   # Wait for the <a> element inside the button to be clickable
    link_xpath = "//button[@class='btn p-1']/a[contains(@class, 'dropdown-item')]"
    
    # Wait for the <a> element to be clickable
    link_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, link_xpath))
    )
    
    # Click the <a> element
    time.sleep(3)
    link_element.click()
    time.sleep(5)
  


    # Use only class and partial href (ignoring dmx-bind:href)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item btn' and contains(@href, 'javascript:void(0)')]"))
    )
    
    # Click the element
    time.sleep(3)
    element.click()


                  #           click Leadership and Upcomming search click  :: CV ::click properly working


     # Increase wait time to handle slower loading elements
    leadership_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/rac_assessment/leadership"]')))
    
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", leadership_link)
    
    # Click the link
    time.sleep(3)
    leadership_link.click()
    
     # Find the username field and enter email
    username_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username_field.send_keys("Nina")
    time.sleep(4)


 # Define the XPath for the <a> element that contains the SVG
    link_xpath = "//a[contains(@class, 'dropdown-item') and contains(@class, 'btn')]"

  
    # Wait for the link element to be clickable
    link_element = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, link_xpath))
    )

    # Click the link element
    time.sleep(3)
    link_element.click()

    # # Use only class and partial href (ignoring dmx-bind:href)
    # element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item btn' and contains(@href, 'javascript:void(0)')]"))
    # )
    
    # # Click the element
    # time.sleep(3)
    # element.click()



    time.sleep(15)  # Wait for 15 seconds to view results
finally:
    # Close the browser
    driver.quit()  # Ensure the browser closes

