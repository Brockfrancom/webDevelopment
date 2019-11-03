from django.http import HttpResponse
from .models import Unitconv
from django.http import JsonResponse

def index(request):
    return HttpResponse("Initialize the database by going to init/")

def convert(request):
    try:
        unitsOut = request.GET.get('to')
        unitsIn = request.GET.get('from')
        value = request.GET.get('value')
        value = float(value) 
        
        conv = Unitconv.objects.get(toUnits=unitsOut, fromUnits=unitsIn)
        returnValue = value * conv.conversion

        context = {'value':returnValue,
                   'units':conv.toUnits}
        response = JsonResponse(context)
        response['Access-Control-Allow-Origin'] = '*' 
        return response
    except:
        context = {'error': "Invalid unit conversion request"}
        response = JsonResponse(context)
        response['Access-Control-Allow-Origin'] = '*' 
        return response

# This came from https://www.metric-conversions.org/weight/pounds-to-troy-ounces.htm
def init(request):
    for u in Unitconv.objects.all():
        u.delete()    
    U = Unitconv()
    U.conversion = 14.583 
    U.fromUnits = 'lbs'
    U.toUnits = 't_oz'
    U.save()
    return HttpResponse("Database initialized.")
