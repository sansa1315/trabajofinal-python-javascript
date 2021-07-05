from .models import Categorias

def menu(request):
    categorias = Categorias.objects.all()
    return {'categorias': categorias}
