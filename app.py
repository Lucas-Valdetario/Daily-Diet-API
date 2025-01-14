from flask import Flask, request, jsonify
from models.snack import Snack, db  # Importando o modelo e db

app = Flask(__name__)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snacks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco de dados
db.init_app(app)

# Endpoints
@app.route('/snacks', methods=['POST'])
def create_snack():
    data = request.get_json()

    # Validação
    if not data or "title" not in data or "date" not in data:
        return jsonify({"message": "Dados inválidos. Certifique-se de incluir 'title' e 'date'."}), 400

    new_snack = Snack(
        title=data["title"],
        description=data.get("description", ""),
        diet=data.get("diet", False),
        date=data["date"]
    )
    db.session.add(new_snack)
    db.session.commit()

    return jsonify({"message": "Nova refeição criada com sucesso", "snack": new_snack.to_dict()}), 201

@app.route('/snacks', methods=['GET'])
def get_snacks():
    snacks = Snack.query.all()
    snack_list = [snack.to_dict() for snack in snacks]

    return jsonify({"snacks": snack_list, "total_snacks": len(snack_list)})

@app.route('/snacks/<int:id>', methods=['GET'])
def get_snack(id):
    snack = Snack.query.get(id)
    if not snack:
        return jsonify({"message": "Não foi possível encontrar essa refeição"}), 404

    return jsonify(snack.to_dict())

@app.route('/snacks/<int:id>', methods=['PUT'])
def update_snack(id):
    data = request.get_json()
    snack = Snack.query.get(id)

    if not snack:
        return jsonify({"message": "Não foi possível encontrar essa refeição"}), 404

    snack.title = data.get("title", snack.title)
    snack.description = data.get("description", snack.description)
    snack.diet = data.get("diet", snack.diet)
    snack.date = data.get("date", snack.date)

    db.session.commit()

    return jsonify({"message": "Refeição atualizada com sucesso", "snack": snack.to_dict()})

@app.route('/snacks/<int:id>', methods=['DELETE'])
def delete_snack(id):
    snack = Snack.query.get(id)

    if not snack:
        return jsonify({"message": "Não foi possível encontrar essa refeição"}), 404

    db.session.delete(snack)
    db.session.commit()

    return jsonify({"message": "Refeição deletada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)
