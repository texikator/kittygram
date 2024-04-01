from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.response import Response

from .models import Cat
from .serializers import CatSerializer


class CatList(ListCreateAPIView):

    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatDetail(RetrieveDestroyAPIView):
    
    queryset = Cat.objects.all()
    serializer_class = CatSerializer




# class APICat(APIView):

#     def get(self, request):

#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):

#         serializer = CatSerializer(request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)


# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def cat_detail(request, pk):
#     try:
#         cat = Cat.objects.get(pk=pk)
#     except ObjectDoesNotExist:
#         print('dfg')
#         return Response(status=status.HTTP_204_NO_CONTENT)
   
#     if request.method in ['PUT', 'PATCH']:
#         serializer = CatSerializer(cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         cat.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     serializer = CatSerializer(cat)
#     return Response(serializer.data, status=status.HTTP_200_OK)
