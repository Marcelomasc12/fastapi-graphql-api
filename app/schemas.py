from pydantic import BaseModel, Field

#Validar os dados que chegam    
class PostCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    content: str = Field(min_length=5, max_length=500)


class PostUpdate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    content: str = Field(min_length=5, max_length=500)