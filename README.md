# 🚗 SmartParking-Gate – Sistema de Controle de Cancela

Este projeto simula um sistema inteligente de controle de cancela automatizada para estacionamentos, utilizando **Arduino**, **Raspberry Pi**, **RabbitMQ** e **Python**.

---

## 🔧 Tecnologias Utilizadas

- 🐍 Python
- 🐇 RabbitMQ
- 💻 Raspberry Pi
- ⚙️ Arduino (C)
- 🔌 Comunicação Serial
- 💡 Sensor de proximidade
- 🔄 Servo Motor + LEDs

---

## 🧠 Como Funciona

1. **Sensor de Proximidade (no Arduino)** detecta a presença de um veículo. (feito por outro grupo/colega)
2. O **Arduino** envia o sinal `0` (ausente) ou `1` (presente) via **porta serial** para a **Raspberry Pi**. (feito por outro grupo/colega)
3. A **Raspberry Pi** roda o `producer.py`, que lê os dados da serial e publica na fila do **RabbitMQ**. (feito por outro grupo/colega)
4. Um **consumer** recebe da fila o 0 ou 1 e aciona: 
   - 🔓 Cancela (servo motor)
   - 🔴 LED vermelho (sem presença)
   - 🟢 LED verde (presença detectada)

---

- Pablo Antonio De Oliveira
- Gabriela Lenz
- Patricia Lima Massolini
- Pedro Bartz 1135935
- Rafael Pedra 1136090
