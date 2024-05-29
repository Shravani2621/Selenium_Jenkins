pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Shravani2621/Selenium_Jenkins.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python -m unittest discover'
            }
        }
    }
}
