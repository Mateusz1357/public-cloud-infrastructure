# public-cloud-infrastructure

In order to perform this task, I chose the public cloud, AWS, and used CloudFormation as the Infrastructure as code tool. Using the yaml code, I created an EC2 instance that uses User Data to set up an nginx server with a simple static page displaying Hello World. I expanded this infrastructure taking care of good security practices. I additionally configured Application Load Balancer, which balances traffic to two EC2 instances located in different subnets in order to obtain a highly available infrastructure. As a security element, I've set up security groups that restrict the allowed incoming traffic to the EC2 instance. Finally, I configured a bucket in the Amazon S3 service, which receives previously set Flog Logs monitoring network traffic inside the VPC virtual network.

![image](https://user-images.githubusercontent.com/107367815/209612169-4558e3e9-38a2-4a9b-ad0a-ff762b91eb06.png)
