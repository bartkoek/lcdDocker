import pika
from grove_rgb_lcd import *
import time

if __name__ == '__main__':
    pika_conn_params = pika.ConnectionParameters(
        host='localhost', port=5672,
        credentials=pika.credentials.PlainCredentials('guest', 'guest'),
    )
    while True:
        connection = pika.BlockingConnection(pika_conn_params)
        channel = connection.channel()
        queue = channel.queue_declare(
            queue="hello"
        )

        msgCount = queue.method.message_count
        setText_norefresh("berichtjes: " + str(msgCount))
        time.sleep(0.2)
