from django.shortcuts import redirect, render
from .PersonnelFormulaire import PersonnelFormulaire
from .models import Personnel


# Create your views here.
def home(request):
    return personnel_form(request)

def personnel_liste(request):
    context = {'personnel_liste':Personnel.objects.all()}
    return render(request, "crudapp/personnel_liste.html",context)

def personnel_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PersonnelFormulaire()
        else:
            personnel = Personnel.objects.get(pk=id)
            form = PersonnelFormulaire(instance=personnel)
        return render(request, "crudapp/personnel_form.html", {'form': form})
    else:
        if id == 0:
            form = PersonnelFormulaire(request.POST)
        else:
            personnel = Personnel.objects.get(pk=id)
            form = PersonnelFormulaire(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
        return redirect("/personnel/liste")

def personnel_delete(request,id):
    personnel = Personnel.objects.get(pk=id)
    personnel.delete()
    return redirect("/personnel/liste")