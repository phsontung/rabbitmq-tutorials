# Introduction
- A simple application that demo rabbitmq use pika client
- Add docker-compose for easy to build and start

# Setup
## Start rabbitmq/applications
### Ignore deploy (replicas) options
```
docker-compose up
```
### Deploy with replicas options
```
docker-compose --compatibility up
```

## Start consumer
### To receive all the logs run:
```
python consumer.py "#"
```
### To receive all logs from the facility "kern":
```
python consumer.py "kern.*"
```

### Or if you want to hear only about "critical" logs:
```
python consumer.py "*.critical"
```
### You can create multiple bindings:
```
python consumer.py "kern.*" "*.critical"
```

## Start producer
```
python producer.py "kern.critical" "A critical kernel error"
```

# Refs:
- https://www.rabbitmq.com/tutorials/tutorial-two-python.html
- https://www.rabbitmq.com/tutorials/tutorial-five-python.html