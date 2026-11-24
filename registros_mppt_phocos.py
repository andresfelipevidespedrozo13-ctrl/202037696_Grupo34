# Tarea 3 - Lenguajes Interpretados
# Escenario 5: Controlador solar Phocos MPPT

mppt_phocos = {
    "0x10": {
        "hardware_source": "PV_ARRAY",
        "max_safe_value": 150.0,
        "system_flag": True
    },
    "0x11": {
        "hardware_source": "BATTERY",
        "max_safe_value": 60.0,
        "system_flag": True
    },
    "0x15": {
        "hardware_source": "LOAD_RELAY",
        "max_safe_value": 20.0,
        "system_flag": False
    }
}

MAX_BUSQUEDAS = 5

print("CONSULTA DE REGISTROS - PHOCOS MPPT")
print("Direcciones disponibles: 0x10, 0x11, 0x15")
print("También puede consultar: PV_ARRAY, BATTERY, LOAD_RELAY")

for intento in range(MAX_BUSQUEDAS):
    consulta = input(
        f"\nConsulta {intento + 1}/{MAX_BUSQUEDAS} "
        "(o escriba salir): "
    ).strip()

    if consulta.lower() == "salir":
        print("Consulta finalizada por el usuario.")
        break

    # Primero se intenta buscar por dirección.
    registro = mppt_phocos.get(consulta)

    # Si no existe la dirección, se busca por origen.
    if registro is None:
        registro_encontrado = None
        direccion_encontrada = None

        for direccion, datos in mppt_phocos.items():
            if datos.get("hardware_source", "").lower() == consulta.lower():
                registro_encontrado = datos
                direccion_encontrada = direccion
                break

        registro = registro_encontrado
    else:
        direccion_encontrada = consulta

    if registro is not None:
        print("\nRegistro encontrado")
        print("Dirección:", direccion_encontrada)
        print("Origen:", registro.get("hardware_source", "No definido"))
        print("Límite seguro:", registro.get("max_safe_value", "No definido"))
        print("Bandera del sistema:", registro.get("system_flag", "No definida"))
    else:
        print("Consulta no válida: no se encontró el registro.")
else:
    print("\nSe alcanzó el máximo de búsquedas permitido.")
