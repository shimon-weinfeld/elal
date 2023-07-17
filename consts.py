from selenium.webdriver.common.by import By

# login data
ORDER_NUMBER = "JS8TU8"
LAST_NAME = "weinfeld"

# URL
LOGIN_URL = "https://booking.elal.com/manage/login?lang=he"

# color
COLOR_SEAT = 'color-elal-space'
COLOR_SEAT = 'color-economy'

# locators
ORDER_NUMBER_LOCATOR = (By.XPATH, "//input[contains(@placeholder,'מספר הזמנה')]")
LAST_NAME_LOCATOR = (By.XPATH, "//input[contains(@placeholder,'שם משפחה')]")
LOGIN_FORM = (By.TAG_NAME, "form")
CLOSE_POPUP_LOCATOR = (By.ID, "close-upgrade-seat")
CHANGE_CHOICE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "#anc-seat-container button")
DESIRED_FLIGHT_LOCATOR = (By.XPATH, "//div[contains(@class,'anc-segment__container flex-wrap') "
                                  "and .//div[contains(@class,'anc-segment__location')][1]//p[2][text()='JFK']]")
ROWS_WITH_AVAILABLE_SEATS_LOCATOR = (By.XPATH, f"//div[contains(@class,'seatmap__plan__row') and .//div[contains(@class,'{COLOR_SEAT}')]]")
SEAT_XPATH = ".//div[contains(@class,'seatmap__plan__cell') and not(contains(@class,'align'))]"