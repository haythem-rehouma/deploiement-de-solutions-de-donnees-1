pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // IMPORTANT : remplacez l'URL par celle de VOTRE depot GitHub
                git branch: 'main', url: 'https://github.com/VOTRE-COMPTE/calculator.git'
            }
        }
        stage('Build & Test') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'mvn -B clean package'
                    } else {
                        bat 'mvn -B clean package'
                    }
                }
            }
        }
    }
    post {
        always {
            // Publie le rapport des tests unitaires (visible dans "Test Result")
            junit '**/target/surefire-reports/*.xml'
            // Archive le JAR genere (telechargeable depuis la page du build)
            archiveArtifacts artifacts: 'target/*.jar', fingerprint: true, allowEmptyArchive: true
        }
    }
}
