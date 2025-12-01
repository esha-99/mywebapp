pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    sudo apt update
                    
                    # Install Python
                    sudo apt install -y python3 python3-pip python3-venv
                    
                    # Install Chrome
                    sudo apt install -y wget gnupg2
                    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
                    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list
                    sudo apt update
                    sudo apt install -y google-chrome-stable
                    
                    # Install pip modules
                    pip3 install --user selenium webdriver-manager flask
                '''
            }
        }

        stage('Start Flask App') {
            steps {
                sh '''
                    # Start Flask in background
                    nohup python3 app.py > flask.log 2>&1 &
                    sleep 3
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh '''
                    python3 test.py
                '''
            }
        }
    }
}
