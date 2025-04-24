from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.controllers.validation_controller import ValidationController

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(Config)

    @app.route('/api/validate', methods=["POST"])
    async def validate():
        return await ValidationController.validate()

    return app