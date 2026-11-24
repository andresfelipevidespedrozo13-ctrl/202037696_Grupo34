# 202037696_Grupo34

Tarea 5 del curso Lenguajes Interpretados (202037696), Grupo 34.

El repositorio reúne en un solo sistema los módulos de las tareas 2, 3 y 4.

## Módulos

- control_voltaje_baterias.py: protección del banco de baterías (sensor INA219).
- registros_mppt_phocos.py: mapa de registros del controlador Phocos MPPT y consulta con get().
- historial_presion_hidraulica.py: registro de lecturas de presión con alerta sobre 5,0 bar.
- main.py: menú que llama a los tres módulos.

## Ejecución

    python main.py

Todo el código sigue PEP 8: 4 espacios, nombres en snake_case y líneas de máximo 79 caracteres.
