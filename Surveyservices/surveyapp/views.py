from django.shortcuts import render # type: ignore

# View for the home page
def home(request):
    return render(request, 'index.html')

# View for the upload documents page
def upload(request):
    return render(request, 'upload.html')

# View for the map page
def map(request):
    return render(request, 'map.html')

# View for the find surveyors page
def services(request):
    return render(request, 'services.html')

# View for the contact page
def contact(request):
    return render(request, 'contact.html')

# View for the find surveyors page
def login(request):
    return render(request, 'login.html')

# View for the contact page
def signup(request):
    return render(request, 'register.html')