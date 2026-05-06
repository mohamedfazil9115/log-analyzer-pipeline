pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/mohamedfazil9115/log-analyzer-pipeline.git'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 analyzer.py'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.txt', fingerprint: true
            }
        }
    }

    triggers {
        pollSCM('* * * * *')
    }
}