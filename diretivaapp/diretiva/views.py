from .models import Diretiva
from .serializers import DiretivaSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework import renderers


class DiretivaList(generics.ListCreateAPIView):
    queryset = Diretiva.objects.all()
    serializer_class = DiretivaSerializer


class DiretivaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diretiva.objects.all()
    serializer_class = DiretivaSerializer





# FUNCTION BASED API

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Diretiva
# from .serializers import DiretivaSerializer
#
#
# @api_view(['GET', 'POST'])
# def diretiva_list(request, format=None):
#     if request.method == 'GET':
#         diretivas = Diretiva.objects.all()
#         serializer = DiretivaSerializer(diretivas, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = DiretivaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def diretiva_detail(request, pk, format=None):
#     try:
#         diretiva = Diretiva.objects.get(pk=pk)
#     except Diretiva.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = DiretivaSerializer(diretiva)
#         return Response(data=serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = DiretivaSerializer(diretiva, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         diretiva.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





# OLD VERSION

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from .models import Diretiva
# from .serializers import DiretivaSerializer
#
#
# @csrf_exempt
# def diretiva_list(request):
#     if request.method == 'GET':
#         diretivas = Diretiva.objects.all()
#         serializer = DiretivaSerializer(diretivas, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = DiretivaSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def diretiva_detail(request, pk):
#     try:
#         diretiva = Diretiva.objects.get(pk=pk)
#     except Diretiva.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         seriaizer = DiretivaSerializer(diretiva)
#         return JsonResponse(seriaizer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         seriaizer = DiretivaSerializer(diretiva, data=data)
#         if seriaizer.is_valid():
#             seriaizer.save()
#             return JsonResponse(seriaizer.data)
#     elif request.method == 'DELETE':
#         diretiva.delete()
#         return HttpResponse(status=204)
