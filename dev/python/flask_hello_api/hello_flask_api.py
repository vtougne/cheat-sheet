from flask import Flask, request, jsonify

app = Flask(__name__)

# ------------------------------------------------------------------
# Route GET : /hello
# ------------------------------------------------------------------
@app.route('/hello', methods=['GET'])
def hello():
    """Retourne un message de bienvenue."""
    return jsonify({
        'message': 'Bonjour depuis l\'API Flask !',
        'status': 'success'
    }), 200

# ------------------------------------------------------------------
# Route GET : /coucou
# ------------------------------------------------------------------
@app.route('/coucou', methods=['GET'])
def coucou():
    """Retourne un message de bienvenue en français."""
    return jsonify({
        'message': 'Coucou depuis l\'API Flask !',
        'status': 'success'
    }), 200

# ------------------------------------------------------------------

# ------------------------------------------------------------------
@app.route('/echo', methods=['POST'])
def echo():
    """
    Renvoie le JSON reçu dans la requête.
    Si le corps n’est pas du JSON, renvoie une erreur 400.
    """
    if not request.is_json:
        return jsonify({
            'error': 'Le corps de la requête doit être du JSON',
            'status': 'error'
        }), 400

    data = request.get_json()
    return jsonify({
        'received': data,
        'status': 'success'
    }), 200

# ------------------------------------------------------------------
# Point d’entrée
# ------------------------------------------------------------------
if __name__ == '__main__':
    # Exécute le serveur en mode debug (développement uniquement)
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
