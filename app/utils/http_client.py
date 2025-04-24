import aiohttp
from app.config import Config

class HTTPClient:
    @staticmethod
    async def get(url: str, headers: dict = None):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers or Config.WHATSAPP_HEADERS) as response:
                return {
                    "status": response.status,
                    "text": await response.text(),
                    "headers": dict(response.headers)
                }