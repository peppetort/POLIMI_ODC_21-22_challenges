import os
#web
# DB_URI = 'sqlite:////tmp/test.db'
DB_URI = 'mysql+pymysql://%s:%s@localhost/%s' % ("admin", "admin", "base")
print(DB_URI)
SECRET_KEY = "ciao"
