from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'fourth_task/platform.html')

def choice(request):
    context = {
        'buy': 'Купить',
        'playstation': ['Playstation 5', 'Playstation 5 Slim', 'Playstation 5 Pro']
    }
    return render(request, 'fourth_task/PS5.html', context)

def cart(request):
    return render(request, 'fourth_task/cart.html')