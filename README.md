# cicd-ec2-checker
Scans for running ec2 instances with a specific tag for budget reasons.


This is python script to scan your AWS EC2 instances and display the running K8S master instances.
Use a multi-branch pipeline and scan this repo (https://github.com/sishays/cicd-ec2-checker.git) on development branch.
It will create a Jenkins pipeline job with an interval parameter for how many times to rescan your instances (default is 60s).
You can pass an empty parameter to run the scan once.

<b>Please take notice of the below plugin and Jenkins credentials dependencies:</b>


## Dependencies:</br>
Make sure you have the following jenkins plugins installed:</br>
Workspace Cleanup</br>
Credentials</br>
Credentials Binding</br>
SSH agent</br>


In Jenkins credentials, under global credentials config the following secret files:</br>
**Credential ID:** AWSconfig</br>
Upload a text file containing:</br>
```
[default]
region=<your aws region>
```

**Credential ID:** AWScreds</br>
Upload a text file containing:</br>
```
[default]
aws_access_key_id=<your AWS access key id>
aws_secret_access_key=<your AWS secret access key>
```

## Instructions :</br>
In Jenkins credentials, as the above, also configure your kubeconfig credentials for connecting to your k8s cluster, your ssh creds for accessing your github repository. Don't forget to install ArgoCD in your cluster beforehand. You may choose to deploy using helm (https://argo-cd.readthedocs.io/en/stable/operator-manual/installation/#helm) or any other preferred method.</br>

In your repository define a dev branch along the master branch, and define a webhook in your repository, so that for every sucessfull commit in your dev branch it auto merges to master. 

Create a private docker hub image repository for the succesfull builds and add these credentials (user+pass) as well to Jenkins credentials, in order for the build job to be able to use docker login and docker push to your private docker hub repo. 

In Jenkins, configure a new pipepline project that uses the git repo as the pipeline script. It will detect the jenkinsfile and configure the jenkins script.

