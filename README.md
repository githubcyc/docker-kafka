## docker-kafka


* kafka config from offical .tgz,  edit it and mount via -volumns

* edit /config/server.properties  

* change localhost to service name of zookeeper in docker-compose.yml, e.g.:
```
zookeeper.connect=zoo:2181
```

### How to run

```
docker-compose up
```
