#!/bin/sh
# wait until MySQL is really available and ready to accept connections
 
mysql -uroot -p"$MYSQL_ROOT_PASSWORD" -e "show databases;"