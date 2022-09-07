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


