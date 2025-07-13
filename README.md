# Mini-IDE Web de Análisis Léxico y Sintáctico

## Descripción
Proyecto Flask que permite analizar código desde el navegador:
- Análisis léxico: Muestra tokens con PLY.
- Análisis sintáctico: Muestra AST como JSON.

## Estructura
- `app.py`: Servidor Flask.
- `lexer.py`: Definición de tokens con PLY.
- `parser.py`: Gramática y parser con PLY.
- `templates/index.html`: Interfaz de usuario.
- `static/main.js`: Lógica JS.

## Requisitos
- Python 3
- Paquetes: Flask, ply

```bash
pip install -r requirements.txt
python app.py
```

La app correrá en http://127.0.0.1:5000/.
