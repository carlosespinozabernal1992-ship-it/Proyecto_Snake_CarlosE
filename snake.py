import os
import time
import msvcrt
import random

# Variables globales de control
estado = "MENU"
high_score = 0
score = 0
nivel = 1
velocidad = 0.13  # 130 milisegundos expresados en segundos para Python

# Coordenadas iniciales
snake_x = 10
snake_y = 10
dx = 1
dy = 0

comida_x = 5
comida_y = 12

def mostrar_menu():
    global estado, score, nivel, velocidad, snake_x, snake_y, dx, dy, comida_x, comida_y
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=================================")
    print("        SNAKE GAME PYTHON        ")
    print("=================================")
    print(f" Record Actual: {high_score} pts")
    print("=================================")
    print()
    opcion = input("¿Desea iniciar el juego? (S/N): ").strip().upper()
    
    if opcion == "S":
        estado = "PLAYING"
        score = 0
        nivel = 1
        velocidad = 0.13
        snake_x = 10
        snake_y = 10
        dx = 1
        dy = 0
        comida_x = 5
        comida_y = 12
    else:
        estado = "EXIT"

def motor_juego():
    global estado, score, high_score, nivel, velocidad, snake_x, snake_y, dx, dy, comida_x, comida_y
    
    # Captura de teclado no bloqueante en Windows
    if msvcrt.kbhit():
        tecla = msvcrt.getch().decode('utf-8', errors='ignore').upper()
        if tecla == 'A': dx = -1; dy = 0
        elif tecla == 'W': dx = 0; dy = -1
        elif tecla == 'D': dx = 1; dy = 0
        elif tecla == 'S': dx = 0; dy = 1

    # Actualizar posiciones
    snake_x += dx
    snake_y += dy

    # Rombo de colisión con bordes (Matriz 1 a 20)
    if snake_x < 1 or snake_x > 20 or snake_y < 1 or snake_y > 20:
        if score > high_score:
            high_score = score
        estado = "GAMEOVER"
        return

    # Rombo de colisión con la comida
    if snake_x == comida_x and snake_y == comida_y:
        score += 10
        comida_x = random.randint(2, 19)
        comida_y = random.randint(2, 19)
        
        # Aumento de dificultad cada 50 puntos
        if score % 50 == 0:
            nivel += 1
            velocidad = max(0.03, velocidad - 0.015)

    # Renderizado en consola
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"[Nivel: {nivel}] | [Puntaje: {score}] | Posición: ({snake_x},{snake_y})")
    print(f"Ubicación Objetivo: ({comida_x},{comida_y})")
    print("-" * 50)
    
    time.sleep(velocidad)

def mostrar_game_over():
    global estado
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=================================")
    print("           GAME OVER             ")
    print("=================================")
    print(f" Puntuación Obtenida: {score} pts")
    print(f" Record Invencible:  {high_score} pts")
    print("=================================")
    print("\nPresione cualquier tecla para retornar al menú...")
    msvcrt.getch()
    estado = "MENU"

# Bucle principal
while estado != "EXIT":
    if estado == "MENU":
        mostrar_menu()
    elif estado == "PLAYING":
        motor_juego()
    elif estado == "GAMEOVER":
        mostrar_game_over()

print("Ejecución finalizada con éxito.")
