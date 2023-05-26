import pika
rabbitmq_host = "localhost"
rabbitmq_port = 5672
rabbitmq_exchange = "grades"


def rabbitmqMessage(message="error", routing_key="error"):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port)
    )
    

    
    channel = connection.channel()

    channel.queue_declare(queue=routing_key)

    channel.basic_publish(
        exchange='', routing_key=routing_key, body=message
    )

    connection.close()