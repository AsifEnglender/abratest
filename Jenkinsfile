pipeline {
    agent any



    stages {
        // Run this stage only if the branch is not 'main'
        stage('code format') {
            when {
                not {
                    
                    branch 'main'
                }
            }
            steps { 
                script {
                    sh '''
                    echo 'not on main, running  black'
                    
                    black --diff app.py
                    '''
                }
            }
}
        // Run this stage only if the branch is not 'main'
       stage('lint') {
            when {
                not {
                    
                    branch 'main'
                }
            }
            steps { 
                script {

                    sh '''
                    echo 'not on main, running pylint'
                    python3 -m pylint app.py  || true
                    '''
                }
            }
}

             stage('sonarqube') {
        
            steps { 
                script {

                    sh '''
                    /sonar-scanner-5.0.1.3006-linux/bin/sonar-scanner  \
                    -Dsonar.projectKey=test \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://192.168.0.3:9000 \
                    -Dsonar.token=sqp_e13baa7c81ebd1be56dc962367e28ab600e0a5c3
                    '''
                }
            }
}




        //always run this stage 
        stage('Build  and run container container ') {
            steps {
                script {
                    // Build the Docker image
                    sh '''
                    docker build -t localhost:6000/asif-flask .
                    
                    
                    '''
                }
            }
        }

        //always run this stage         
        stage('unit test ') {
            steps {
                script {
                    // unit test
                    
                    sh '''    
                    pytest test_app.py
                    '''
                    
                }
            }
        }


            // curl should return "abra", run this stage not on 'main'
            stage('black box- curl test') {
            when {
                not {
                    
                    branch 'main'
                }
            }
            steps { 
                script {
                 containerId = sh(script: 'docker run --ip 192.168.0.20 --network testnet  -d  localhost:6000/asif-flask', returnStdout: true).trim()
                sleep(10)
                def response = sh(script: 'curl -s 192.168.0.20:7000', returnStdout: true).trim()
               
                if (response == 'abra') {
                    sh '''
                    echo 'test worked'
                    
                    '''
                } else {
                    sh '''
                    echo 'test failed'
                    '''
                }
                
                // kill container
                sh """
                docker kill ${containerId}
                docker rm  ${containerId}
                """

                }
                
            }
}


           // push , only on main
            stage('push test') {
            when {
                branch 'main'
            }
            steps { 
                sh '''
                docker push localhost:6000/asif-flask

                '''

            }
}

    }
}
