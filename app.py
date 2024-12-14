from flask import Flask, jsonify, request
from models.snack import Snack

app = Flask(__name__)


snacks = []                                      # Armazenamento das refeições
snack_id_control = 1                             # Identificador
@app.route('/snacks', methods=["POST"])
def create_snack():                               # Função Create
    global snack_id_control                      
    data = request.get_json()
    new_snack = Snack(id=snack_id_control, title=data.get("title"), description=data.get("description"), date=data.get("date"), diet=data.get("diet",False)) 
    snack_id_control += 1
    snacks.append(new_snack)
    print(snacks)
    return jsonify({"message":"Refeição adicionada com sucesso"})  

@app.route('/snacks', methods=['GET'])
def get_snacks():                            # Função para retornar todas as minhas atividades.
    snack_list = [snack.to_dict() for snack in snacks]      # Nessa parte o comando for vai me retornar tudo no comando to_dict para trazer em dicionário
        
    output = {
                "snacks": snack_list,
                "total_snacks": len(snack_list)
            }
    return jsonify(output)

@app.route('/snacks/<int:id>', methods=['GET']) # Função para retornar uma tarefa. # Parâmetro de rotas, convertendo "id" para int.
def get_snack(id):
    for s in snacks:
        if s.id == id:
            return jsonify(s.to_dict())
        
    return jsonify({"message": "Não foi possível encontrar a refeição"}), 404



if __name__ == "__main__":
    app.run(debug=True)
