"""Mapa de registros del controlador solar Phocos MPPT."""

MAX_BUSQUEDAS = 5

mppt_phocos = {
    "0x10": {
        "hardware_source": "PV_ARRAY",
        "max_safe_value": 150.0,
        "system_flag": True,
    },
    "0x11": {
        "hardware_source": "BATTERY",
        "max_safe_value": 60.0,
        "system_flag": True,
    },
    "0x15": {
        "hardware_source": "LOAD_RELAY",
        "max_safe_value": 20.0,
        "system_flag": False,
    },
}


def buscar_registro(consulta):
    """Busca por dirección y, si no existe, por origen de hardware."""
    registro = mppt_phocos.get(consulta)
    if registro is not None:
        return consulta, registro

    for direccion, datos in mppt_phocos.items():
        origen = datos.get("hardware_source", "")
        if origen.lower() == consulta.lower():
            return direccion, datos

    return None, None


def mostrar_registro(direccion, registro):
    """Imprime los tres campos del registro encontrado."""
    print("\nRegistro encontrado")
    print("Dirección:", direccion)
    print("Origen:", registro.get("hardware_source", "No definido"))
    print("Límite seguro:", registro.get("max_safe_value", "No definido"))
    print(
        "Bandera del sistema:",
        registro.get("system_flag", "No definida"),
    )


def ejecutar_consulta_registros():
    """Atiende hasta MAX_BUSQUEDAS consultas del operario."""
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

        direccion, registro = buscar_registro(consulta)
        if registro is not None:
            mostrar_registro(direccion, registro)
        else:
            print("Consulta no válida: no se encontró el registro.")
    else:
        print("\nSe alcanzó el máximo de búsquedas permitido.")


if __name__ == "__main__":
    ejecutar_consulta_registros()
