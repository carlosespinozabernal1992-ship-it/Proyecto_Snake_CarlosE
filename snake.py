import os
import time

# ==========================================
# 1. EL MODELO (Variables y Reglas Lógicas)
# ==========================================
class JuegoModelo:
    def __init__(self):
        self.puntos = 0
        self.game_over = False
        self.snake_x = 1         # Posición inicial en la cuadrícula
        self.limite_pantalla = 20 # Borde derecho del mapa

    def actualizar_logica(self):
        # Movimiento automático (Raptor: SnakeX <- SnakeX + 1)
        self.snake_x += 1
        
        # Condición de pérdida (Raptor: SnakeX > 20)
        if self.snake_x > self.limite_pantalla:
            self.game_over = True

# ==========================================
# 2. LA VISTA (Diseño por Consola)
# ==========================================
class JuegoVista:
    def dibujar_elementos(self, modelo):
        # Limpia la pantalla para refrescar la animación (Windows: cls, Mac/Linux: clear)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=== AVANCE PROYECTO SNAKE (MVC) ===")
        print(f"Puntos: {modelo.puntos} | Posición X: {modelo.snake_x}/{modelo.limite_pantalla}")
        print("-" * (modelo.limite_pantalla + 2))
        
        # Dibuja el mapa y la serpiente representada por un carácter '[O]'
        if not modelo.game_over:
            espacios = " " * (modelo.snake_x - 1)
            print(f"|{espacios}[O]" + " " * (modelo.limite_pantalla - modelo.snake_x) + "|")
        else:
            print("|" + " " * modelo.limite_pantalla + "|")
            
        print("-" * (modelo.limite_pantalla + 2))
        
        if modelo.game_over:
            print("\n¡COLISIÓN DETECTADA! Fin del juego (GameOver = True).")

# ==========================================
# 3. EL CONTROLADOR (El Loop Principal)
# ==========================================
class JuegoControlador:
    def __init__(self):
        self.modelo = JuegoModelo()
        self.vista = JuegoVista()

    def ejecutar_juego(self):
        # El ciclo principal (Raptor: Loop)
        while not self.modelo.game_over:
            self.modelo.actualizar_logica()
            self.vista.dibujar_elementos(self.modelo)
            
            # Delay: Pausa de 0.3 segundos por cada ciclo (Raptor: Delay)
            time.sleep(0.3)

# Arranque del juego independiente de librerías externas
if __name__ == "__main__":
    juego = JuegoControlador()
    juego.ejecutar_juego()
    