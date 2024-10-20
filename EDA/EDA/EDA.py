# Manejador de eventos
class EventManager:
    def __init__(self):
        self.listeners = {}  # Diccionario de eventos y sus suscriptores

    def suscribir(self, evento, listener):
        if evento not in self.listeners:
            self.listeners[evento] = []
        self.listeners[evento].append(listener)

    def emitir(self, evento, data=None):
        if evento in self.listeners:
            for listener in self.listeners[evento]:
                listener(data)

# Componentes que escuchan los eventos
class Cocina:
    def preparar_pedido(self, data):
        print(f"[Cocina] Preparando pedido de {data['cliente']}: {data['platos']}")

class CajaRegistradora:
    def procesar_pago(self, data):
        print(f"[Caja] Procesando pago de {data['cliente']} por un total de ${data['total']}")

# Sistema de Pedidos
class SistemaPedidos:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def nuevo_pedido(self, cliente, platos):
        print(f"[Sistema] Recibiendo pedido de {cliente}")
        # Emitir evento de nuevo pedido
        self.event_manager.emitir("nuevo_pedido", {"cliente": cliente, "platos": platos})

    def realizar_pago(self, cliente, total):
        print(f"[Sistema] Recibiendo pago de {cliente}")
        # Emitir evento de pago
        self.event_manager.emitir("pago_realizado", {"cliente": cliente, "total": total})

# Crear el manejador de eventos
event_manager = EventManager()

# Crear los componentes que escucharan los eventos
cocina = Cocina()
caja = CajaRegistradora()

# Suscribir los componentes a los eventos
event_manager.suscribir("nuevo_pedido", cocina.preparar_pedido)
event_manager.suscribir("pago_realizado", caja.procesar_pago)

# Crear el sistema de pedidos
sistema_pedidos = SistemaPedidos(event_manager)

# Funcion para interactuar con el usuario
def iniciar_sistema():
    while True:
        print("\n--- Menu de Opciones ---")
        print("1. Hacer un nuevo pedido")
        print("2. Realizar un pago")
        print("3. Salir")
        
        opcion = input("Selecciona una opcion (1/2/3): ")

        if opcion == "1":
            # Tomar los datos del pedido
            cliente = input("Ingresa el nombre del cliente: ")
            platos = input("Ingresa los platos pedidos (separados por comas): ").split(", ")
            # Procesar nuevo pedido
            sistema_pedidos.nuevo_pedido(cliente, platos)
        
        elif opcion == "2":
            # Tomar los datos del pago
            cliente = input("Ingresa el nombre del cliente: ")
            total = float(input("Ingresa el total a pagar: "))
            # Procesar pago
            sistema_pedidos.realizar_pago(cliente, total)

        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opcion no valida. Intenta de nuevo.")

# Iniciar el sistema interactivo
iniciar_sistema()
