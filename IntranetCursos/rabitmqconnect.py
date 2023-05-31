import pika
import datetime 
import json

rabbitmq_host = "localhost"
rabbitmq_port = 5672


def rabbitmqMessage(message="error", routing_key="error"):

    log={
        "timestamp": datetime.datetime.now().isoformat(),
        "Level": routing_key,
        "Message": json.dumps(message)
    }

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port)
    )
        
    channel = connection.channel()

    channel.queue_declare(queue="logs")

    channel.basic_publish(
        exchange='', routing_key="logs", body=json.dumps(log)
    )

    connection.close()