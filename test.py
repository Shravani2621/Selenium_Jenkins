from selenium import webdriver

# Path to the Microsoft Edge WebDriver executable
edge_driver_path = 'C:\\ProgramData\\Jenkins\\.jenkins\\tools\\edgedriver\\msedgedriver.exe'

# Initialize the EdgeOptions
edge_options = webdriver.EdgeOptions()

# Specify the path to the WebDriver executable
edge_options.binary_location = edge_driver_path

# Set the WebDriver executable path in EdgeOptions
edge_options.use_chromium = True  # Set to True if using the Chromium version of Edge

# Initialize the Edge WebDriver with EdgeOptions
driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)

# Navigate to a webpage
driver.get('https://www.youtube.com')

# Print the title of the webpage
print("Title of the webpage:", driver.title)

# Close the browser
driver.quit()
