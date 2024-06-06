

# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Test
from django.core import serializers

# def accueil_test(request):
#     return render(request, 'accueil.html')



# def ajouter_test(request):
#     if request.method == 'POST':
#         nom = request.POST.get('nom')
#         description = request.POST.get('description')
#         test = Test(nom=nom, description=description)
#         test.save()
#         return redirect('liste_tests') # Vous devrez définir cette vue séparément
#     return render(request, 'myapp/ajouter_test.html')




def render_personne(request):
    return render(request, 'myapp/ajouter_test.html')

# def ajouter_test(request):
#     if request.method == 'GET':
#         nom = request.POST.get('nom')
#         description = request.POST.get('description')
#         test = Test(nom='tety', description='zefezf')
#         test.save()
#         # return redirect('liste_tests') # Vous devrez définir cette vue séparément
   



def get_all_data(request):
    if request.method == 'GET':
        tests = Test.objects.all()
        tests_data = []
        for test in tests:
            test_data = {
                'nom': test.nom,
                'description': test.description
            }
            tests_data.append(test_data)
        return JsonResponse(tests_data, safe=False)