from django.shortcuts import render
from .models import Mensagem
# Create your views here.


def index(request):
    mensagens = Mensagem.objects.all()
    return render(request, "home/index.html", {"mensagens": mensagens})