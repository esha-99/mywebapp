pipeline {
    agent any
    environment {
        IMAGE_NAME = "selenium-test"
    }
    stages {
        stage('Code Linting') {
            steps {
                script {
                    // Example: run flake8 for Python linting
                    sh 'pip install flake8'
                    sh 'flake8 .'
                }
            }
        }

        stage('Code Build') {
            steps {
                script {
                    // Example: build Python package or compile code
                    sh 'python setup.py build'
                }
            }
        }

        stage('Unit Testing') {
            steps {
                script {
                    // Run unit tests with pytest
                    sh 'pip install pytest'
                    sh 'pytest tests/unit --maxfail=1 --disable-warnings -q'
                }
            }
        }

        stage('Containerized Deployment') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Selenium Testing') {
            steps {
                script {
                    // Run Selenium tests inside the container
                    sh 'docker run --rm $IMAGE_NAME'
                }
            }
        }
    }
    post {
        always {
            // Cleanup unused Docker resources
            sh 'docker system prune -af'
        }
    }
}
