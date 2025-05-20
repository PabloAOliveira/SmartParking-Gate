import serial
import pika
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)

rabbitmq_url = 'amqps://hvpxnovf:CH77RwnodPscpjvXfe3jy73jUVCYHpW7@jaragua.lmq.cloudamqp.com/hvpxnovf'
params = pika.URLParameters(rabbitmq_url)
connection = pika.BlockingConnection(params)

channel = connection.channel()
queue_name = 'sensor_presenca'
channel.queue_declare(queue=queue_name)

print("Lendo da serial e enviando ao RabbitMQ...")

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            if data in ["0", "1"]:
                print(f"Recebido: {data} - Enviando para RabbitMQ...")
                channel.basic_publish(exchange='',
                                      routing_key=queue_name,
                                      body=data)
except KeyboardInterrupt:
    print("Encerrando...")

finally:
    ser.close()
    connection.close()
