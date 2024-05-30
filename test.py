from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Path to the Microsoft Edge WebDriver executable
edge_driver_path = 'C:\\ProgramData\\Jenkins\\.jenkins\\tools\\edgedriver\\msedgedriver.exe'

# Initialize the Edge Service
edge_service = Service(edge_driver_path)

# Start the Edge Service
edge_service.start()

# Initialize the Edge WebDriver with Edge Service
driver = webdriver.Edge(service=edge_service)

# Navigate to a webpage
driver.get('https://www.youtube.com')

# Print the title of the webpage
print("Title of the webpage:", driver.title)

# Close the browser
driver.quit()

# Stop the Edge Service
edge_service.stop()
