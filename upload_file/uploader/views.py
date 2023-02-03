import os
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from requests import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Upload, UploadFile
from .serializers import UploadSerializer
from rest_framework.decorators import action


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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @action(detail=False, methods=['get'])
    def get(self, request, *args, **kwargs):
        result = Upload.objects.all()
        serializers = UploadSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    @action(detail=False, methods=['post'])
    def post(self, request,format=None):
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class Download(APIView):
    def get(self,request, file_id):
        result = Upload.objects.filter(id=file_id)
        if not result:
            return Response({"status": "invalid PK"}, status=status.HTTP_400_BAD_REQUEST)
        file_path = settings.MEDIA_ROOT  + '/' + str(result.file)
        file_path = file_path
        response = HttpResponse(open(file_path, 'rb').read())
        response['Content-Type'] = 'application/text'
        response['Content-Disposition'] = 'attachment; filename=DownloadedText.txt'
        return response