# aitools_admin
AiKloud Admin Application

The Admin (Adama) Application helps to approve Ai Tools Submission.

Run the download_nltk.py script once to enable searfch application


1. Install Git
`sudo yum install git`

2. Git Clone the aitools_admin repo
remember to use your github token as password
`git clone https://github.com/flukkytom/aitools_admin.git`

To create Tokens for Password for Git Clone
===========================================

`Tokens: https://www.educative.io/answers/how-to-create-a-personal-access-token-for-github-access`

4. Install Virtualenv
`yum install virtualenv`

5. Create a virtual environment (cd into your repo directory)
`virtualenv environment`

6. Activate your Virtual Environment
`source environment/bin/activate`

7. Install GCC
`yum install gcc`

8. Install Python Devel
`yum install python-devel`

9. Find Mysql Devel
`sudo yum search mysql | grep devel`

10. Install the Devel found (Mine was mariadb105-devel)
`sudo yum install mariadb105-devel`

11. Install the Application requirements
`pip install -r requirements.txt`
(If you encounter a pip not found error: use `yum install pip`)

13. Run the NLTK script
`python app/functions/download_nltk_data.py`

14. Update the application Config.py with your Database Connection details (See Database Connection below)

15. Run your Application
`python application.py`

Database Connection
===================
If you get your database connection strings

edit the file config.py
`SQLALCHEMY_DATABASE_URI = 'mysql://<database_user>:<database_password>@<endpoint>/<database_name>'`








