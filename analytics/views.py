from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, FileResponse, Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status

from django.core.files.storage import default_storage

from .utils import analyze_csv
from .services import save_dataset
from .services import get_recent_datasets

import os
import tempfile

from .models import Dataset
from .pdf_utils import generate_pdf


class UploadCSVAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        if 'file' not in request.FILES:
            return Response(
                {"error": "CSV file not provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        uploaded_file = request.FILES['file']

        # Save file temporarily
        file_path = default_storage.save(uploaded_file.name, uploaded_file)

        try:
            analysis_result = analyze_csv(default_storage.path(file_path))
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Save history (last 5 logic inside this)
        save_dataset(
            file_name=uploaded_file.name,
            summary=analysis_result
        )

        return Response(
            analysis_result,
            status=status.HTTP_201_CREATED
        )

class HistoryAPIView(APIView):

    def get(self, request):
        datasets = get_recent_datasets()

        data = []
        for ds in datasets:
            data.append({
                "id": ds.id,
                "file_name": ds.file_name,
                "uploaded_at": ds.uploaded_at,
                "summary": ds.summary
            })

        return Response(data, status=status.HTTP_200_OK)

class PDFReportAPIView(APIView):

    def get(self, request, dataset_id):
        try:
            dataset = Dataset.objects.get(id=dataset_id)
        except Dataset.DoesNotExist:
            raise Http404("Dataset not found")

        # Create temporary PDF file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        temp_file_path = temp_file.name
        temp_file.close()

        # Generate PDF
        generate_pdf(
            analysis_result=dataset.summary,
            output_path=temp_file_path,
            dataset_name=dataset.file_name
        )

        # Return file as response
        response = FileResponse(
            open(temp_file_path, "rb"),
            content_type="application/pdf"
        )
        response["Content-Disposition"] = (
            f'attachment; filename="report_{dataset.id}.pdf"'
        )

        return response
