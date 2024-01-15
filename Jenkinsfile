pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh '''
                    sudo docker build -t localhost:6000/asif-flask .
                    sudo docker run --name samplerun -d -p  5000:5000  localhost:6000/asif-flask
                    sudo docker kill samplerun
                    '''

                    // Check if we're on the main branch
                    if (env.BRANCH_NAME == 'main') {
                        sh 'sudo docker push localhost:6000/asif-flask'
                    } else {
                        // For branches other than main, perform a curl request
                        def response = sh(script: 'curl -s localhost:5000', returnStdout: true).trim()
                        if (response == 'abra') {
                            echo 'ok'
                        } else {
                            echo 'test failed'
                        }
                    }
                }
            }
        }
    }
}
