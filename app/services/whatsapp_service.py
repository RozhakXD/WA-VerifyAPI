import re
from typing import Dict, Optional
from app.utils.http_client import HTTPClient
from app.models.schemas import GroupInfo, ValidationResponse

class WhatsAppService:
    WHATSAPP_LINK_PREFIX = "https://chat.whatsapp.com/"

    @classmethod
    async def validate_group_link(cls, group_link: str) -> Dict:
        if not cls._is_valid_whatsapp_link(group_link):
            return ValidationResponse(
                status="error",
                message="Invalid WhatsApp group link",
            ).model_dump()

        response = await HTTPClient.get(group_link)

        if response["status"] != 200:
            return ValidationResponse(
                status="error",
                message="WhatsApp group id not active"
            ).model_dump()

        response_html = response["text"]
        group_info = cls._extract_group_info(response_html)

        if not group_info.group_name:
            return ValidationResponse(
                status="error",
                message="WhatsApp group is not active"
            ).model_dump()

        return ValidationResponse(
            status="success",
            data={
                "link": group_link,
                "groups_info": group_info.model_dump(),
            }
        ).model_dump()

    @classmethod
    def _is_valid_whatsapp_link(cls, link: str) -> bool:
        return link.startswith(cls.WHATSAPP_LINK_PREFIX)

    @classmethod
    def _extract_group_info(cls, html: str) -> GroupInfo:
        profile_picture = cls._extract_profile_picture(html)
        group_name = cls._extract_group_name(html)
        return GroupInfo(
            profile_picture=profile_picture,
            group_name=group_name
        )

    @classmethod
    def _extract_profile_picture(cls, html: str) -> str:
        match = re.search(r'content="(https://pps\.whatsapp\.net/v/[^\s"]+)"', html)
        return match.group(1).replace('amp;', '') if match else 'null'

    @classmethod
    def _extract_group_name(cls, html: str) -> Optional[str]:
        match = re.search(r'<h3 class="_9vd5 _9scr"[^>]*>(.*?)</h3>', html)
        return match.group(1).strip() if match else None