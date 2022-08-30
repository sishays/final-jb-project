import boto3
import sys
import time

def scan_instances():
    ec2 = boto3.resource('ec2')

#### In order to scan by other tags you can change or add Name and Value pairs
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

#    inst_names = [tag['Value'] for i in instance_iterator for tag in i.tags if tag['Key'] == 'Name']

    print("***")
    for instance in instance_iterator:
        ec2_name = [tag['Value'] for tag in instance.tags if tag['Key'] == 'Name']
        ec2_ip = instance.public_ip_address
        ec2_type = instance.instance_type
        print("Instance name: {0}\nIP address: {1}\nType: {2}\n***".format(ec2_name, ec2_ip, ec2_type))

# Main
try:
    interval = sys.argv[1]
except IndexError:
    interval = None

if interval == None:
    scan_instances()
else:
    while True:
        scan_instances()
        print("Sleeping for {0} seconds!".format(interval))
        time.sleep(int(interval))