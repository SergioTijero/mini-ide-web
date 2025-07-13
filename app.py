"""
app.py
Servidor Flask para el Mini-IDE de Análisis Léxico y Sintáctico
"""
from flask import Flask, render_template, request, jsonify
from lexer import lexer
from parser import parser

app = Flask(__name__)

@app.route('/')
def index():
    # Renderiza la plantilla principal
    return render_template('index.html')

@app.route('/api/lex', methods=['POST'])
def api_lex():
    """
    API para análisis léxico.
    Recibe JSON con 'code' y devuelve lista de tokens.
    """
    code = request.json.get('code', '')
    try:
        lexer.input(code)
        tokens = []
        while True:
            t = lexer.token()
            if not t:
                break
            tokens.append({
                'type': t.type,
                'value': t.value,
                'lineno': t.lineno,
                'lexpos': t.lexpos
            })
        return jsonify(tokens)
    except Exception as e:
        # En caso de error léxico, devuelve mensaje y status 400
        return jsonify({'error': str(e)}), 400

def node_to_dict(node):
    """
    Convierte nodos del AST en diccionarios recursivamente.
    """
    return {
        'type': node.type,
        'value': node.value,
        'children': [node_to_dict(c) for c in getattr(node, 'children', [])]
    }

@app.route('/api/parse', methods=['POST'])
def api_parse():
    """
    API para análisis sintáctico.
    Devuelve el AST o un error.
    """
    code = request.json.get('code', '')
    try:
        ast = parser.parse(code, lexer=lexer)
        return jsonify(node_to_dict(ast))
    except Exception as e:
        # En caso de error, devuelve mensaje y status 400
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Ejecuta la app en modo debug en puerto 5001
    app.run(debug=True, port=5001)
