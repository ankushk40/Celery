import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='Hey')

channel.basic_publish(exchange='', routing_key='Hey', body='Hey Everyone! This is our test message code')
print(" [x] Sent 'Hey Everyone! This is our test message code'")
connection.close()