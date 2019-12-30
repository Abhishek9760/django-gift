from django.shortcuts import render, redirect

from app.models import Message
from app.forms import AuthForm


def home(request):
    return render(request, 'index.html', {})


def password_view(request):
    form = AuthForm()
    auth = False
    msg_obj = None
    gf = False
    if request.method == "POST":
        form = AuthForm(request.POST or None)
        if form.is_valid():
            auth = False
            name = form.cleaned_data.get('name')
            password = form.cleaned_data.get('password')
            obj = Message.objects.all().filter(name__icontains=name, password__iexact=password)
            if obj.exists():
                auth = True
                msg_obj = obj.first()
                if "amruta" in msg_obj.name.lower():
                    gf = True
                return render(request, 'index.html',
                              {'form': form, 'msg': msg_obj, 'auth': auth, 'gf': gf})
        else:
            form = AuthForm()
    return render(request, 'index.html', {'form': form, 'msg': msg_obj, 'auth': auth, 'gf': gf})


