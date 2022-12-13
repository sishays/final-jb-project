// properties([pipelineTriggers([githubPush(branch: 'development')])])
pipeline {
    agent any
    parameters {
        string defaultValue: '60', name: 'INTERVAL'
    }
    environment {
        NAME = "ishays"
        VERSION = "${env.BUILD_ID}"
        IMAGE = "${NAME}:${VERSION}"
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
                git url: 'git@github.com:sishays/final-jb-project.git', branch: 'development', credentialsId: 'jenkins-ssh'
            }
        }
        stage('Build') {
            steps {
                // withCredentials([file(credentialsId: 'AWSconfig', variable: 'AWS_CONFIG_FILE'), file(credentialsId: 'AWScreds', variable: 'AWS_CREDS_FILE')]) {
                    // sh "cp $AWS_CONFIG_FILE config"
                    // sh "cp $AWS_CREDS_FILE credentials"
                    // sh "docker build -t ${IMAGE} ."
                    // sh "rm -f credentials config"
                    sh "echo 'This is the build step running'"
                // }
            }
        }
        stage('Upload image to Docker Hub') {
            steps {
                // sh "docker run -itd --name ${NAME} --env INTERVAL=${params.INTERVAL} ${IMAGE}"
                withCredentials([usernamePassword(credentialsId: 'docker_login_creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh "echo 'This is the deploy step, might replace it later to push stage?'"
                    sh "echo ${DOCKER_USERNAME} and ${DOCKER_PASSWORD}"
                    // sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                    // sh "docker push ${IMAGE}"
                }
            }
        }
        stage('Increment tag in Helm') {
            steps {
                sh "echo 'If previous step was successful, use yq to change the tag the helm chart'"
                sh "yq eval -i '.env.INTERVAL = ${params.INTERVAL}' final-jb-project/values.yaml"
                sh "yq eval -i '.image.tag = ${VERSION}' final-jb-project/values.yaml"
            }
        }
        stage('Commit changes and merge to master') {
            steps {
                sshagent (credentials: ['jenkins-ssh']) {
                // withCredentials([usernamePassword(credentialsId: 'github_api_token', usernameVariable: 'DISCARD', passwordVariable: 'GITLAB_API_TOKEN')]) {
                    sh "echo 'here we will commit the updated helm to the dev repo and merge all changes into master'"
                    sh 'git add .'
                    sh 'git commit -m "Build ${VERSION} commit"'
                    // sh 'git remote set-url origin https://final-jb-project:${git-token}@github.com/sishays/final-jb-project.git'
                    // sh 'git remote add origin https://${GITLAB_API_TOKEN}@github.com/sishays/final-jb-project.git'
                    sh 'git push -u development'
                    sh 'git checkout master'
                    sh 'git merge dev'
                    sh 'git push origin master'
                }
            }
        }
    }
}
