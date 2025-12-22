from pydantic import BaseModel, ConfigDict


class RelationItem(BaseModel):
    relation_id: int
    student_id: int
    student_name: str
    grade: int
    tutor_inn: str

    model_config = ConfigDict(from_attributes=True)
