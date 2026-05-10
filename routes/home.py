from flask import Blueprint,render_template,jsonify,request
from supabase import create_client
from database.supabase_client import supabase
from datetime import datetime
import locale
import uuid

home_route = Blueprint('home', __name__)

#ROTAS DE TRANSIÇÃO WEB
@home_route.route('/')
def home():
    return render_template('index.html')




@home_route.route('/validar')
def valid():
    try:
        response = supabase.table("ger_rsv").select("id, data, qtd_disp, bloqueio").execute()

        if response.data:
            return jsonify(response.data)  # Retorna os dados diretamente
        
        return jsonify([])  # Retorna lista vazia se não houver dados
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Retorna erro HTTP 500 em caso de falha
    








@home_route.route('/reservar', methods=['POST'])
def reservar():

    try:

        dados = request.get_json()

        print("Dados recebidos:", dados)

        nome = dados.get('nome')
        telefone = dados.get('telefone')
        horario = dados.get('horario')
        produto = dados.get('prod')
        qtd = dados.get('qtd')
        obs = dados.get('obs')
        data = dados.get('data')

        # Validação
        if not nome or not telefone or not horario or not produto or not qtd:

            return jsonify({
                "error": "Campos obrigatórios não preenchidos."
            }), 400

        # Insert no Supabase
        response = supabase.table("rsv_031assados").insert({
            "nome": nome,
            "telefone": telefone,
            "previsao": horario,
            "produto": produto,
            "qtd": qtd,
            "data": data,
            "observacao": obs
        }).execute()

        print("Reserva salva com sucesso!")

        return jsonify({
            "message": "Reserva realizada com sucesso!",
            "data": response.data
        }), 201

    except Exception as e:

        print("Erro:", e)

        return jsonify({
            "error": str(e)
        }), 500


