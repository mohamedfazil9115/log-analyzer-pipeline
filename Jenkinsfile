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
                sh 'C:\Users\FAZIL\AppData\Local\Python\pythoncore-3.14-64\python.exe'
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