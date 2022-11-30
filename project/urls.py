from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from cadastro.api import router as cadastro_router

import orjson
from ninja.parser import Parser
from django.http import HttpRequest

class ORSJONParser(Parser):
    def parser_body(self, request: HttpRequest):
        return orjson.loads(request.body)

api = NinjaAPI(parser=ORSJONParser())

api.add_router("/cadastro/", cadastro_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
