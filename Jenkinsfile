pipeline {
    agent any
 
    environment {
        PYTHON_ENV = 'python3'
    }
 
    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository containing the Flask application
git 'https://github.com/sairachapudi28/CICD.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                // Install the Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                // (Optional) Run any tests if you have them
                echo 'No tests specified.'
            }
        }
        
        stage('Run Application') {
            steps {
                // Run the Flask application
sh 'nohup python app.py &'
            }
        }
    }
    
    post {
        always {
            // Clean up
            echo 'Pipeline finished.'
        }
    }
}
