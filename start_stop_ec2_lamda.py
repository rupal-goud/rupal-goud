import json
import boto3

instance_ids_list= ['i-0c9f0d24caad683cb']
region='us-east-1'
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    
    print(event)
    
    action = event["action"]
   
    if action == 'start':

        # Stop the instance
        ec2.start_instances(
               InstanceIds=instance_ids_list,
        )
        print("Successfully started instance: " +str(instance_ids_list))
    
    # If this is the hour of stopping it...
    elif action == 'stop':
        # Stop the instance
        ec2.stop_instances(
            InstanceIds=instance_ids_list,
        )
        print("Successfully stopped instance: " +str(instance_ids_list))