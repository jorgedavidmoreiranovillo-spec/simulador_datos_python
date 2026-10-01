import time
import random

from rich.console import Console
from rich.panel import Panel
from rich.live import Live

console = Console()

# constantes, caras de los dados

DADO_D4 = 4
DADO_D6 = 6
DADO_D8 = 8
DADO_D10 = 10
DADO_D12 = 12
DADO_D20 = 20

#bucle principal
while True:
    #titulo del programa coloreado de amarillo
    print("\n[yellow]Simulador de Dados[/yellow]")
    #menu de opciones
    print("1. Lanzar los dados ")
    print("2. Ver estadisticas (proximamente)")
    print("3. Salir")
    #control de excepciones para el menu
    try:
        opcion = int(input("\nElige una opcion: "))
    except ValueError:
        #mensaje de error un rojo
        print("[bold red]Opcion no valida. Por favor, introduce un numero.[/bold red]")
        continue #salto al inicio del bucle si algo falla
    