from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    

# Create your views here.
