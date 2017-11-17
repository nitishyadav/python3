from terrascript import provider, dump,variable, output,provisioner,connection
from terrascript.aws.r import aws_instance
from terrascript.aws.r import aws_key_pair
import json
import os
import sys
import logging

provider('aws', region='ap-south-1')


#aws_key_pair('test_keypair',key_name='id_rsa.pub')
#public_key= '${file("/home/cloud_user/.ssh/id_rsa.pub")}')

conn = connection(type='ssh',user='ec2-user',private_key='${file("/home/cloud_user/.ssh/id_rsa")}')

prov = provisioner('file',source = '/home/cloud_user/python_terrorm_templates/script_terrascript/test.sh',destination='/tmp/test.sh',connection=conn)
prov1=provisioner('remote-exec',inline =['chmod +x /tmp/test.sh','/tmp/test.sh'],connection=conn)

aws_instance('test_instance', ami='ami-2ed19c41', instance_type='t2.micro',key_name='id_rsa',provisioner=[prov,prov1])

#tags(Name='Terraform')

output('public_ip',value = '${aws_instance.test_instance.public_ip}')
jsonstr = dump()
jsonobj=json.loads(jsonstr)

with open("ec2-httpd.tf.json",'w')as outfile:
    json.dump(jsonobj,outfile)
# Print the JSON-style configuration to stdout.
print(dump())




#scp -i /home/cloud_user/.ssh/id_rsa /home/cloud_user/python_terrorm_templates/script_terrascript/test.sh ec2-user@13.126.88.101:~/.
#Terraform
