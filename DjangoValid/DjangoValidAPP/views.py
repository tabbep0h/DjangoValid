from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm,SignForm

def index(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            return HttpResponse(f"""<p style="font-family:Helvetica">{name}, поздравляю с регистрацией!</p>
            <p style="font-family:Helvetica">Указанные вами данные:<br>
            Имя - {name}<br>
            Email - {email}<br>
            Пароль - {password}</p>""")
    return render(request, "index.html", {"form": form})
def sign(request):
    formsign = SignForm()
    if request.method == "POST":
        formsign = SignForm(request.POST)
        if formsign.is_valid():
            email = formsign.cleaned_data["email1"]
            password = formsign.cleaned_data["password1"]
            if email == "User1" and password == "12345678":
               return HttpResponse(f"""<p style="font-family:Helvetica">Поздравляю с успешным входом</p>""")
            else:
               return redirect("http://127.0.0.1:8000/reg/")
    return render(request, "sign.html", {"form1": formsign})
