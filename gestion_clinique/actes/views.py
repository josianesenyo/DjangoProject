from django.shortcuts import render, redirect, get_object_or_404
from .models import Acte
from .forms import ActeForm
# Create your views here.


def liste_actes(request):
    actes = Acte.objects.all()
    return render(request, 'actes/liste_actes.html', {'actes': actes})

def ajouter_acte(request):
    if request.method == 'POST':
        form = ActeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_actes')
    else:
        form = ActeForm()
    return render(request, 'actes/ajouter_acte.html', {'form': form})

def modifier_acte(request, acte_id):
    acte = get_object_or_404(Acte, id=acte_id)
    if request.method == 'POST':
        form = ActeForm(request.POST, instance=acte)
        if form.is_valid():
            form.save()
            return redirect('liste_actes')
    else:
        form = ActeForm(instance=acte)
    return render(request, 'actes/modifier_acte.html', {'form': form})

def supprimer_acte(request, acte_id):
    acte = get_object_or_404(Acte, id=acte_id)
    if request.method == 'POST':
        acte.delete()
        return redirect('liste_actes')
    return render(request, 'actes/supprimer_acte.html', {'acte': acte})
