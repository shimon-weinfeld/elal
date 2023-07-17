import time
import consts
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")

while True:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    wait = WebDriverWait(driver, 120)
    driver.maximize_window()

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

    driver.get(consts.LOGIN_URL)

    # login page
    wait.until(EC.visibility_of_element_located(consts.ORDER_NUMBER_LOCATOR)).send_keys(consts.ORDER_NUMBER)
    wait.until(EC.visibility_of_element_located(consts.LAST_NAME_LOCATOR)).send_keys(consts.LAST_NAME)
    wait.until(EC.presence_of_element_located(consts.LOGIN_FORM)).submit()

    # order page
    wait.until(EC.element_to_be_clickable(consts.CLOSE_POPUP_LOCATOR)).click()
    wait.until(EC.element_to_be_clickable(consts.CHANGE_CHOICE_BUTTON_LOCATOR)).click()

    # seats component
    wait.until(EC.element_to_be_clickable(consts.DESIRED_FLIGHT_LOCATOR)).click()
    time.sleep(3)
    rows_with_available_seats = wait.until(EC.presence_of_all_elements_located(consts.ROWS_WITH_AVAILABLE_SEATS_LOCATOR))
    print(f"נמצאו {len(rows_with_available_seats)} שורות עם מושבים פנויים")

    there_is_a_seat = False
    for row in rows_with_available_seats:
        all_seats = row.find_elements(By.XPATH, consts.SEAT_XPATH)

        for seat in all_seats:
            if consts.COLOR_SEAT in seat.get_attribute("innerHTML"):
                if there_is_a_seat:
                    print("נמצאו זוג מושבים סמוכים פנויים!!!!!")
                else:
                    print("נמצא מושב בודד פנוי")
                    there_is_a_seat = True
            elif there_is_a_seat:
                there_is_a_seat = False

    driver.close()
    driver.quit()

    time.sleep(3600)