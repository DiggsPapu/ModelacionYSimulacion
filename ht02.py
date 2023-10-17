import simpy
import random

# Parámetros de la simulación
M = 1  # Número de cajas
LAMBDA_LLEGADA = 20  # Tasa de llegada de clientes por hora
LAMBDA_DESPACHO = 40  # Tasa de servicio (despacho) por hora
TIEMPO_SIMULACION = 24  # Duración de la simulación en horas
tiempos_ocupados_cajeros = [0 for _ in range(M)]

class Cliente:
    def __init__(self, id, tiempo_llegada):
        self.id = id  
        self.tiempo_llegada = tiempo_llegada  
        self.tiempo_salida = 0  
        

def llegada_cliente(env, cajas, tiempos_espera):
    cliente_id = 0
    while True:
        yield env.timeout(random.expovariate(LAMBDA_LLEGADA))
        
        cliente_id += 1
        cliente = Cliente(cliente_id, env.now) 
        
        env.process(despacho_cliente(env, cliente, cajas, tiempos_espera))


def despacho_cliente(env, cliente, cajas, tiempos_espera):

    min_customers = min(len(caja.queue) for caja in cajas)

    min_cajas = [caja_id for caja_id, caja in enumerate(cajas) if len(caja.queue) == min_customers]

    selected_caja = random.choice(min_cajas)

    with cajas[selected_caja].request() as req:
        yield req  # Espera hasta que el recurso esté disponible
        

        inicio_servicio = env.now  
        tiempo_espera = inicio_servicio - cliente.tiempo_llegada
        tiempos_espera.append(tiempo_espera)  # Agrega el tiempo de espera a la lista
        yield env.timeout(random.expovariate(LAMBDA_DESPACHO))
        fin_servicio = env.now  
        tiempos_ocupados_cajeros[selected_caja] += (fin_servicio - inicio_servicio)  
        
        cliente.tiempo_salida = env.now

def main():
    env = simpy.Environment()
    cajas = [simpy.Resource(env) for _ in range(M)]
    tiempos_espera = []

    env.process(llegada_cliente(env, cajas, tiempos_espera))

    env.run(until=TIEMPO_SIMULACION)

    tiempo_promedio_cola = sum(tiempos_espera) / len(tiempos_espera)  # Tiempo promedio en cola
    clientes_en_cola_promedio = sum(len(caja.queue) for caja in cajas) / len(cajas)  # Promedio de clientes en cola
    utilizacion_cajeros = [tiempo_ocupado / TIEMPO_SIMULACION for tiempo_ocupado in tiempos_ocupados_cajeros]

    print("Resultados:")
    print("1. Tiempo promedio de un cliente en la cola:", tiempo_promedio_cola)
    print("2. Número de clientes en la cola en promedio:", clientes_en_cola_promedio)
    print("3. Grado o factor de utilización de cada cajero:")
    for i, utilizacion in enumerate(utilizacion_cajeros):
        print(f"   Cajero {i}: {utilizacion * 100:.2f}%")


if __name__ == "__main__":
    main()