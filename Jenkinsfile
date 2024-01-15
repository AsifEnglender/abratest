pipeline {
    agent any

    environment {
        // Define your Docker image tag, registry, and credentials if needed
        IMAGE_TAG = 'your-image-tag'
        DOCKER_REGISTRY = 'your-docker-registry'
        REGISTRY_CREDENTIALS_ID = 'your-registry-credentials-id' // ID for Jenkins credentials
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh "docker build -t ${DOCKER_REGISTRY}/${IMAGE_TAG} ."
                }
            }
        }

        stage('Push Docker Image
