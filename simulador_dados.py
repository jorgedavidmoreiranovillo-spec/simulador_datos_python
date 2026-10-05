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
    
    #limite de caras del dado
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
    
    #validacion de los dados
    cantidad_dados = 0 
    while True:
        try: #se va a entrar en este bucle para que el programa nos haga lanzar al menos un dado
            cantidad_dados = int(input("¿cuantos dados vas a lanzar?"))
            if cantidad_dados <=0:
                console.print("[italic orange]debe haber al menos 1 dado [\italic orange]")
                continue
            break #si la entrada es correcta se sale del bucle para validar que hemos puesto al menos un dado
        except ValueError:
            console.print("[bold red]introduce un numero valido (que sea entero positivo)[\bold red]")
    
    #efecto para que se vea la animacion de los numeros pasar con el Live
    console.print("[italic bold]LANZANDO DADOS...[\italic bold]")
    # with Live muestra y actualiza un panel en la terminal mientras dura este bloque
    with Live(Panel("dando vueltas...", title="simulacion"), refresh_per_second=10) as live: #
        bucle_animacion = 0 
        while bucle_animacion < 12: #asi cambia de valor 12 veces  
            valor_temporal = random.randint(1, caras_dado)
            live.update(Panel("[italic bold]GIRANDO DADOS...[\italic bold]"))
            time.sleep(0.1)  # pausa de 0,1 segundos para que la animacion se pueda ver
            bucle_animacion += 1
            
    #lazamiento de los dados logico
    suma_total=0
    texto_resultados = "" #acumulador de texto
    
    contador= 1
    while contador <= cantidad_dados:
        tirada = random.randint(1, caras_dado)
        suma_total += tirada #acumular numero
        
    #asignacion de color segun el valor, verde es maximo, rojo es 1, amarillo es el resto
    if tirada == caras_dado:
        color = "bold green"
    elif tirada == 1:
        color = "bold red"
    else:
        color = "bold yellow"
    #se le asigna el color a cada tirada segun lo que salga
    texto_resultados += f"dado {contador}: [{color}]{tirada}[/{color}]\n"
    contador += 1
    
