from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View


def user_profile(request):  
    return JsonResponse(
        {
        'first':'Jay',
        'first':'jay@email.com',
        'phone_number':'0446677'

        }      
    )

# Create your views here.


class QueryView(View):
    def get(self,request):
        return JsonResponse({"result":[{"id":1,"title":"Adama declined Val shots"},
                             {"id":2,"title":"Samson declined Val shots"}]})
    
    def post(self,request):
        return JsonResponse({"status":"ok"})