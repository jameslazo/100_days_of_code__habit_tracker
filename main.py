from api_requests import APIRequests
from datetime import datetime
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service

api = APIRequests()
today = datetime.now()

api.send_telegram_message(api.post_pixel(date=today.strftime("%Y%m%d"), hours="4"))
# api.send_telegram_message(api.post_pixel(date="20230522", hours="9"))

# # Set up Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode
# chrome_options.add_argument("--start-maximized")  # Maximize the browser window
#
# # Set the path to the Chrome driver executable
# # Download the Chrome driver from: https://sites.google.com/a/chromium.org/chromedriver/downloads
# chrome_driver_path = "/path/to/chromedriver"
#
# service = Service(chrome_driver_path)
#
# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome(service=service, options=chrome_options)
#
# # Navigate to the webpage
# driver.get("https://www.example.com")
#
# # Take a screenshot of the webpage
# screenshot_path = f'/graphs/{today.strftime("%Y%m%d")}.png'
# driver.save_screenshot(screenshot_path)
#
# # Close the browser
# driver.quit()
#
# with open("graphs/2023")
# api.send_telegram_message(screenshot_path)


