"""Control de voltaje del banco de baterías (sensor INA219)."""

VOLTAJE_CRITICO = 30.0
VOLTAJE_MINIMO = 21.0
VOLTAJE_FLOTACION = 27.5
MAX_LECTURAS = 20


def monitorear_banco_baterias(voltios):
    """Simula las lecturas del banco y aplica la protección."""
    chequeo_baterias = True
    lectura = 0

    while chequeo_baterias and lectura < MAX_LECTURAS:
        lectura += 1
        print("\nLectura:", lectura)
        print("Voltaje actual:", round(voltios, 2), "V")

        if voltios > VOLTAJE_CRITICO:
            print("PELIGRO: Sobretensión extrema. Fusible abierto.")
            chequeo_baterias = False
        elif voltios < VOLTAJE_MINIMO:
            print("Protección: Desconexión de carga por descarga")
            voltios += 1.0
        elif voltios <= VOLTAJE_FLOTACION:
            print("Protección: Sistema operativo en flotación")
            voltios += 0.2
        else:
            print("Protección: Disipador térmico activado")
            voltios -= 1.5

    print("\nFin del monitoreo del banco de baterías.")


def ejecutar_control_voltaje():
    """Pide el voltaje inicial y lanza el monitoreo."""
    voltios = float(
        input("Ingrese el voltaje inicial del banco de baterías: ")
    )
    monitorear_banco_baterias(voltios)


if __name__ == "__main__":
    ejecutar_control_voltaje()
