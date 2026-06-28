 # PROYECTO INTEGRADOR: JUEGO SNAKE
## El impacto de las nuevas tecnologías en la sociedad: desarrollo y proyección de soluciones informáticas

## 👤 Información del Proyecto
* **Asignatura:** LOGICA DE PROGRAMACION 1-CIB-1A
* **Integrante:** Carlos Alberto Espinoza Bernal
* **Fecha:** Junio 2026

---

## 🎯 Objetivo del Sistema
Desarrollar un entorno de simulación algorítmica y control de flujos basado en el modelo clásico del **Juego Snake** empleando el lenguaje Python. El sistema tiene como propósito técnico evaluar el manejo de estructuras de control repetitivas, la optimización en la captura de eventos de hardware en tiempo real (teclado) y la gestión de lógica matricial en entornos de consola, sirviendo como base práctica para comprender la abstracción de problemas complejos en soluciones informáticas seguras y estructuradas.

---

## 💻 Descripción de Funcionalidades (Juego Snake)
El sistema integra de manera síncrona el control de hilos de ejecución mediante pausas de reloj y eventos periféricos, dividiéndose en los siguientes componentes modulares:

1. **Motor de Menú Interactivo (`mostrar_menu`):** Interfaz inicial basada en texto que administra el estado global de la aplicación, permitiendo al usuario iniciar ciclos del juego Snake, configurar parámetros o realizar una salida limpia del sistema (`EXIT`), previniendo bucles infinitos o cuelgues de memoria.
2. **Ciclo de Ejecución Principal (Game Loop de Snake):** Administra de forma secuencial la actualización de posiciones espaciales de la serpiente, la verificación de colisiones y el refresco visual de la pantalla a una tasa controlada de 0.3 segundos por ciclo.
3. **Control Dinámico de Movimiento Automatizado:** Sistema lógico que altera las coordenadas cartesianas del elemento principal en el eje X, actualizando los vectores de posición de la serpiente en cada ciclo de reloj.
4. **Captura no Bloqueante de Periféricos (`msvcrt.getch`):** Implementación de bajo nivel para la lectura de interrupciones del teclado, permitiendo la interactividad del usuario para dirigir la serpiente sin congelar la ejecución del renderizado de la consola.
5. **Algoritmo de Detección de Colisiones y Límites:** Función analítica que calcula si las variables de posición de la serpiente exceden los umbrales de la frontera espacial configurada (límite de pantalla). Al detectarse una violación de fronteras, el software realiza una conmutación segura del estado global hacia `game_over = True`, desplegando la pantalla de fin de juego y preservando el registro de la puntuación de la sesión.

---

## 🛠️ Herramientas de Desarrollo y Control de Versiones
* **Lenguaje:** Python 3.x
* **Librerías nativas:** `os`, `time`, `msvcrt`
* **Entorno de Desarrollo:** Visual Studio Code
* **Control de Versiones:** Git & GitHub (Garantizando la trazabilidad del código, la gestión de ramas y el despliegue seguro del repositorio).
