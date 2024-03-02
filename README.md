# Project setup and workflow

**Requirements**

1. Create free AWS root account and create a user group with administrator privileges. After that, create an IAM user and assign him to previously created user group. Visit the IAM user profile and find a section with access keys. Keep both public and secret key, as you will need them for later.
2. Make sure to have installed Node.js and npm, python3 and AWS CLI.
3. Run the command **npm install -g serverless** (in case it does not work, try with "**sudo npm install -g serverless**"). 
4. Run the command **aws configure**. This will prompt you to enter public and secret keys of IAM user we previously created.
5. Run the command **pip3 install boto3 flask**. Boto3 is needed for AWS SDK, and Flaks is needed for flask framework.
--------------

**Start of the project**

Now that we are all set with the requirements, we need to create a virtual environment locally, with **python3 -m venv venv** in the project repository we previously created.
To activate virtual environment, I remind you for WIN command is **venv/Scripts/activate** while for Mac/Linux its **source venv/bin/activate**
To initialize the project, we position ourselves inside the project repository, and run **serverless create --template aws-python3 --path our-project-name**, and then position inside that project name directory.
