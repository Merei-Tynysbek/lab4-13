pipeline {
    agent any

    environment {
        IMAGE = 'lab4-13'
    }

    stages {
        stage('Secret scen') {
            steps {
                sh 'trivy fs --scanners secret --skip-dirs .git --exit-code 1 .'
            }
        }

        stage('Build image') {
           steps {
               sh 'docker build -t $IMAGE:%BUILD_NUMBER .'
           }
        }
        stage('OS report') {
            steps {
                sh 'trivy image --pkg-types os --severity CRITICAL --ignore-unfixed $IMAGE:$BUILD_NUMBER'
            }
        }
   }
