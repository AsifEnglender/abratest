pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh '''
                    docker build -t localhost:6000/asif-flask .
                    docker run -d -p  5000:5000  localhost:6000/asif-flask
                    docker push localhost:6000/asif-flask


                    '''
                }
            }
        }
