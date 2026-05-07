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
    




# @home_route.route('/insert_finpATIVOS', methods=['POST'])
# def insert_finpativos():
#     try:
#         dados = request.json
#         print("Dados recebidos:", dados)
#         # Extrai mês e ano da data_comp e data_deb

#         # Insere os dados na tabela finp_ativos
#         response = supabase.table("finp_ativos").insert({
#             "ticket": dados['ticket'],
#             "ativo": dados['ativo'],
#             "tipo": dados['tipoativo'],
#             "segmento": dados['segmento'],
#             "cotacao": dados['cotacao'],
#             "carteira": dados['switchTexto']
#         }).execute()
#         print("Dados enviados para inserção:", dados)
#         return jsonify({"message": "Cadastro realizado com sucesso!", "data": response.data}), 201

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


