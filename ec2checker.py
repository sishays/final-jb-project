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
exit()



for instance in ec2.instances.all():
    print(instance)
    print("IN INSTACE")
    print(instance.tags)
    for tag in instance.tags:
        print("IN TAG")
        print(tag)
        print("HELLO!!!!!!!!!!")
        print(tag['Key'])
        #print(tag['Name'])
        #if tag['Key'] == 'Name': testName = tag
        #print(testName)
        if tag['Key'] == "k8s.io/role/master":
           print(instance)
           #lala = tag['Key'] == 'Name'
           print(tag)


# instance_iterator = ec2.instances.filter(
#     Filters=[
#         {
#             'Name': 'string',
#             'Values': [
#                 'string'
#             ]
#         },
#     ],
#     InstanceIds=[
#         'string'
#     ],
#     DryRun=False,
#     MaxResults=10
#)