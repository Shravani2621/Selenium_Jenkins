pipeline {
    agent any
    
    environment {
        // Define the path to your Edge WebDriver executable
        EDGE_DRIVER_PATH = 'C:\\Users\\sss927832\\Downloads\\edgedriver_win64\\msedgedriver.exe'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from GitHub
                git 'https://github.com/Shravani2621/Selenium_Jenkins.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                bat 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run Selenium tests in Edge browser
                bat 'python -m pytest --driver=edge --driver-path="${EDGE_DRIVER_PATH}" tests/'
            }
        }
    }
}
