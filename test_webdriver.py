from selenium import webdriver

# Path to the Microsoft Edge WebDriver executable
edge_driver_path = 'C:\\Users\\sss927832\\Downloads\\edgedriver_win64\\msedgedriver.exe'

edge_options.add_argument('headless')

# Initialize the Edge WebDriver
edge_options = webdriver.EdgeOptions()
# Add any additional options if needed
# e.g., to run Edge in headless mode: edge_options.add_argument('headless')
driver = webdriver.Edge()

# Navigate to a webpage
driver.get('https://www.youtube.com')

# Print the title of the webpage
print("Title of the webpage:", driver.title)

# Close the browser
driver.quit()
