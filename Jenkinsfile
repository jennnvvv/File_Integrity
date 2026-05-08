pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/jennnvvv/File_Integrity.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t integrity-checker .'
            }
        }

        stage('Initialize Database') {
            steps {
                bat 'docker run --rm -v "%WORKSPACE%:/app" integrity-checker python main.py init test_folder'
            }
        }

        stage('Run Integrity Check') {
            steps {
                bat 'docker run --rm -v "%WORKSPACE%:/app" integrity-checker python main.py check test_folder'
            }
        }
    }
}