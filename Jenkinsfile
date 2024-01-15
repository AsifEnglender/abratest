pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh '''
                    sudo docker build -t localhost:6000/asif-flask .
                    sudo docker run -d -p  5000:5000  localhost:6000/asif-flask
                    sudo docker push localhost:6000/asif-flask


                    '''
                }
            }
        }
    }
}
