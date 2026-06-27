from django.db import models

# Create your models here.
class Mensagem(models.Model):
    titulo = models.CharField(max_length=120)
    autor = models.CharField(max_length=80, default="Anônimo")
    conteudo = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-criada_em"]

    def __str__(self):
        return self.titulo


# O que isso faz:

# Define uma tabela Mensagem com 3 colunas: titulo, conteudo, criada_em.
# auto_now_add=True preenche a data automaticamente quando a mensagem é criada.
# ordering = ["-criada_em"] faz as mais recentes aparecerem primeiro.
# __str__ define como a mensagem aparece no admin (pelo título).