pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh '''
                    docker kill  samplerun || true
                    docker rm samplerun || true
                    sudo docker build -t localhost:6000/asif-flask .
                    sudo docker run --name samplerun -d -p  5000:5000  localhost:6000/asif-flask
                    

                    '''
                    sleep(10)

                    // Check if we're on the main branch
                    if (env.BRANCH_NAME == 'main') {
                        sh ''' 
                        echo " on main branch, hence pushing container
                        sudo docker push localhost:6000/asif-flask
                        '''
                    } else {
                        // For branches other than main, perform a curl request
                        def response = sh(script: 'curl -s 172.17.0.1:5000', returnStdout: true).trim()
                        if (response == 'abra') {
                            sh '''
                            echo 'test worked'
                            sudo docker kill samplerun
                            sudo docker rm samplerun
                            '''
                        } else {
                            sh '''
                            echo 'test failed'
                            sudo docker kill samplerun
                            sudo docker rm samplerun
                            '''
                        }
                    }
                }
            }
        }
    }
}
