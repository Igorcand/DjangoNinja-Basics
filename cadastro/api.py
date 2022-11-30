from ninja import NinjaAPI, UploadedFile, Router
from .models import Livro
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from .schema import LivroSchema

import orjson
from ninja.parser import Parser
from django.http import HttpRequest

class ORSJONParser(Parser):
    def parser_body(self, request: HttpRequest):
        return orjson.loads(request.body)

api = NinjaAPI(parser=ORSJONParser())
router = Router()

@router.get('livro/')
def listar(request):
    livros = Livro.objects.all()

    response = [{'id': i.id, 'titulo': i.titulo, 'descricao': i.descricao, 'autor': i.autor} for i in livros]
    return response

@router.get('livro/{int:id}')
def listar_livro(request, id: int):
    livro = get_object_or_404(Livro, id=id)
    return model_to_dict(livro)

@router.get('livro_consulta/')
def listar_consulta(request, id:int=1):
    livro = get_object_or_404(Livro, id=id)
    return model_to_dict(livro)


#type rints
from typing import List
#livro:List[LivroSchema]


@router.post('livro', response=LivroSchema)
def livro_criar(request, livro:LivroSchema):
    livro = livro.dict()
    livro = Livro(**livro)
    livro.save()
    return livro

@router.post('file')
def file_upload(request, file: UploadedFile):
    print(file.size)
    return 1
