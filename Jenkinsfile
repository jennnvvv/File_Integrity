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


        stage('Run Integrity Check') {
            steps {
                bat 'docker run -v %cd%:/app integrity-checker python main.py check test_folder'
            }
        }
    }
}