pipeline {
    agent any
    parameters {
        string defaultValue: '60', name: 'INTERVAL'
    }
    environment {
        NAME = "ishays"
        VERSION = "${env.BUILD_ID}"
        IMAGE = "${NAME}:${VERSION}"
        //CRED = credentials('credentials')
        //CONFIG = credentials('config')
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
                // withCredentials([file(credentialsId: 'AWSconfig', variable: 'AWS_CONFIG_PATH'), file(credentialsId: 'AWScreds', variable: 'AWS_CREDS_PATH')]) {
                    // sh "cp $AWS_CONFIG_PATH config"
                    // sh "cp $AWS_CREDS_PATH credentials"
                    // sh "docker build -t ${IMAGE} ."
                    // sh "rm -f credentials config"
                    sh "echo 'This is the build step running'"
                }
            }
        }
        stage('Deploy') {
            steps {
                // sh "docker run -itd --name ${NAME} --env INTERVAL=${params.INTERVAL} ${IMAGE}"
                sh "echo 'This is the deploy step, might replace it later to push stage?'"
            }
        }
        stage('Increment tag in Helm') {
            when {
                succuess {}
            }
            steps {
                sh "echo 'If previous step was successful, use yq to change the tag the helm chart'"
            }
        }
        stage('Commit changes and merge to master') {
            when {
                succuess {}
            }
            steps {
                sh "echo 'here we will commit the updated helm to the dev repo and merge all changes into mater"
            }
        }
    }
}
