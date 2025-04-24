import pytest
from app.services.whatsapp_service import WhatsAppService

@pytest.mark.asyncio
async def test_validate_group_link():
    result = await WhatsAppService.validate_group_link("https://invalid.com")
    assert  result["status"] == "error"

    result = await WhatsAppService.validate_group_link("ttps://chat.whatsapp.com/INVALID")
    assert result["status"] == "error"