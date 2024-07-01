from pydantic import BaseModel, Field

from utils.string import snake_to_camel


class TurnoverSchema(BaseModel):
    date: str = Field(...)
    ti_cai: float = Field(..., ge=0)
    wai_dian: float = Field(..., ge=0)
    fu_cai: float = Field(..., ge=0)
    one_percent: float = Field(..., ge=0)

    class Config:
        alias_generator = snake_to_camel
        populate_by_name = True
        json_schema_extra = {
            'example': {
                'date': '2021-01-01',
                'tiCai': 100,
                'waiDian': 200,
                'fuCai': 300,
                'onePercent': 100,
            }
        }


class UpdateTurnoverModel(BaseModel):
    ti_cai: float | None
    wai_dian: float | None
    fu_cai: float | None
    one_percent: float | None

    class Config:
        alias_generator = snake_to_camel
        populate_by_name = True
        json_schema_extra = {
            'example': {
                'tiCai': 100,
                'waiDian': 200,
                'fuCai': 300,
                'onePercent': 200,
            }
        }
