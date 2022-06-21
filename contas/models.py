from django.db import models

# Create your models here.
class Categoria(models.Model):
    '''
    DEFINE A CATEGORIA DO CUSTO
    '''
    nome = models.CharField(max_length = 100, blank = False)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Categorias'
    
    def __str__(self) -> str:
        return self.nome

class Transacao(models.Model):
    '''
    DEFINE OS DADOS DETRANSAÇÃO
    '''
    data = models.DateTimeField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, null = False)
    valor = models.DecimalField(max_digits = 9, decimal_places=2, null = False)
    descricao = models.CharField(max_length = 100, null = False)
    observacoes = models.TextField(max_length = 500, null = True, blank = True)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name_plural = 'Transações'
    
    def __str__(self) -> str:
        return self.descricao