pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                // No need to clone again if using SCM configuration at the beginning
                echo 'Cloning the repository...'
            }
        }
        stage('Install dependencies') {
            steps {
                // Use 'bat' for Windows command
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                // Use 'bat' for Windows command
                bat 'python -m unittest discover'
            }
        }
    }
}
