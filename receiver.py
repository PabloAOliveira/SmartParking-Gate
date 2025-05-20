import pika
import serial
import time

# Conexão serial com Arduino
serial_port = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)

# Conexão com RabbitMQ Cloud
url = "amqps://hvpxnovf:CH77RwnodPscpjvXfe3jy73jUVCYHpW7@jaragua.lmq.cloudamqp.com/hvpxnovf"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

fila = 'sensor_presenca'
channel.queue_declare(queue=fila, passive=True)

print("Aguardando mensagens...")

ultimo_comando = 0

while True:
    # Só lê mensagens se já passaram 6 segundos desde o último comando
    if time.time() - ultimo_comando >= 6:
        method_frame, header_frame, body = channel.basic_get(queue=fila, auto_ack=True)

        if method_frame:
            mensagem = body.decode().strip()
            print("Mensagem recebida:", mensagem)

            if mensagem == '1':
                print(">>> Enviando '1' para o Arduino")
                serial_port.write(b'1\n')
                ultimo_comando = time.time()  # Marca tempo do último comando
    else:
        # Durante o tempo de espera, esvazia mensagens acumuladas
        channel.basic_get(queue=fila, auto_ack=True)

    time.sleep(0.1)
