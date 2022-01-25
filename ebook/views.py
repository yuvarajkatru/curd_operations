from django.shortcuts import render
from .models import ebook
from .serializer import EbookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from user.views import auth



class Create_ebook(APIView):
    def post(self, request):
        res=auth(token)
        serializer = EbookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request):
        token = request.COOKIES.get('jwt')
        res=auth(token)
        if not res:
            return Response({"data":"please login"})
        book = ebook.objects.all()
        serializer=EbookSerializer(book, many=True)
        return Response(serializer.data)

class Update_ebook(APIView):
    def get_object(self,pk):
        return ebook.objects.get(pk=pk)

    def get(self, request, pk):
        token = request.COOKIES.get('jwt')
        res=auth(token)
        if not res:
            return Response({"data":"please login"})
        book = self.get_object(pk)
        serializer = EbookSerializer(book)
        return Response(serializer.data)

    def put(self,request, pk):
        token = request.COOKIES.get('jwt')
        res=auth(token)
        if not res:
            return Response({"data":"please login"})
        serializer = EbookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Saved')

    def patch(self, request, pk):
        token = request.COOKIES.get('jwt')
        res=auth(token)
        if not res:
            return Response({"data":"please login"})
        book = self.get_object(pk)
        serializer = EbookSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('Data Saved')

    def delete(self,request,pk):
        token = request.COOKIES.get('jwt')
        res=auth(token)
        if not res:
            return Response({"data":"please login"})
        book = self.get_object(pk)
        book.delete()
        return Response('Deleted')
