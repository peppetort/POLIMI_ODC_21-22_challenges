sudo docker stop some-mysql && sudo docker rm some-mysql && sudo docker run --name some-mysql -e MARIADB_ROOT_PASSWORD=root -e MARIADB_DATABASE=base -e MARIADB_USER=admin -e MARIADB_PASSWORD=admin -p 3306:3306 -d mariadb
