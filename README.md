
# Mini-IDE Web de Análisis Léxico y Sintáctico

Mini-IDE web interactivo para analizar expresiones matemáticas usando **Flask** y **PLY**. Permite realizar análisis léxico y sintáctico desde el navegador, mostrando los tokens y el árbol de sintaxis abstracta (AST) en tiempo real, con una interfaz inspirada en Windows 95.

## Características
- **Análisis léxico:** Extrae y muestra los tokens del código fuente usando PLY.
- **Análisis sintáctico:** Genera y visualiza el AST en formato JSON.
- **Interfaz web:** Editor de código con CodeMirror y diseño retro.
- **API REST:** Endpoints `/api/lex` y `/api/parse` para integración y pruebas.

## Estructura del proyecto
- `app.py`: Servidor Flask y endpoints API.
- `lexer.py`: Definición de tokens y reglas léxicas (PLY).
- `parser.py`: Gramática y construcción del AST (PLY).
- `templates/index.html`: Interfaz principal con editor y botones.
- `static/main.js`: Lógica JS para interactuar con la API y mostrar resultados.
- `static/win95.css`: Estilos visuales tipo Windows 95.
- `requirements.txt`: Dependencias necesarias.

## Instalación y uso
1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta el servidor:
   ```bash
   python app.py
   ```
3. Abre [http://127.0.0.1:5001/](http://127.0.0.1:5001/) en tu navegador.

## Ejemplo de uso
Escribe una expresión como:
```
3 + 4 * (2 - 1)
```
y presiona los botones para ver los tokens y el AST generado.

## APIs disponibles
- `POST /api/lex`: Recibe `{ code: "..." }` y devuelve lista de tokens.
- `POST /api/parse`: Recibe `{ code: "..." }` y devuelve el AST o error.

## Créditos
Desarrollado por Sergio Tijero. Basado en PLY y Flask.
