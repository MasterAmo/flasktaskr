import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True  # WTF_CSRF_ENABLED config setting is used for cross-site request forgery prevention, which makes your app more secure
SECRET_KEY = '\xf2O>s3\n\xbd\xf9\xfe\xa1_N/y\x0e\x91\x9f\xc2\xbe\xb2\xd5R8\xd5'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
