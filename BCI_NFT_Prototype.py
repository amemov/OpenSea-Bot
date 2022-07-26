#coding:utf-8
# Requirement: install following packages -> keyboard, selenium, webdriver_manager, http_request_randomizer
import os, sys, requests, time, keyboard
from selenium import webdriver                                  # Selenium Webdriver API
from webdriver_manager.chrome import ChromeDriverManager        # necessary to operate with Chrome
from selenium.webdriver.chrome.options import Options           # necessary to load existing extensions for bot 
from selenium.webdriver.chrome.service import Service           # necessary to inialize the ChromeDriverManager
from selenium.webdriver.common.by import By                     # necessary to search through html/css content 
from selenium.webdriver import ActionChains                     # necessary to perform mouse clicks
from selenium.webdriver.support.ui import Select                # probably necessary to select stuff on page (like, click 'next')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait         # timing tool for WebDriver
from fake_useragent import UserAgent                            # sets up random agent for ChromeDriver
from selenium.webdriver.common.keys import Keys
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

##################################################################################################################
### -1. Methods for Dealing with Captcha and Related Constants
##################################################################################################################
speechToText = 'https://speech-to-text-demo.ng.bluemix.net/'
delayTime = 2
audioToTextDelay = 10
filename = '1.mp3'
def audioToText(audioDir):
    driver.execute_script('''window.open("","_blank");''')
    driver.switch_to.window(driver.window_handles[1])
    driver.get(speechToText)
    delayTime = 10

    # Upload file
    time.sleep(1)
    print("3")

    # Upload file
    time.sleep(1)
    root = driver.find_element_by_id('root').find_elements_by_class_name('dropzone _container _container_large')
    btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/input')
    btn.send_keys(audioDir)

    # Audio to text is processing
    time.sleep(delayTime)
    print("4")

    # Audio to text is processing
    time.sleep(audioToTextDelay)
    text = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[7]/div/div/div').find_elements_by_tag_name('span')
    result = " ".join( [ each.text for each in text ] )
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return result

def saveFile(content,filename):
    with open(filename, "wb") as handle:
        for data in content.iter_content():
            handle.write(data)

##################################################################################################################
### 0. Load Extension. Initialize ChromeDriver and Open Browser
##################################################################################################################
ua = UserAgent()
userAgent = ua.random
chrome_options =  Options()
chrome_options.add_extension('extension.crx')    
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome(service =Service(ChromeDriverManager().install()), options=chrome_options  )
 

##################################################################################################################
### 1. First Appearance of Extension Window 
# Press to continue setup wallet: <button class="button btn--rounded btn-primary first-time-flow__button" role="button" tabindex="0">������ ������</button>
# Decline:                        <button class="button btn--rounded btn-secondary page-container__footer-button" data-testid="page-container-footer-cancel" role="button" tabindex="0">���, �������</button>
# Import wallet:                  <button class="button btn--rounded btn-primary first-time-flow__button" role="button" tabindex="0">������ ��������</button>
# 'No thanks' window:             <button class="button btn--rounded btn-secondary page-container__footer-button" data-testid="page-container-footer-cancel" role="button" tabindex="0">���, �������</button>
# Manually provide information for the wallet
##################################################################################################################
        # '������ ������'
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
print(driver.current_url)
WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary'))).click()
button = driver.find_element(By.CSS_SELECTOR,'.btn-primary').click()
                   
##################################################################################################################
### 2. Switchback to OpenSea
# MetaMask:                       <li class="sc-197zmwo-0 lcXNuJ"><button class="sc-ty1bh0-0 infdiL sc-1xf18x6-0 sc-1twd32i-0 sc-1idymv7-0 dIseSe kKpYwv fNIWSU" type="button"><div size="24" class="sc-1xf18x6-0 sc-1twd32i-0 sc-1wwz3hp-0 sc-b4hiel-0 sc-cjf6mn-0 sc-sbw25j-0 sc-s8gv83-0 fhVUfN kKpYwv kuGBEl iVtKaT euUQqP jwEsBT bLwasA"><img alt="" height="30px" src="/static/images/logos/metamask-fox.svg" size="24" class="sc-1xf18x6-0 sc-sbw25j-1 eTKUoZ kGXfai"></div><div class="sc-1xf18x6-0 sc-1twd32i-0 sc-1wwz3hp-0 sc-b4hiel-0 sc-1idymv7-1 haVRLx kKpYwv kuGBEl iVtKaT cjftsJ"><span font-weight="700" font-size="14px" class="sc-1xf18x6-0 sc-1w94ul3-0 sc-1idymv7-2 jsdyUC jIOnMl">MetaMask</span></div><div class="sc-1xf18x6-0 sc-1idymv7-3 haVRLx dOqAvv"><span class="sc-1xf18x6-0 sc-1w94ul3-0 sc-1idymv7-6 cwzfDK fBGJrx"><div class="sc-1xf18x6-0 sc-14v1v8i-1 haVRLx jwMqMl">Popular</div></span></div></button></li>
#                                 <button class="sc-ty1bh0-0 infdiL sc-1xf18x6-0 sc-1twd32i-0 sc-1idymv7-0 dIseSe kKpYwv fNIWSU" type="button"><div size="24" class="sc-1xf18x6-0 sc-1twd32i-0 sc-1wwz3hp-0 sc-b4hiel-0 sc-cjf6mn-0 sc-sbw25j-0 sc-s8gv83-0 fhVUfN kKpYwv kuGBEl iVtKaT euUQqP jwEsBT bLwasA"><img alt="" height="30px" src="/static/images/logos/metamask-fox.svg" size="24" class="sc-1xf18x6-0 sc-sbw25j-1 eTKUoZ kGXfai"></div><div class="sc-1xf18x6-0 sc-1twd32i-0 sc-1wwz3hp-0 sc-b4hiel-0 sc-1idymv7-1 haVRLx kKpYwv kuGBEl iVtKaT cjftsJ"><span font-weight="700" font-size="14px" class="sc-1xf18x6-0 sc-1w94ul3-0 sc-1idymv7-2 jsdyUC jIOnMl">MetaMask</span></div><div class="sc-1xf18x6-0 sc-1idymv7-3 haVRLx dOqAvv"><span class="sc-1xf18x6-0 sc-1w94ul3-0 sc-1idymv7-6 cwzfDK fBGJrx"><div class="sc-1xf18x6-0 sc-14v1v8i-1 haVRLx jwMqMl">Popular</div></span></div></button>
# Next (popup):                   <button class="button btn--rounded btn-primary" role="button" tabindex="0">�����</button>
# Sign (popup):                   <button class="button btn--rounded btn-primary btn--large request-signature__footer__sign-button" data-testid="request-signature__sign" role="button" tabindex="0">���������</button>
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
time.sleep(2)
driver.switch_to.window(driver.window_handles[2])
print(driver.current_url) # works
button = driver.find_element(By.CSS_SELECTOR,'.btn-primary').click()
driver.switch_to.window(driver.window_handles[0])

        # Accept and Sign
time.sleep(13)  
print(driver.current_url) # works
WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, "//button[contains( text(), 'Accept and sign')]"))).click() # now works
button = driver.find_element(By.XPATH, "//button[contains( text(), 'Accept and sign')]").click() 
time.sleep(3) 

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

        ## Make Sure Input Transefered Correctly, then Press F8
while True:
    if keyboard.is_pressed("F8"):
        break
print(driver.current_url) 

        # Create 
time.sleep(2)
button = driver.find_element(By.XPATH, "//button[contains( text(), 'Create')]").click() 

        # Captcha 
time.sleep(3)
captchaBody = driver.find_elements_by_class_name('g-recaptcha')[0]
time.sleep(2)
checkbox = captchaBody.find_element_by_tag_name('iframe')
time.sleep(1)
checkbox.click()
print("CLICKED ON CHECKBOX")
time.sleep(2)
allIframesLength = driver.find_elements_by_tag_name('iframe')
time.sleep(1)
audioButtonExists = False
audioButtonIndex = -1

for index in range(len(allIframesLength)):
    driver.switch_to.default_content()
    iframe = driver.find_elements_by_tag_name('iframe')[index]
    driver.switch_to.frame(iframe)
    driver.implicitly_wait(delayTime)
    try:
        audioButton = driver.find_element_by_id('recaptcha-audio-button') or driver.find_element_by_id('recaptcha-anchor')
        audioButton.click()
        audioButtonExists = True
        audioButtonIndex = index
        break
    except Exception as e:
        pass

if audioButtonExists:
    try:
        while True:
            href = driver.find_element_by_id('audio-source').get_attribute('src')
            response = requests.get(href, stream=True)
            saveFile(response,filename)
            response = audioToText(os.getcwd() + '/' + filename)
            print(response)

            driver.switch_to.default_content()
            iframe = driver.find_elements_by_tag_name('iframe')[audioButtonIndex]
            driver.switch_to.frame(iframe)

            inputBox = driver.find_element_by_id('audio-response')
            inputBox.send_keys(response)
            inputBox.send_keys(Keys.ENTER)

            time.sleep(2)
            error = driver.find_elements_by_class_name('rc-audiochallenge-error-message')[0]

            if error.text == "" or error.value_of_css_property('display') == 'none':
                print("Success!")
                break
             
    except Exception as e:
        print(e)
        print('EXCEPTION. Change Proxy!')
else:
    print('ERROR. Button not found.') 

##################################################################################################################
#####                                                END                                                     #####
##################################################################################################################
while True: 
    if keyboard.is_pressed("F8"):
        driver.quit()
        break 