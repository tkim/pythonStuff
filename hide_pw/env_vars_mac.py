import os

# In Mac  update .bash_profile from terminal
# nano .bash_profile
# export DB_USER="my_db_user"
# export DB_PASS="my_db_pw_123!"
#
# Add to $PATH. Lower ones have higher priority.
# 
# ctrl X and Yes to Save and exit from nano


db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

print(db_user)
print(db_password)