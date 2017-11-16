#####################################################################################################
# Author : Nitish K Yadav                                      #
# Desc   : Create ec2 instance in aws and then  es the script there which will dothe installation  #
# Parametrs:As of now taking through command line arguments
######################################################################################################
from terrascript import provider, dump,variable, output,provisioner,connection
from terrascript.aws.r import aws_instance
from terrascript.aws.r import aws_key_pair
import json
import os
import sys
import logging

ami_id=''
instance_type=''

def getami(ami_id):
    #This method will get the ami id
    print (ami_id)
    return ami_id

def getinst_type(instance_type):
    #This will return the instance_type
    print(instance_type)
    return instance_type

amiid=getami(sys.argv[1])
instancetype=getinst_type(sys.argv[2])
keyname=sys.argv[3]
privatekey=sys.argv[4]
source1=sys.argv[5]
source2=sys.argv[6]


#provider('aws', access_key=' AKIAJ3IBSGR743T2EPBA',secret_key='Vv7S+ kQ62OP71on7Ampq/aBCy3nJyUoCdl9iiMKX', region='ap-south-1')
provider('aws',region='ap-south-1')

#aws_key_pair('test_keypair',key_name='id_rsa.pub')
#public_key= '${file("/home/cloud_user/.ssh/id_rsa.pub")}')

conn = connection(type='ssh',user='ec2-user',private_key='${file('+privatekey+')}')

prov = provisioner('file',source = source1,destination='/tmp/script.sh',connection=conn)

prov0=provisioner('file',source= source2,destination='/tmp/user.properties',connection=conn)

prov1=provisioner('remote-exec',inline =['chmod +x /tmp/script.sh','chmod +x /tmp/user.properties','/tmp/script.sh'],connection=conn)

#Aws instance
aws_instance('test_instance', ami=amiid, instance_type=instancetype,key_name=keyname,provisioner=[prov,prov0,prov1],tags={'Name':'ec2_terraform'})

#name('Terraform')

output('public_ip',value = '${aws_instance.test_instance.public_ip}')
jsonstr = dump()
jsonobj=json.loads(jsonstr)

with open("ec2-propertyfile.tf.json",'w')as outfile:
    json.dump(jsonobj,outfile)
# Print the JSON-style configuration to stdout.
print(dump())

# python3.6 ec2_propertyfile.py ami-2ed19c41 t2.micro id_rsa '/home/cloud_user/.ssh/id_rsa' '/home/cloud_user/python_terrorm_templates/script_propertyfile/script.sh' '/home/cloud_user/python_terrorm_templates/script_propertyfile/user.properties'