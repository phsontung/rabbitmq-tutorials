import pika
import sys
import time
import logging

LOGGER = logging.getLogger(__name__)

LOGGER.warning('Prepare to start consumer .....')
time.sleep(20) # Hack here to wait for rabbitmq when run with docker-compose

connection = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@rabbitmq:5672/%2F'))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)

LOGGER.warning(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    LOGGER.warning(" [x] %r:%r" % (method.routing_key, body))

channel.basic_qos(prefetch_count=1)
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()