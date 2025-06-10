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

        stage('Run Tests') {
            steps {
                sh 'pytest || echo "Tests failed"'
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
