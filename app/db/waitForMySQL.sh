#!/bin/sh
# wait until MySQL is really available and ready to accept connections
 
mysql -uroot -p"$MYSQL_ROOT_PASSWORD" -e "ALTER USER '$MYSQL_USER'@'%' IDENTIFIED WITH mysql_native_password BY '$MYSQL_PASSWORD'; flush privileges;"