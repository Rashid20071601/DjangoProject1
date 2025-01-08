from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'third_task/platform.html')

def choice(request):
    buy = 'Купить'
    context = {
        'buy': buy
    }
    return render(request, 'third_task/PS5.html', context)

def cart(request):
    return render(request, 'third_task/cart.html')