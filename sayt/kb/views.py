from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Report, Period, Satrlar

report = Report.objects.all()



def view_satrlar(request, xisobot, davr):
    satr = Satrlar.objects.filter(period_id = davr)
    context = {
        'satr': satr,
        'report': report,
        'xisobot': xisobot,
        'davr': davr,
    }
    return render(request, template_name='kb/satr_ruyxat.html', context=context)


# @login_required
def index(request):

    contex = {
        'report': report,
        'title': 'Ishbilarmonlik boshqarmasi',
        'header': 'Ishbilarmonlik muhiti kuzatuvlari va tadbirkorlikni rivojlantirish statistikasi boshqarmasi',
        'boshqarma': "Tadbirkorlik statistikasi bo`yicha yig`ma tahliliy axborotlarni shakllantirish bo`limi"
    }

    return render(request, 'kb/index.html', context=contex)


def view_xisobot(request, ids):

    xisobot = Period.objects.filter(report=ids)


    context = {
        'report': report,
        'xisobot': xisobot,
    }
    return render(request, template_name='kb/xisobot_ruyxat.html', context=context,)



def logout(request):
    return render(request, 'logout.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Перенаправление на другую страницу после входа
            return redirect('home')
        else:
            # Обработка неверных учетных данных
            return render(request, 'kb/login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'kb/login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу после регистрации
    else:
        form = UserCreationForm()
    return render(request, 'kb/signup.html', {'form': form})

