from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configure Edge options
edge_options = EdgeOptions()
edge_options.use_chromium = True

# Path to Edge WebDriver
edge_service = EdgeService(executable_path='C:\Users\sss927832\Downloads\edgedriver_win64\msedgedriver.exe')

# Initialize WebDriver
driver = webdriver.Edge(service=edge_service, options=edge_options)

