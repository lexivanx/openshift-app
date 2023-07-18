pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'docker build -t flask-app .'
            }
        }
        stage('Test') {
            steps {
                sh 'python test_app.py'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                oc login --token=<token> --server=<server>
                oc project flask-app
                oc start-build flask-app --from-dir . --follow
                '''
            }
        }
    }
}
