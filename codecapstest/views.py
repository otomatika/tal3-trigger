from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import testModel

@csrf_exempt
def index(request):
    tm = testModel.objects.first()
    if not tm:
        tm = testModel(testField='', testField2=0)
        tm.save()
    if request.method == 'POST':
        tm.testField2 = tm.testField2 + 1
        tm.save()
    context = {
        "MyVar": int(tm.testField2),
    }
    return render(request, 'index.html', context)