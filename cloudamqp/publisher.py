import pika, os

url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare('text_exchange')
channel.queue_declare(queue='test_queue')
channel.queue_bind('test_queue', 'test_exchange', 'tests')

channel.basic_publish(
    body="Hello RabbitMQ!",
    exchange="test_exchange",
    routing_key='tests'
)

print(' Message sent. ')
channel.close()
connection.close()