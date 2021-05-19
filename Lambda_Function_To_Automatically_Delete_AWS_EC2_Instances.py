#python 3.6

import boto3
import json

def lambda_handler(event,context):
                                                              
    regions=['us-east-1','us-east-2','us-west-1','us-west-2'] #regions = in regions where your instances are deployed
    for j in regions:                                         #loop,so that code will be executed in regions defined in regions list
        instances = []                                        #instance ids will be appended in this list
        ec2 = boto3.client('ec2',region_name=j)
        response = ec2.describe_instances()
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                if instance['State']['Name'] != 'terminating': #Condition for excluding terminated instances
                    #print(instance["InstanceId"])
                    instances.append(instance["InstanceId"])  
                    #print(instances)
            ec2.terminate_instances(InstanceIds=instances)    #terminating instances
