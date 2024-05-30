from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
import time

try:
    # Configure Edge options
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument('--headless')  # Uncomment if you want to run in headless mode
    edge_options.add_argument('--disable-gpu')
    edge_options.add_argument('--no-sandbox')

    # Path to Edge WebDriver
    edge_service = EdgeService(executable_path='C:\\Users\\sss927832\\Downloads\\edgedriver_win64\\msedgedriver.exe')

    # Initialize WebDriver
    driver = webdriver.Edge(service=edge_service, options=edge_options)

    # Open a website
    driver.get('http://https://www.youtube.com/')

    # Perform actions
    print(driver.title)
    driver.quit()

except Exception as e:
    print(f"An error occurred: {e}")