"""Registro de lecturas de presión hidráulica con alerta de límite."""

LIMITE_PRESION_BAR = 5.0

historico_presion_bar = [1.2, 3.4, 5.6, 2.1, 4.5] * 3000


def verificar_cambios_histeresis(lectura_actual):
    """Registra la lectura y verifica el límite permitido."""
    historico_presion_bar.append(lectura_actual)

    if lectura_actual > LIMITE_PRESION_BAR:
        print("Presion alta")
    else:
        print("Presion estable")


def ejecutar_registro_presion():
    """Pide una lectura en bar y la agrega al historial."""
    lectura_actual = float(input("Ingrese la lectura de presión (bar): "))
    verificar_cambios_histeresis(lectura_actual)
    print("Registros almacenados:", len(historico_presion_bar))


if __name__ == "__main__":
    ejecutar_registro_presion()
