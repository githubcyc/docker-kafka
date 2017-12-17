# docker-kafka


kafka config from offical .tgz,  edit it and mount via -volumns

edit /config/server.properties  

change localhost  to  service name of zookeeper in dockercompose.yml, e.g.:
```
zookeeper.connect=zoo:2181
```

run with

```
docker-compose up
```
