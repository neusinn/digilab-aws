import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="demo",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",


    author="author",


    package_dir={"": "demo"},
    packages=setuptools.find_packages(where="demo"),


    install_requires=[
        "aws-cdk.core",
        "aws_cdk.aws_ec2",
        "aws_cdk.aws_autoscaling",
        "aws_cdk.aws_elasticloadbalancingv2"
    ],


    python_requires=">=3.6",
    

    classifiers=[
        "Development Status :: 4 - Beta",


        "Intended Audience :: Developers",


        "License :: OSI Approved :: Apache Software License",


        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",


        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",


        "Typing :: Typed",
    ],
)
