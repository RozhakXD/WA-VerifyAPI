from pydantic import BaseModel

class GroupInfo(BaseModel):
    profile_picture: str
    group_name: str

class ValidationResponse(BaseModel):
    status: str
    data: dict | None = None
    message: str | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "data": {
                    "link": "https://chat.whatsapp.com/EXAMPLE",
                    "groups_info": {
                        "profile_picture": "https://pps.whatsapp.net/v/EXAMPLE",
                        "group_name": "Example Group"
                    }
                }
            }
        }