from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """регистрирует нового пользователя."""
    if request.method != 'POST':
        """Выводим пустую форму регистрации."""
        form = UserCreationForm()
    else:
        """Обработка заполненной формы."""
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            """Выполнение входа и перенаправление на домашнюю страницу."""
            login(request, new_user)
            return redirect('blogs:index')

    """Выыести пустую или недействительную форму."""
    context = {'form': form}
    return render(request, 'users/register.html', context)
