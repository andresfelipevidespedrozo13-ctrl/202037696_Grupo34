# ESCENARIO 5
# Gestión de Voltaje en Banco de Baterías de Nodo UNAD
# Sensor INA219

voltios = float(
    input("Ingrese el voltaje inicial del banco de baterías: ")
)

chequeo_baterias = True
lectura = 0
max_lecturas = 20

while chequeo_baterias and lectura < max_lecturas:

    lectura += 1

    print("\nLectura:", lectura)
    print("Voltaje actual:", round(voltios, 2), "V")

    if voltios > 30:
        print(
            "PELIGRO: Sobretensión extrema. "
            "Fusible abierto."
        )
        chequeo_baterias = False

    elif voltios < 21:
        print(
            "Protección: Desconexión de carga "
            "por descarga"
        )
        voltios += 1.0

    elif voltios >= 21 and voltios <= 27.5:
        print(
            "Protección: Sistema operativo "
            "en flotación"
        )
        voltios += 0.2

    else:
        print(
            "Protección: Disipador térmico "
            "activado"
        )
        voltios -= 1.5

print("\nFin del monitoreo del banco de baterías.")
