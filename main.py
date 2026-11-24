"""Menú principal del sistema integrado del Grupo 34."""

from control_voltaje_baterias import ejecutar_control_voltaje
from historial_presion_hidraulica import ejecutar_registro_presion
from registros_mppt_phocos import ejecutar_consulta_registros

OPCIONES_MENU = {
    "1": ("Control de voltaje del banco de baterías",
          ejecutar_control_voltaje),
    "2": ("Consulta de registros del controlador MPPT",
          ejecutar_consulta_registros),
    "3": ("Registro de presión hidráulica",
          ejecutar_registro_presion),
}


def mostrar_menu():
    """Imprime las opciones disponibles para el operario."""
    print("\nSISTEMA DE MONITOREO - GRUPO 34")
    for clave, (descripcion, _) in OPCIONES_MENU.items():
        print(f"{clave}. {descripcion}")
    print("0. Salir")


def main():
    """Repite el menú hasta que el operario elija salir."""
    opcion = ""
    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        seleccion = OPCIONES_MENU.get(opcion)

        if seleccion is not None:
            seleccion[1]()
        elif opcion != "0":
            print("Opción no válida.")


if __name__ == "__main__":
    main()
