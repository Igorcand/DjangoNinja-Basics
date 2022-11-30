from .models import Livro
from ninja import Schema, ModelSchema

#Pydantic
""" class LivroSchema(Schema):
    titulo: str
    descricao:str
    autor:str=None  """

class LivroSchema(ModelSchema):
    class Config:
        model = Livro
        model_fields = '__all__'
        #model_fields = ['titulo', 'descricao']


