import pymysql

# "Engana" o Django simulando uma versão compatível do mysqlclient
pymysql.version_info = (2, 2, 7, "final", 0) 

pymysql.install_as_MySQLdb()
