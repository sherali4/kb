from django.shortcuts import render, get_object_or_404

# Create your views here.







from django.http import JsonResponse
from .forms import FileUploadForm

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            tr = request.POST.get('innx')
            instance = get_object_or_404(Baza, pk=tr)
            instance.yopilgan = 1
            instance.save()
            return JsonResponse({'message': 'File uploaded successfully.'})
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)












from django.shortcuts import render, redirect
from .models import Baza

from .forms import BazaForm

def forma(request):

    baza = Baza.objects.exclude(yopilgan = 1)
    context = {
        'baza': baza,
    }
    return render(request, 'jarima/forma.html', context=context)




def update(request, pk):
    # Получение объекта модели по первичному ключу
    my_model_obj = Baza.objects.get(pk=pk)

    # Новые значения для обновления
    new_boolean_value = True
    new_other_value = "Updated value"

    # Обновление данных объекта модели
    my_model_obj.okpo = new_boolean_value
    my_model_obj.inn = new_other_value
    my_model_obj.save()

    return redirect('success')  # Редирект на другую страницу после успешного обновления








def success(request):
    return render(request, 'jarima/success.html')




def index(request):
    baza = Baza.objects.exclude(yopilgan=1)
    context = {
        'baza': baza,
    }

    return render(request, 'jarima/index.html', context=context)






