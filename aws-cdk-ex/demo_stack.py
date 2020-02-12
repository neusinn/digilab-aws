from aws_cdk import core
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_autoscaling as autoscaling
from aws_cdk import aws_elasticloadbalancingv2 as elbv2

# Hint 1: Add modules in setup.py and run pip install -r requiremnts.txt
# Hint 2: Cleanup resources with $ cdk destroy ! Otherwise you get charged

class DemoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        # Create a VPN named 'Digilab-Demo2VPC' with 2 availability zones and 2 subnets, a public and a private one
        vpc= ec2.Vpc(self, 'Digilab-Demo2VPC',
            cidr='10.1.0.0/16',
            max_azs=2,
            subnet_configuration=[
                { 'cidrMask': 24, 'name': 'Web', 'subnetType': ec2.SubnetType.PUBLIC},
                { 'cidrMask': 24, 'name': 'Application', 'subnetType': ec2.SubnetType.PRIVATE},
            ]
        )

        # Create a auto scaling Group named "Digilab-ASG" of ec2-micro instances with AmazonLinux
        asg = autoscaling.AutoScalingGroup(self, "Digilab-ASG",
            vpc=vpc,
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.MICRO),
            machine_image=ec2.AmazonLinuxImage()
        )


        # Install Apache webserver and a dummmy index.html. Then start the webserver.
        asg.add_user_data(
            """
            yum update -y
            yum install httpd -y
            echo 'Hello from the Digilab Web App' > /var/www/html/index.html
            service httpd start
            chkconfig httpd on
            """
        )


        # Add a LoadBalancer named "Digilab-LB" in front of the webservers
        lb = elbv2.ApplicationLoadBalancer(
            self, "Digilab-LB",
            vpc=vpc,
            internet_facing=True
        )


        listener = lb.add_listener("Listener", port=80)
        listener.add_targets("Target", port=80, targets=[asg])
        listener.connections.allow_default_port_from_any_ipv4("Open to the world")
