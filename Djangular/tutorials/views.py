from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from tutorials.serializers import TutorialSerializer

from tutorials.models import Tutorial

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    return JsonResponse("hello")
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    # fieldid = request.GET.get('id', None)
    # post_data = Tutorial.objects.filter(id=fieldid)
    # serialize_data = TutorialSerializer(post_data, many=True)
    # return JsonResponse({"status": "success", "data": serialize_data.data})

    dataGET = Tutorial.objects.get()
    data_dictGET = TutorialSerializer(dataGET).data
    contextGET = {'id':data_dictGET}
    return JsonResponse(data_dictGET, safe=False)

    # try: 
    #     tutorial = Tutorial.objects.get(pk=pk) 
    #     return JsonResponse(tutorial, safe=False)
    # except Tutorial.DoesNotExist: 
    #     return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    pass
    # GET all published tutorials