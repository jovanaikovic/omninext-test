# **Project setup and workflow**

**Requirements**

1. Create free AWS root account and create a user group with administrator privileges. After that, create an IAM user and assign him to previously created user group. Visit the IAM user profile and find a section with access keys. Keep both public and secret key, as you will need them for later.
2. Make sure to have installed Node.js and npm, python3 and AWS CLI.
3. Run the command **npm install -g serverless** (in case it does not work, try with "**sudo npm install -g serverless**"). 
4. Run the command **aws configure**. This will prompt you to enter public and secret keys of IAM user we previously created.
5. Run the command **pip3 install boto3 flask**. Boto3 is needed for AWS SDK, and Flaks is needed for flask framework.
--------------

**Start of the project**

Now that we are all set with the requirements:
1. We need to create a virtual environment locally, with **python3 -m venv venv** in the project repository we previously created.
2. To activate virtual environment, I remind you for WIN command is **venv/Scripts/activate** while for Mac/Linux its **source venv/bin/activate**
3. To initialize the project, we position ourselves inside the project repository, and run **serverless create --template aws-python3 --path our-project-name**, and then position inside that project name directory.
4. When the project is created, fill the necessary files **handler.py** and **serverless.yml** with needed code, so the test can work.
5. After everything is done, run **serverless deploy** to deploy everything so the test can work.
--------------

# **Important notes**

1. Highly important is to make sure that through AWS Console, we added adequate policies for permissions for IAM user who is not root. I suggest adding **CloudDirectoryFullAccess, AmazonDynamoDBFullAccess, AWSLambdaFullAccess**, as well as custom policies I created for the purposes of smooth running.

**Bucket Policy**
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": [
				"s3:PutObject",
				"s3:GetObject",
				"s3:ListBucket"
			],
			"Resource": [
				"arn:aws:s3:::*"
			]
		}
	]
}

**Cloud&API policy**
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Stmt1449904348000",
			"Effect": "Allow",
			"Action": [
				"cloudformation:CreateStack",
				"cloudformation:CreateChangeSet",
				"cloudformation:ListStacks",
				"cloudformation:UpdateStack",
				"cloudformation:DescribeStacks",
				"cloudformation:DescribeStackResource",
				"cloudformation:DescribeStackEvents",
				"cloudformation:ValidateTemplate",
				"cloudformation:DescribeChangeSet",
				"cloudformation:ExecuteChangeSet",
				"cloudformation:GetTemplateSummary",
				"cloudformation:DeleteChangeSet",
				"apigateway:GET",
				"apigateway:POST",
				"apigateway:DELETE",
				"apigateway:PUT"
			],
			"Resource": [
				"*"
			]
		}
	]
}

**DB Help Policy**
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Action": "dynamodb:PutItem",
			"Resource": "arn:aws:dynamodb:us-east-1:891377357282:table/Users"
		}
	]
}
-----------------

# **Testing**
I tested the endpoints using postman, sending POST request to the endpoint /user, and GET request to the endpoint /user/{id}. Postman collection file is attached.
