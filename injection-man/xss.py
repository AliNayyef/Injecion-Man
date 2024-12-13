from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from importlib.resources import files
def xss(target_url, input_id, button_value):
    xss_file = files('injection_man').joinpath('xss.txt')
    with open(xss_file, "r", encoding="utf-8" ) as file:
        xss_payloads = file.readlines()

    driver = webdriver.Chrome()
    driver.get(target_url)
    #https://jis.tu.edu.iq/index.php/jis/search?query=
    #https://xss-game.appspot.com/level1
    #https://www.yougetsignal.com/tools/whois-lookup/
    time.sleep(2)

    #iframe = driver.find_element(By.TAG_NAME, "iframe") # this if we have i frame
    #driver.switch_to.frame(iframe)

    for payload in xss_payloads:
        inputs = driver.find_elements(By.ID, input_id)
        print(f"Found {len(inputs)} input fields.")  # enumeration buttons field

        buttons = driver.find_elements(By.XPATH, f"//input[@value='{button_value}']")
        print(f"Found {len(buttons)} button fields.")  # enumeration inputs field


        print(f"Testing payload: {payload}")
        for input in inputs:
            try:
                input.clear()
                input.send_keys(payload)
            except Exception as e:
                print(f"Error inputting payload in field: {e}")
        try:
            for button in buttons:
                button.click()
                time.sleep(1)
        except Exception as e:
            print(f"Error submitting form: {e}")

        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            print(f"Alert triggered with payload: '{payload}', alert text: {alert_text}")
            alert.accept()
            break

        except:
            print("no alert found")
    time.sleep(20)
