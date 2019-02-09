node {
    stage('Build') {
        checkout scm
        sh "docker build . -t aaronmwilliams/python-api-testing"
    }
    stage('Test') {
        sh "docker-compose up --exit-code-from tests"
    }
}