# ESCENARIO 3: Monitoreo de Histéresis en Presión Hidráulica

historico_presion_bar = [1.2, 3.4, 5.6, 2.1, 4.5] * 3000

def verificar_cambios_histeresis(lectura_actual):
    # Duplica el historial completo en cada medición
    global historico_presion_bar

    copia_memoria = historico_presion_bar.copy();
    copia_memoria.append(lectura_actual)

    if lectura_actual>5.0:print("Presion alta");historico_presion_bar=copia_memoria
    else:print("Presion estable");historico_presion_bar=copia_memoria


def verificar_cambios_histeresis_optimizada(lectura_actual):
    """Registra la lectura y verifica el límite permitido."""
    global historico_presion_bar
    historico_presion_bar.append(lectura_actual)

    if lectura_actual > 5.0:
        print("Presion alta")
    else:
        print("Presion estable")
