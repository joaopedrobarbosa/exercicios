import pika, os

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queu='test_queue')

def callback(ch, method, properties, body):
    print(' [x] Received ' +  str(body))

channel.basic_consume(
    'test_queue',
    callback,
    auto_ack=True
)

print(' [*] Waiting for Messages: ')
channel.start_consuming()
connection.close()