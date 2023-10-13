from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("Hello World!")

def add(request):
    if request.method == 'POST':
        num1 = request.POST.get('number1')
        num2 = request.POST.get('number2')
        sum = int(num1) + int(num2)
        return render(request, 'hello/addition.html', {'sum': sum})
    return render(request, 'hello/addition.html')
