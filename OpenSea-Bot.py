#coding:utf-8
# Requirement: install keyboard, selenium, webdriver_manager
import time, keyboard
from selenium import webdriver                                  # Selenium Webdriver API
from webdriver_manager.chrome import ChromeDriverManager        # necessary to operate with Chrome
from selenium.webdriver.chrome.options import Options           # necessary to load existing extensions for bot 
from selenium.webdriver.chrome.service import Service           # necessary to inialize the ChromeDriverManager
from selenium.webdriver.common.by import By                     # necessary to search through html/css content 
from selenium.webdriver import ActionChains                     # necessary to perform mouse clicks
from selenium.webdriver.support.ui import Select                # probably necessary to select stuff on page (like, click 'next')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait         # timing tool for WebDriver

##################################################################################################################
### 0. Load Extension. Initialize ChromeDriver and Open Browser
##################################################################################################################
chrome_options =  Options()
chrome_options.add_extension('extension.crx')    
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service =Service(ChromeDriverManager().install()), options=chrome_options  )
 

##################################################################################################################
### 1. First Appearance of Extension Window 
# Press to continue setup wallet: <button class="button btn--rounded btn-primary first-time-flow__button" role="button" tabindex="0">Начало работы</button>
# Decline:                        <button class="button btn--rounded btn-secondary page-container__footer-button" data-testid="page-container-footer-cancel" role="button" tabindex="0">Нет, спасибо</button>
# Import wallet:                  <button class="button btn--rounded btn-primary first-time-flow__button" role="button" tabindex="0">Импорт кошелька</button>
# 'No thanks' window:             <button class="button btn--rounded btn-secondary page-container__footer-button" data-testid="page-container-footer-cancel" role="button" tabindex="0">Нет, спасибо</button>
# Manually provide information for the wallet
##################################################################################################################
        # 'Начало Работы'
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)
WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary'))).click()
button = driver.find_element(By.CSS_SELECTOR,'.btn-primary').click()
                   
##################################################################################################################
### 2. Switchback to OpenSea
# MetaMask:                       <li class="sc-197zmwo-0 lcXNuJ"><button class="sc-ty1bh0-0 infdiL sc-1xf18x6-0 sc-1twd32i-0 sc-1idymv7-0 dIseSe kKpYwv fNIWSU" type="button"><div size="24" class="sc-1xf18x6-0 sc-1twd32i-0 sc-1wwz3hp-0 sc-b4hiel-0 sc-cjf6mn-0 sc-sbw25j-0 sc-s8gv83-0 fhVUfN kKpYwv kuGBEl iVtKaT euUQqP jwEsBT bLwasA"><img alt="" height="30px" src="/static/images/logos/metamask-fox.svg" size="24" class="sc-1xf18x6-0 sc-sbw25j-1 eTKUoZ kGXfai"></div><div class="sc-1xf18x6-0 sc-1twd32i-0 sc-1wwz3hp-0 sc-b4hiel-0 sc-1idymv7-1 haVRLx kKpYwv kuGBEl iVtKaT cjftsJ"><span font-weight="700" font-size="14px" class="sc-1xf18x6-0 sc-1w94ul3-0 sc-1idymv7-2 jsdyUC jIOnMl">MetaMask</span></div><div class="sc-1xf18x6-0 sc-1idymv7-3 haVRLx dOqAvv"><span class="sc-1xf18x6-0 sc-1w94ul3-0 sc-1idymv7-6 cwzfDK fBGJrx"><div class="sc-1xf18x6-0 sc-14v1v8i-1 haVRLx jwMqMl">Popular</div></span></div></button></li>
# <button class="sc-ty1bh0-0 infdiL sc-1xf18x6-0 sc-1twd32i-0 sc-1idymv7-0 dIseSe kKpYwv fNIWSU" type="button"><div size="24" class="sc-1xf18x6-0 sc-1twd32i-0 sc-1wwz3hp-0 sc-b4hiel-0 sc-cjf6mn-0 sc-sbw25j-0 sc-s8gv83-0 fhVUfN kKpYwv kuGBEl iVtKaT euUQqP jwEsBT bLwasA"><img alt="" height="30px" src="/static/images/logos/metamask-fox.svg" size="24" class="sc-1xf18x6-0 sc-sbw25j-1 eTKUoZ kGXfai"></div><div class="sc-1xf18x6-0 sc-1twd32i-0 sc-1wwz3hp-0 sc-b4hiel-0 sc-1idymv7-1 haVRLx kKpYwv kuGBEl iVtKaT cjftsJ"><span font-weight="700" font-size="14px" class="sc-1xf18x6-0 sc-1w94ul3-0 sc-1idymv7-2 jsdyUC jIOnMl">MetaMask</span></div><div class="sc-1xf18x6-0 sc-1idymv7-3 haVRLx dOqAvv"><span class="sc-1xf18x6-0 sc-1w94ul3-0 sc-1idymv7-6 cwzfDK fBGJrx"><div class="sc-1xf18x6-0 sc-14v1v8i-1 haVRLx jwMqMl">Popular</div></span></div></button>
# Next (popup):                   <button class="button btn--rounded btn-primary" role="button" tabindex="0">Далее</button>
# Sign (popup):                   <button class="button btn--rounded btn-primary btn--large request-signature__footer__sign-button" data-testid="request-signature__sign" role="button" tabindex="0">Подписать</button>
# Accept and Sign:                <button width="100%" type="button" class="sc-1xf18x6-0 sc-glfma3-0 jPlHEK bVTTPO">Accept and sign</button>
##################################################################################################################
time.sleep(2)
while True: 
    if keyboard.is_pressed("F8"):
        driver.get('http://opensea.io/asset/create')
        #driver.switch_to.window(driver.window_handles[1]) # Switches to the Extension page when set to [0]  [1] to OpenSea. 
        # UPD: After adding feature for automating extension [0] is OpenSea
        print(driver.current_url)
        break
        # MetaMask 
WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'MetaMask')]"))).click()
button = driver.find_element(By.XPATH,"//span[contains(text(), 'MetaMask')]").click() 
 
        ## Check if can switch to extension page popup - Success ##
time.sleep(2)
driver.switch_to.window(driver.window_handles[2]) # Switches to the Extension page when set to [0]  [1] to OpenSea
print(driver.current_url)
        # Next(popup)
WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button.btn--rounded.btn-primary'))).click()
button = driver.find_element(By.CSS_SELECTOR,'.button.btn--rounded.btn-primary').click() 
 
        # Sign(popup) and go back to OpenSea
time.sleep(4)
driver.switch_to.window(driver.window_handles[2])
print(driver.current_url) # works
button = driver.find_element(By.CSS_SELECTOR,'.btn-primary').click()
driver.switch_to.window(driver.window_handles[0])
        # Accept and Sign
print(driver.current_url) # works
WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sc-1xf18x6-0.sc-glfma3-0.jPlHEK.bVTTPO'))).click()
button = driver.find_element(By.CSS_SELECTOR, '.sc-1xf18x6-0.sc-glfma3-0.jPlHEK.bVTTPO').click() 
time.sleep(5) 

##################################################################################################################
### 3. Entries to fill to submit NFT
# Image:                          <input id="media" name="media" type="file" tabindex="-1" style="display: none;">
# Name:                           <input type="text" autocapitalize="off" autocomplete="off" autocorrect="off" class="browser-default Input--input" data-testid="Input" id="name" name="name" placeholder="Item name" required="" spellcheck="false" value="">
# Description:                    <textarea id="description" name="description" placeholder="Provide a detailed description of your item." rows="4" class="sc-ehtjq3-0 boxrpc"></textarea>
#                                  text should appear before </textarea>
# Create:                         <button type="button" class="sc-1xf18x6-0 sc-glfma3-0 hiIVBZ bVTTPO">Create</button>
# Captcha:                        <span class="recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox" role="checkbox" aria-checked="false" id="recaptcha-anchor" tabindex="0" dir="ltr" aria-labelledby="recaptcha-anchor-label"><div class="recaptcha-checkbox-border" role="presentation"></div><div class="recaptcha-checkbox-borderAnimation" role="presentation"></div><div class="recaptcha-checkbox-spinner" role="presentation"><div class="recaptcha-checkbox-spinner-overlay"></div></div><div class="recaptcha-checkbox-checkmark" role="presentation"></div></span>
##################################################################################################################
        # Name
name = driver.find_element(By.XPATH,'//input[@type="text"][@placeholder="Item name"]') 
name.send_keys("Abstract Brain Painting")                                                           
        # Description
time.sleep(4)
description = driver.find_element(By.ID, 'description')
description.send_keys("This is an abstract brain painting which depicts someones brain activity.")  
        # Image 
time.sleep(2)
image = driver.find_element(By.XPATH,'//input[@id="media"][@name="media"][@type="file"]')
image.send_keys("C:\\sample.jpg")
while True:
    if keyboard.is_pressed("F8"):
        break
print(driver.current_url) 
        # Create 
time.sleep(2)
button = driver.find_element(By.XPATH, "//button[@class='sc-1xf18x6-0 sc-glfma3-0 hiIVBZ bVTTPO']").click() 
        # Captcha - Doesn't work
#time.sleep(3)
#button = driver.find_element(By.CLASS_NAME,"recaptcha-checkbox-border").click()
 
##################################################################################################################
#####                                                END                                                     #####
##################################################################################################################
while True: 
    if keyboard.is_pressed("F8"):
        driver.quit()
        break 