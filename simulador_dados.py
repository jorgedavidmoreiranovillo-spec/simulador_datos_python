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
        opcion_menu = int(input("\nElige una opcion: "))
    except ValueError:
        #mensaje de error un rojo
        print("[bold red]Opcion no valida. Por favor, introduce un numero.[/bold red]")
        continue #salto al inicio del bucle si algo falla
    #seleccion de las opciones
    if opcion_menu == 3:
        console.print("\n[bold green]saliendo del programa...[/bold green]")
        break
    elif opcion_menu == 2:
        console.print("\n[dim italic]Esta opcion todavia no funciona.[/dim italic]")
        pass #se usa pass para futuras modificaciones
        continue
    elif opcion_menu != 1:
        console.print("[bold red]Opcion no valida.[/bold red]")

    #seleccion del tipo de dado
    console.print("\n[bold orange]---Tipos de dados---[/bold orange]")
    console.print("1. D4  (4 caras)")
    console.print("2. D6  (6 caras)")
    console.print("3. D8  (8 caras)")
    console.print("4. D10 (10 caras)")
    console.print("5. D12 (12 caras)")
    console.print("6. D20 (20 caras)")
    
    