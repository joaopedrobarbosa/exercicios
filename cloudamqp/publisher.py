import pika, os

url = os.environ.get('CLOUDAMQP_URL', 'amqps://kdtbtirf:ZMAfLPaKnBnwKR0oYFY3odqTNhxl_BZo@jackal.rmq.cloudamqp.com/kdtbtirf')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                    routing_key='hello',
                    body='Hello CloudAMQP!')

print(" [x] Sent 'Hello World!'")
connection.close()