import mimetypes
import os
from wsgiref.util import FileWrapper

from django.conf import settings
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from requests import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FileUploadParser
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Upload, UploadFile
from .serializers import UploadSerializer
from django.utils.encoding import smart_str


class UploadView(CreateView):
    model = Upload
    fields = ['upload_file', ]
    success_url = reverse_lazy('fileupload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all().order_by('-upload_date')
        return context




class FileUploadView(APIView):
    # parser_classes = [FileUploadParser]

    def get(self, request, *args, **kwargs):
        result = Upload.objects.all()
        serializers = UploadSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request,format=None):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class Download(APIView):
    def get(self,request, file_id):
        result = Upload.objects.get(id=file_id)
        file_path = settings.MEDIA_ROOT  + '/' + str(result.file)
        file_path = file_path
        response = HttpResponse(open(file_path, 'rb').read())
        response['Content-Type'] = 'application/text'
        response['Content-Disposition'] = 'attachment; filename=DownloadedText.txt'
        return response