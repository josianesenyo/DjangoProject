from django.shortcuts import get_object_or_404, redirect, render
from .forms import MedicamentForm
from .models import Medicament

# Create your views here.
def liste_medicaments(request):
    medicaments = Medicament.objects.all()
    return render(request, 'medicaments/liste_medicaments.html', {'medicaments': medicaments})

def ajouter_medicament(request):
    if request.method == 'POST':
        form = MedicamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_medicaments')
    else:
        form = MedicamentForm()
    return render(request, 'medicaments/ajouter_medicament.html', {'form': form})

def modifier_medicament(request, pk):
    medicament = get_object_or_404(Medicament, pk=pk)
    if request.method == 'POST':
        form = MedicamentForm(request.POST, instance=medicament)
        if form.is_valid():
            form.save()
            return redirect('liste_medicaments')
    else:
        form = MedicamentForm(instance=medicament)
    return render(request, 'medicaments/modifier_medicament.html', {'form': form})

def supprimer_medicament(request, pk):
    medicament = get_object_or_404(Medicament, pk=pk)
    if request.method == 'POST':
        medicament.delete()
        return redirect('liste_medicaments')
    return render(request, 'medicaments/supprimer_medicament.html', {'medicament': medicament})
