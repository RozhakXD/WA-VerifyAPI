from app import  create_app
import asyncio
from aiohttp import web

app = create_app()

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])