from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required




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
@login_required
def index(request):
    contex = {
        'title': 'Ishbilarmonlik boshqarmasi',
        'header': 'Ishbilarmonlik muhiti kuzatuvlari va tadbirkorlikni rivojlantirish statistikasi boshqarmasi',
        'boshqarma': "Tadbirkorlik statistikasi bo`yicha yig`ma tahliliy axborotlarni shakllantirish bo`limi"
    }
    return render(request, 'kb/index.html', context=contex)
