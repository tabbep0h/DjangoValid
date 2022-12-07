from django import forms

class UserForm(forms.Form):
    name = forms.CharField(min_length=4,widget = forms.TextInput(attrs = {"class":"name__input input","placeholder":"Имя"}), required =True,label = "Введите имя")
    email = forms.EmailField(widget = forms.TextInput(attrs = {"class":"email__input input","type":"email","placeholder":"Email"}), required =True,label = "Введите Email")
    password = forms.CharField(min_length=8,widget = forms.TextInput(attrs = {"class":"password__input input","type":"password","placeholder":"Пароль"}), required = True,label = "Введите пароль")

class SignForm(forms.Form):
    email1 = forms.CharField(
        widget=forms.TextInput(attrs={"class": "email__input input", "type": "text", "placeholder": "Email"}),
        required=True, label="Введите Email")
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={"class": "password__input input", "type": "password", "placeholder": "Пароль"}),
        required=True, label="Введите пароль")
