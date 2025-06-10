pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Nazarmalskij/term-project.git'
            }
        }

        stage('Build Backend') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t your-app:latest .'
            }
        }
        stage('Build') {
            steps {
                sh 'echo "No build required for this type of project"'
            }
}

        stage('Deploy') {
            steps {
                 // Зупинка попереднього контейнера, якщо він існує, і запуск нового
                sh '''
                docker stop your-app || true
                docker rm your-app || true
                docker run -d --name your-app -p 8080:8080 your-app:latest
                '''
            }
        }
    }
} 
  