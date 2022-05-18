from django.shortcuts import render, redirect
from .forms import NewForm
from .models import Http
from django.contrib import messages

# Imports for random url
import random
import string


def shortener(request):
    if request.method == 'POST':
        form  = NewForm(request.POST)

        if form.is_valid():
            shortened = ''.join(random.choice(string.ascii_letters) for i in range (5))  
            original = form.cleaned_data['original']
            shortened_url = Http(original=original,shortened=shortened)
            shortened_url.save()

            messages.info(request, 'Here is your URL: ' + shortened_url.shortened)

            return redirect('/')
    else:
        form = NewForm()
        
    data = Http.objects.all()

    context = {'form': form, 'data': data}
    return render(request, "home.html", context)

# Errors
def not_found_404(request, exception):
    data={'err': exception}
    return render(request, '404.html', data)

def server_error_500(request):
    return render(request, '500.html')