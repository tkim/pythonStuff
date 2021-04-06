import os

# set user / password and create environment variable DB_USER and DB_PASS under user env.
# DB_USER = 'my_db_user'
# DB_PASS = 'my_db_pw_123!'

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

print(db_user)
print(db_password)

