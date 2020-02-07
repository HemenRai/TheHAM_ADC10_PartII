from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from jobapp.models import Company
import json

# Create your views here.
@csrf_exempt
def view_get_post_company(request):
    print("What's the request => ",request.method)
    if request.method=="GET":
        companies = Company.objects.all()
        print("Queryset objects => ",companies)
        list_of_companies = list(companies.values("companyName","companyAddress","companyContactNo"))
        print("List of Company objects => ",list_of_companies)
        dictionary_name = {
            "companies": list_of_companies
        }
        return JsonResponse(dictionary_name)

    elif request.method == "POST":
        print("Request body content => ",request.body)
        print("Request body type => ",type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents =>",python_dictionary_object)
        print("Python dictionary type =>",type(python_dictionary_object))
        print(python_dictionary_object['companyName'])
        print(python_dictionary_object['companyAddress'])
        print(python_dictionary_object['companyContactNo'])
        Company.objects.create(companyName=python_dictionary_object['companyName'],companyAddress=python_dictionary_object['companyAddress'],companyContactNo=python_dictionary_object['companyContactNo'])
        return JsonResponse({
            "message": "Successfully posted!!"
        })
    else:
        return HttpResponse("Other Http verbs testing")