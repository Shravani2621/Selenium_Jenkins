from selenium import webdriver

# Path to the WebDriver executable
driver_path = 'C:\\Users\\sss927832\\Downloads\\edgedriver_win64\\msedgedriver.exe'

# Initialize the WebDriver instance (e.g., Chrome)
driver = webdriver.Chrome(executable_path=driver_path)

# Navigate to a webpage
driver.get('https://www.youtube.com')

# Get and print the page title
print("Page title:", driver.title)

# Close the browser
driver.quit()
