pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Nazarmalskij/term-project.git'
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t your-app:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                docker stop your-app || true
                docker rm your-app || true
                docker run -d --name your-app -p 8080:8080 your-app:latest
                '''
            }
        }
    }
}