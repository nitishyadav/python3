#####################################################################################################
# Author : Nitish K Yadav                                      #
# Desc   : Script is written to create vpc, internet gateway,nat gateway and public and private subnet  #
# Parametrs:As of now taking through command line arguments
#http://blog.kaliloudiaby.com/index.php/terraform-to-provision-vpc-on-aws-amazon-web-services/
######################################################################################################
from terrascript import *
from terrascript.aws.r import *
#from terrascript.aws.d import *
import json
import os
import sys,logging

#provider information
provider('aws', region='ap-south-1')

#vpc creation,and enabling DNS support to the VPCand also enable VPC for DNS hostname
aws_vpc('default',cidr_block = vpccidr , instance_tenancy ='dedicated',enable_dns_support = 'true',enable_dns_hostnames = 'true',tags={'Name':'my_vpc'})

#This will get the vpc id that just got created by above aws_vpc
vpc_id = '${aws_vpc.default.id}'
#print(vpc_id)

#Public subnet creation, and attaching public ip to it on launch
aws_subnet('ap-south-1a-public',vpc_id = '${aws_vpc.default.id}', cidr_block=pubsubnetcidr,map_public_ip_on_launch = 'true',availability_zone='ap-south-1a',tags={'Name':'publicsubnet'})

#private subnet creation
aws_subnet('ap-south-1a-private',vpc_id = '${aws_vpc.default.id}', cidr_block=pvtsubnetcidr,availability_zone='ap-south-1a',tags={'Name':'privatesubnet'})

#Internet Gateway
aws_internet_gateway('gw',vpc_id='${aws_vpc.default.id}',tags={'Name':'InternetGateway'})

#Create route to the internet
aws_route('internet_access',route_table_id='${aws_vpc.default.main_route_table_id}',destination_cidr_block='0.0.0.0/0',gateway_id='${aws_internet_gateway.gw.id}')
#gateway_id: Gateway ID, where all the packets to the internet should be routed through, if you remember the Internet Gateway allow you VPC to communicate with the Internet.

#Create Elastic IP(EIP)
#we create this IP to assign to NAT gateway
aws_eip('default_eip',vpc ='true',depends_on=['aws_internet_gateway.gw'])

#Create NAT Gateway
#allocation_id = The NAT should have an EIP
#Subnet_id=Subnet ID in which NAT resource will be created
aws_nat_gateway('nat',allocation_id='${aws_eip.default_eip.id}',subnet_id='${aws_subnet.ap-south-1a-public.id}',depends_on=['aws_internet_gateway.gw'])

#Create Private route table and the route to the internet
#This will allow all traffics from the private subnets to the internet through the NAT Gateway
aws_route_table('private_route_table',vpc_id='${aws_vpc.default.id}',tags={'Name':'Private route table'})
aws_route('private_route',route_table_id='${aws_route_table.private_route_table.id}',destination_cidr_block = '0.0.0.0/0',nat_gateway_id='${aws_nat_gateway.nat.id}')

#To stringify the output of the dump()
jsonstr=dump()
jsonobj=json.loads(jsonstr)

#writing to the json file we need in the end
with open("vpc_internetgateway.tf.json","w")as outfile:
    json.dump(jsonobj,outfile)
print(dump())

#how to run
#python3.6 vpcigsubnet.py '20.20.20.0/24' '20.20.20.0/27' '20.20.20.64/27'