# aitools_admin
AiKloud Admin Application

The Admin (Adama) Application helps to approve Ai Tools Submission.

Run the download_nltk.py script once to enable searfch application


1. Install Git
sudo yum install git

2. Git Clone the aitools_admin repo
remember to use your github token as password

3. Install Virtualenv
yum install virtualenv

4. Create a virtual environment (cd into your repo directory)
virtualenv environment

5. Activate your Virtual Environment
source environment/bin/activate

6. Install GCC
yum install gcc

7. Install Python Devel
yum install python-devel

8. Find Mysql Devel
sudo yum search mysql | grep devel

9. Install the Devel found (Mine was mariadb105-devel)
sudo yum install mariadb105-devel

10. Install the Application requirements
pip install -r requirements

11. Install the NLTK library
pip install nltk

12. Run the NLTK script
python app/functions/download_nltk_data.py

13. Run your Application
python application.py

Database Connection
===================
If you get your database connection strings

edit the file config.py
SQLALCHEMY_DATABASE_URI = 'mysql://<database_user>:<database_password>@<endpoint>/<database_name>'








