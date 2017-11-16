from terrascript import provider, dump
from terrascript.aws.r import aws_instance
import json
import os
import sys
import logging


#logging.basicConfig(filename="discovery-josn-logs.logs", level=logging.INFO)
#jsonobj = {"resource": {"aws_instance": {"example": {"ami": sys.argv[1], "instance_type": sys.argv[2]}}}}
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

aws_instance('example', ami=amiid, instance_type=instancetype)

#jsonobj = {"resource": {"aws_instance": {"example": {"ami":amiid , "instance_type":instancetype}}}}
logging.basicConfig(filename="discovery-josn-logs.logs", level=logging.INFO)

jsonstr = dump()
jsonobj = json.loads(jsonstr)

with open("data.tf.json",'w')as outfile:
    json.dump(jsonobj, outfile)

#print(jsonobj)
print(dump())