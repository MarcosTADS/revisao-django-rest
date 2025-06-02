from django.db import models

class Produto(models.Model):
    
    UNIDADES_DE_MEDIDA = {
        "lt":"Litro",
        "cx":"Caixa",
        "und":"Unidade"
    }

    CATEGORIA = {
        "comp_eletron":"Componentes Eletrônicos",
        "resinas":"Resinas",
        "filamento":"Filamento para impressão"
    }

    descricao = models.CharField(max_length=50)
    cod = models.CharField(max_length=15)
    und_medida = models.CharField(max_length=15, choices=UNIDADES_DE_MEDIDA)
    categoria = models.CharField(max_length=30, choices=CATEGORIA)
    qtd_estoque = models.IntegerField()

    def __str__(self):
        return f'Descrição: {self.descricao} - Unidade de medida: {self.und_medida}, Categoria: {self.categoria}'