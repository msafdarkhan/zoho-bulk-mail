from emails import from_template
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from os import system
import time


chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
driver.set_window_size(1024, 650)
def ifExist(xpath):
        try:
            driver.find_element_by_xpath(xpath)
            return True
        except:
            return False

def sendingmails():
    url = driver.current_url
    if url != "https://mail.zoho.com/zm/#mail/folder/inbox":
        login()
    else:
        for sendmail in sendemails:
            driver.find_element_by_xpath("//span[@data-appname='mail']").click()
            time.sleep(16)
            #to
            driver.find_element_by_xpath("//input[@class='zm_sgst'][1]").send_keys(sendmail)
            #time.sleep(1) cc
            #driver.find_element_by_xpath("//input[@class='zm_sgst'][2]")
            time.sleep(1)
            #Subject
            driver.find_element_by_xpath("//div[@class='zmCmd']/div/div/div[5]/input").send_keys(subject)
            time.sleep(1)
            #Body
            driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[0])
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div").send_keys(body)
            time.sleep(1)
            driver.switch_to.default_content()
            #send
            time.sleep(2)
            driver.find_element_by_xpath("//div[@id='jsMSCenterIcon']/ul/li/b").click()
            time.sleep(6)
            print("send")

def login():
    driver.get("https://accounts.zoho.com/signin")
    time.sleep(12)
    if ifExist("//form[1]"):
        driver.find_element_by_id('login_id').send_keys(email)
        time.sleep(1)
        driver.find_element_by_id('nextbtn').click()
        time.sleep(1)
        driver.find_element_by_id('password').send_keys(password)
        time.sleep(1)
        driver.find_element_by_id('nextbtn').click()
        time.sleep(6)
        driver.get("https://mail.zoho.com/zm/#mail/folder/inbox")
        time.sleep(42)
        sendingmails()
    else:
        print("error")

system("cls")
email = "your Email"
password = "Your Password"
subject="Test Subject"
sendemails=['"Name1" <email1@emai.com>','"Name2" <email2@email.com>']
body="Email Body"
system("cls")
tiktod = pyfiglet.figlet_format("Zoho Mail Sender", font="slant")
print(tiktod)
print("Author: Safdar Khan")
login()