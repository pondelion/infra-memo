

```bash
$ set -o allexport && source .env && set +o allexport
```

```bash
$ sudo docker volume rm mysql_mysql-data
```

```bash
$ sudo docker-compose up -d
```

```bash
$ sudo docker logs mysql_db_container
2022-02-26 06:29:35+09:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.28-1debian10 started.
2022-02-26 06:29:36+09:00 [Note] [Entrypoint]: Switching to dedicated user 'mysql'
2022-02-26 06:29:36+09:00 [Note] [Entrypoint]: Entrypoint script for MySQL Server 8.0.28-1debian10 started.
2022-02-26 06:29:36+09:00 [Note] [Entrypoint]: Initializing database files
2022-02-25T21:29:36.955207Z 0 [System] [MY-013169] [Server] /usr/sbin/mysqld (mysqld 8.0.28) initializing of server in progress as process 41
2022-02-25T21:29:37.077587Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2022-02-25T21:29:47.689906Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2022-02-25T21:30:25.171498Z 6 [Warning] [MY-010453] [Server] root@localhost is created with an empty password ! Please consider switching off the --initialize-insecure option.
2022-02-26 06:32:24+09:00 [Note] [Entrypoint]: Database files initialized
2022-02-26 06:32:24+09:00 [Note] [Entrypoint]: Starting temporary server
2022-02-25T21:32:48.914673Z 0 [System] [MY-010116] [Server] /usr/sbin/mysqld (mysqld 8.0.28) starting as process 90
2022-02-25T21:32:53.598698Z 1 [System] [MY-013576] [InnoDB] InnoDB initialization has started.
2022-02-25T21:33:03.213957Z 1 [System] [MY-013577] [InnoDB] InnoDB initialization has ended.
2022-02-25T21:33:17.655640Z 0 [Warning] [MY-010068] [Server] CA certificate ca.pem is self signed.
2022-02-25T21:33:17.655824Z 0 [System] [MY-013602] [Server] Channel mysql_main configured to support TLS. Encrypted connections are now supported for this channel.
2022-02-25T21:33:18.413373Z 0 [Warning] [MY-011810] [Server] Insecure configuration for --pid-file: Location '/var/run/mysqld' in the path is accessible to all OS users. Consider choosing a different directory.
2022-02-25T21:33:21.889510Z 0 [System] [MY-011323] [Server] X Plugin ready for connections. Socket: /var/run/mysqld/mysqlx.sock
2022-02-25T21:33:21.889648Z 0 [System] [MY-010931] [Server] /usr/sbin/mysqld: ready for connections. Version: '8.0.28'  socket: '/var/run/mysqld/mysqld.sock'  port: 0  MySQL Community Server - GPL.
2022-02-26 06:33:23+09:00 [Note] [Entrypoint]: Temporary server started.
Warning: Unable to load '/usr/share/zoneinfo/iso3166.tab' as time zone. Skipping it.
Warning: Unable to load '/usr/share/zoneinfo/leap-seconds.list' as time zone. Skipping it.
Warning: Unable to load '/usr/share/zoneinfo/zone.tab' as time zone. Skipping it.
Warning: Unable to load '/usr/share/zoneinfo/zone1970.tab' as time zone. Skipping it.
2022-02-26 06:35:42+09:00 [Note] [Entrypoint]: Creating database test_db
2022-02-26 06:35:44+09:00 [Note] [Entrypoint]: Creating user test_user
2022-02-26 06:35:45+09:00 [Note] [Entrypoint]: Giving user test_user access to schema test_db

2022-02-26 06:35:45+09:00 [Warn] [Entrypoint]: /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/01_ddl.sql.example

2022-02-26 06:35:45+09:00 [Warn] [Entrypoint]: /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/02_dml.sql.example

2022-02-26 06:35:45+09:00 [Note] [Entrypoint]: Stopping temporary server
2022-02-25T21:35:46.281314Z 13 [System] [MY-013172] [Server] Received SHUTDOWN from user root. Shutting down mysqld (Version: 8.0.28).
```

```bash
$ mysql -h 127.0.0.1 -P 3307 -u root -p
```

```bash
$ sudo docker-compose down
```