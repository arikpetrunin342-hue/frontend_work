from django.shortcuts import render

def home_view(request):
    products = [
        {'name': 'Товар 1', 'price': 100},
        {'name': 'Товар 2', 'price': 250},
        {'name': 'Товар 3', 'price': 75},
    ]
    return render(request, 'home.html', {'products': products})

def contacts_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'contacts.html')
