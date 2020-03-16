# Infrastructure as Code (IaC) with AWS Cloud Development Kit (AWS-CDK)

The AWS [Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/home.html) (AWS CDK) is an opinionated, 
open-source software development framework to define cloud infrastructure in code [CDK API](https://docs.aws.amazon.com/cdk/latest/guide/reference.html) 
and provision it through [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

It offers a high-level object-oriented abstraction to define AWS resources imperatively using the power of modern programming languages.
It allows to build and deploy applications without worrying about the underlying infrastructure details.
It generates CloudFormation code. 

                                         
## Example Target topology
- A VPC
- 2 Availability zones
- with 2 subnets:
    - 1 Private subnet with a Webserver
    - 1 Public subnet with a NAT Gatway and Elasitc IP
- 1 Internet Gateway
- 1 Elastic Load balancer


## Blueprint
[Blueprint für eine Statische Web Seite in einem S3 Bucket](./Blueprint_Ex_IaC.png)


## Project structure of aws-cdk-ex
```
├── README.md
├── demo_stack.py                // example IaC
├── output
│   ├── deployed_resources.txt   // list of generated and deployed resources
│   └── out_resources.yaml       // output of Cloud Formation YAML
└── setup.py                     // environment setup

```


## Setup
### Setup Cloud9 Development Environment and CDK:
1. Create a Cloud9 with a EC2 instance
    - t2.small instance, Amazon Linux, leaf other settings as default
2. Install CDK `npm install -g aws-cdk`
    - Check with `cdk --version` / `cdk --help`
3. Initialize the working folder and setup for language (here Python 3) 
    - `mkdir demo`
    - `cd demo`
    - `cdk init --languate python` --> setup a virtual environment
4. activate virtual environment `source .env/bin/activate`
5. Download and install requirements `pip install -r requirements.txt` After each time you added a new AWC-CDK module rerun this command.
6. Make changes to the environment
    - Python version: Python 3
    - Add folder with dist python packages to python path. Check the correct path first.  e.g. `/home/ec2-user/environment/demo/.env/lib/python3.7/dist-packages`     
    - (only first time) `cdk botsstrap` this creates staging resources required by the CDK
5. `cdk synth` Check initialisation.
 
### Coding infrastructure with AWS CDK
- Add CDK modules:
    - Search for name. E.g. `aws cdk ec2` for aws-ec2 module documentation
    - Add module in file `setup.py` install_requiremnts = ["aws_cdk.core", <add module>],
    - `pip install -r requirements.txt` to download and install new module

### Running the Code - create the infrastructure
1. Change to project `demo
    ```
    cd demo
    ```
2. Activate the environment
    ```
   source .env/bin/activate
    ```
3. Preview what will be built
    ```
    cdk synth
    ```
4. Deploy the stack and built infrastructure. This will take 4-5 minutes until the infrastructure is created.
    ```
    cdk deploy
    ```
5. After usage **Cleanup resources with `$ cdk destroy`** ! Otherwise you get charged    
    ```
    cdk destroy
    ```
  
 
 ### Test the Web-App
 In the AWS console open EC2- Dashboard and navigate to loadbalancer demo-Digilab-LB and copy the DNS name. 
 Open a browser and paste the DNS name to go to the website.
 
## Hints:
 1. After adding modules in setup.py and run pip install -r requirements.txt
 2. **Cleanup unused cdresources with `$ cdk destroy`** ! Otherwise you get charged 
 3. Use `source .env/bin/activate` to activate the virtual environment. ( From folder `/home/ec2-user/environment/demo`)
 
   
### Useful commands to work with CDK
 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation 
 
 ## Resources
 
 - AWS Cloud [Development Kit](https://aws.amazon.com/cdk/) and [Documentation](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
 - AWS Cloud Formation [Documentation](https://docs.aws.amazon.com/cloudformation/index.html)
 - AWS CDK [API Developer Guide and API Reference](https://docs.aws.amazon.com/cdk/api/latest)  and [Python API Reference](https://docs.aws.amazon.com/cdk/api/latest/python/modules.html)
 - AWS CDK Code on [Github](https://github.com/aws/aws-cdk)
 - AWS CDK [workshop](https://cdkworkshop.com)

 
 The example was made during the recommended course "AWS Infrastructure as Code for Software Developers" from ACloudGuru. See [A Clout Guru](https://acloud.guru) for their trainings. 
 Also available trough LinkedIn Course: [AWS Infrastructure as Code for Software Developers](https://www.linkedin.com/learning/aws-infrastructure-as-code-for-software-developers)
 
                 