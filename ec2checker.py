import boto3

print("Hello world")
print(boto3.__version__)

ec2 = boto3.resource('ec2')
#instance = ec2.Instance('id')

instance_iterator = ec2.instances.filter(
    Filters=[
        {
            'Name': 'tag:k8s.io/role/master',
            'Values': [
                '1'
            ],
            'Name': 'instance-state-code',
            'Values': [
                '16'
            ]
        },
    ],
    DryRun=False,
    MaxResults=10
)

inst_names = [tag['Value'] for i in instance_iterator for tag in i.tags if tag['Key'] == 'Name']
print(inst_names)
print("***")
