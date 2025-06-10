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
                sh '''
                pip install -r requirements.txt
                pytest --disable-warnings
                '''
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
                fuser -k 8090/tcp || true
                docker run -d --name your-app -p 8090:5000 your-app:latest
                '''
            }
        }
    }
}
