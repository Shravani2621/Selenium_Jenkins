pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                git 'https://github.com/Shravani2621/Selenium_Jenkins.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install required dependencies
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run Selenium tests in Edge browser
                script {
                    // Set the PATH to Edge WebDriver
                    def edgeDriverPath = 'C:\\Users\\sss927832\\Downloads\\edgedriver_win64\\msedgedriver.exe'
                    env.PATH = "${env.PATH}:${edgeDriverPath}"
                    
                    // Run the tests
                    sh 'python -m pytest tests --browser edge'
                }
            }
        }
    }
}

