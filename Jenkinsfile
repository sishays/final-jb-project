pipeline {
    agent any
    parameters {
        string defaultValue: '60', name: 'INTERVAL'
    }
    environment {
        NAME = "ishays"
        VERSION = "${env.BUILD_ID}"
        IMAGE = "${NAME}:${VERSION}"
        CRED = credentials('credentials')
        CONFIG = credentials('config')
    }

    stages {
        stage('Init') {
            steps {
                cleanWs()
                sh "docker kill ${NAME} || true"
                sh "docker rm ${NAME} || true"
                sh "docker rmi -f ${NAME}|| true"
            }
        }
        stage('SCM') {
            steps {
                git url: 'https://github.com/sishays/cicd-ec2-checker.git', branch: 'development'
            }
        }
        stage('Build') {
            steps {
                withCredentials([file(credentialsId: 'AWSconfig', variable: 'AWS_CONFIG_PATH'), file(credentialsId: 'AWScreds', variable: 'AWS_CREDS_PATH')]) {
                    sh "cp $AWS_CONFIG_PATH config"
                    sh "cp $AWS_CREDS_PATH credentials"
                    sh "docker build -t ${IMAGE} ."
                    sh "rm -f credentials config"
                }
            }
        }
        stage('Deploy') {
            steps {
                sh "docker run -itd --name ${NAME} --env INTERVAL=${params.INTERVAL} ${IMAGE}"
            }
        }
    }
}
