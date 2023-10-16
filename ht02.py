import simpy
import random

M = 1  # cajas
lambda_llegada = 5  # llegada de clientes por hora
lambda_despacho = 8  # rate de servicio por hora
tiempo_simulacion = 24  # horas

class Cliente:
    def __init__(self, id, tiempo_llegada):
        self.id = id
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_salida = 0

def llegada_cliente(env, cajas, tiempos_espera):
    cliente_id = 0
    while True:
        yield env.timeout(random.expovariate(lambda_llegada))
        cliente_id += 1
        cliente = Cliente(cliente_id, env.now)
        env.process(despacho_cliente(env, cliente, cajas, tiempos_espera))

def despacho_cliente(env, cliente, cajas, tiempos_espera):
    # Buscar la caja con menos clientes
    min_customers = float('inf')
    selected_caja = None

    for caja_id, caja in enumerate(cajas):
        if len(caja.queue) < min_customers:
            min_customers = len(caja.queue)
            selected_caja = caja_id

    with cajas[selected_caja].request() as req:
        yield req
        tiempo_espera = env.now - cliente.tiempo_llegada
        tiempos_espera.append(tiempo_espera)
        yield env.timeout(random.expovariate(lambda_despacho))
        cliente.tiempo_salida = env.now

env = simpy.Environment()
cajas = [simpy.Resource(env) for _ in range(M)]
tiempos_espera = []
env.process(llegada_cliente(env, cajas, tiempos_espera))
env.run(until=tiempo_simulacion)
tiempo_promedio_cola = sum(tiempos_espera) / len(tiempos_espera)
clientes_en_cola_promedio = sum(len(caja.queue) for caja in cajas) / len(cajas)
utilizacion_cajeros = [(caja.count / (env.now * lambda_despacho)) for caja in cajas]
print("Resultados:")
print("1. Tiempo promedio de un cliente en la cola:", tiempo_promedio_cola)
print("2. Número de clientes en la cola en promedio:", clientes_en_cola_promedio)
print("3. Grado o factor de utilización de cada cajero:")
for i, utilizacion in enumerate(utilizacion_cajeros):
    print(f"   Cajero {i}: {utilizacion * 100:.2f}%")
