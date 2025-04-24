from flask import request, jsonify
from app.services.whatsapp_service import WhatsAppService
from app.models.schemas import ValidationResponse

class ValidationController:
    @staticmethod
    async def validate():
        data = request.get_json()
        group_link = data.get('link', '').strip()

        if not group_link:
            return jsonify({
                "status": "error",
                "message": "Link parameter is required"
            }), 400

        result = await WhatsAppService.validate_group_link(group_link)
        return jsonify(result)