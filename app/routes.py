from flask import Blueprint, render_template, request, jsonify
from .utils.check import check_group_link

main = Blueprint('main', __name__)

@main.route('/', methods=["GET", "POST"])
async def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        group_link = request.json['link']
        response = await check_group_link(groups_link=group_link)
        return jsonify(response)

@main.route('/api/v1/whatsapp/groups/', methods=["POST"])
async def api():
    try:
        link = request.json['link']
        response = await check_group_link(groups_link=link)
        if response['status'] != 'success':
            return jsonify(
                response
            ), 400
        else:
            return jsonify(
                response
            ), 200
    except (KeyError):
       return jsonify(
            {
                'message': 'parameter \'link\' wajib ada di request body',
                'status': 'error'
            }
        ), 400
    except Exception:
        return jsonify(
            {
                'message': 'terjadi kesalahan pada server',
                'status': 'error'
            }
        ), 500