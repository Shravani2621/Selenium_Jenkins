from selenium import webdriver

# Path to the Microsoft Edge WebDriver executable
edge_driver_path = 'C:\\ProgramData\\Jenkins\\.jenkins\\tools\\edgedriver\\msedgedriver.exe'

# Initialize the EdgeOptions
edge_options = webdriver.EdgeOptions()
edge_options.add_argument('headless')

# Specify the path to the WebDriver executable
edge_options.binary_location = edge_driver_path

# Initialize the Edge WebDriver with EdgeOptions
driver = webdriver.Edge(options=edge_options)

# Navigate to a webpage
driver.get('https://www.youtube.com')

# Print the title of the webpage
print("Title of the webpage:", driver.title)

# Close the browser
driver.quit()

