from django.http import JsonResponse
from django.shortcuts import render
from .models import Bamako, Gao, Kidal, Koulikoro, Mopti, Ségou, Sikasso, Timbuktu, Kayes

def afficher_carte(request):
    return render(request, 'index.html')

def get_region_data(request):
    region_name = request.GET.get('region')
    region_model = None
    
    # Trouver le modèle de région approprié en fonction du nom de la région
    if region_name == 'Bamako':
        region_model = Bamako
    elif region_name == 'Gao':
        region_model = Gao
    elif region_name == 'Kidal':
        region_model = Kidal
    elif region_name == 'Koulikoro':
        region_model = Koulikoro
    elif region_name == 'Mopti':
        region_model = Mopti
    elif region_name == 'Ségou':
        region_model = Ségou
    elif region_name == 'Sikasso':
        region_model = Sikasso
    elif region_name == 'Timbuktu':
        region_model = Timbuktu
    elif region_name == 'Kayes':
        region_model = Kayes

    if region_model:
        # regions = region_model.objects.all()  # Sélectionner toutes les instances
        # data = [{'habitats': region.habitats, 'image': region.image} for region in regions]
        # return JsonResponse({'data': data})
        regions = region_model.objects.all()  # Sélectionner toutes les instances
        habitats = [region.habitats for region in regions]
        data = {'habitats': habitats}
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Région non trouvée'})
