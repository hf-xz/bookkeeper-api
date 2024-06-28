from pydantic import BaseModel, Field


class StudentSchema(BaseModel):
    fullname: str = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        json_schema_extra = {
            'example': {
                'fullname': 'John Doe',
                'course_of_study': 'Water resources engineering',
                'year': 2,
                'gpa': '3.0',
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: str | None
    course_of_study: str | None
    year: int | None
    gpa: float | None

    class Config:
        json_schema_extra = {
            'example': {
                'fullname': 'John Doe',
                'course_of_study':
                'Water resources and environmental engineering',
                'year': 4,
                'gpa': '4.0',
            }
        }


def ResponseModel(data, message):
    return {
        'data': data,
        'code': 200,
        'message': message,
    }


def ErrorResponseModel(error, code, message):
    return {'error': error, 'code': code, 'message': message}
