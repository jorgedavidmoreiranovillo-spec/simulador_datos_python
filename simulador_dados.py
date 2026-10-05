import time
import random

from rich.console import Console
from rich.live import Live
from rich.panel import Panel

console = Console()

# constantes, caras de los dados
DADO_D4 = 4
DADO_D6 = 6
DADO_D8 = 8
DADO_D10 = 10
DADO_D12 = 12
DADO_D20 = 20

# bucle principal
while True:
    # titulo del programa coloreado de amarillo
    console.print("\n[yellow]Simulador de Dados[/yellow]")
    # menu de opciones
    console.print("1. Lanzar los dados")
    console.print("2. Ver estadísticas (próximamente)")
    console.print("3. Salir")

    # control de excepciones para el menu
    try:
        opcion_menu = int(input("\nElige una opción: "))
    except ValueError:
        # mensaje de error en rojo
        console.print("[bold red]Opción no válida. Por favor, introduce un número.[/bold red]")
        continue

    # seleccion de las opciones
    if opcion_menu == 3:
        console.print("\n[bold green]Saliendo del programa...[/bold green]")
        break
    elif opcion_menu == 2:
        console.print("\n[dim italic]Esta opción todavía no funciona.[/dim italic]")
        continue
    elif opcion_menu != 1:
        console.print("[bold red]Opción no válida.[/bold red]")
        continue

    # seleccion del tipo de dado
    console.print("\n[bold orange]---Tipos de dados---[/bold orange]")
    console.print("1. D4  (4 caras)")
    console.print("2. D6  (6 caras)")
    console.print("3. D8  (8 caras)")
    console.print("4. D10 (10 caras)")
    console.print("5. D12 (12 caras)")
    console.print("6. D20 (20 caras)")

    try:
        opcion_dado = int(input("Selecciona el tipo de dado (1-6): "))
    except ValueError:
        console.print("[bold red]Error: Entrada no numérica.[/bold red]")
        continue

    caras_dado = 0
    if opcion_dado == 1:
        caras_dado = DADO_D4
    elif opcion_dado == 2:
        caras_dado = DADO_D6
    elif opcion_dado == 3:
        caras_dado = DADO_D8
    elif opcion_dado == 4:
        caras_dado = DADO_D10
    elif opcion_dado == 5:
        caras_dado = DADO_D12
    elif opcion_dado == 6:
        caras_dado = DADO_D20
    else:
        console.print("[bold red]Tipo de dado no válido.[/bold red]")
        continue

    cantidad_dados = 0
    while True:
        try:
            cantidad_dados = int(input("¿Cuántos dados vas a lanzar? "))
            if cantidad_dados <= 0:
                console.print("[italic orange]Debe haber al menos 1 dado.[/italic orange]")
                continue
            break
        except ValueError:
            console.print("[bold red]Introduce un número válido (entero positivo).[/bold red]")

    console.print("[italic bold]LANZANDO DADOS...[/italic bold]")
    with Live(Panel("Dando vueltas...", title="Simulación"), refresh_per_second=10) as live:
        for _ in range(12):
            live.update(Panel("[italic bold]GIRANDO DADOS...[/italic bold]"))
            time.sleep(0.1)

    suma_total = 0
    texto_resultados = ""

    for contador in range(1, cantidad_dados + 1):
        tirada = random.randint(1, caras_dado)
        suma_total += tirada

        if tirada == caras_dado:
            color = "bold green"
        elif tirada == 1:
            color = "bold red"
        else:
            color = "bold yellow"

        texto_resultados += f"dado {contador}: [{color}]{tirada}[/{color}]\n"

    promedio = suma_total / cantidad_dados if cantidad_dados else 0

    salida = (
        f"{texto_resultados}\n"
        f"\n[bold white]Suma total: [/bold white] [sky blue]{suma_total}[/sky blue]\n"
        f"[bold white]Promedio:[/bold white] [purple]{promedio:.2f}[/purple]"
    )
    console.print(Panel(salida,title=f"[bold italic cyan]Resultados tirada (D{caras_dado})[/bold italic cyan]",expand=False))

