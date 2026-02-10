from django.urls import path
from .views import UploadCSVAPIView, HistoryAPIView, PDFReportAPIView

urlpatterns = [
    path('upload/', UploadCSVAPIView.as_view(), name='upload-csv'),
    path('history/', HistoryAPIView.as_view(), name='history'),
    path('report/<int:dataset_id>/', PDFReportAPIView.as_view(), name='pdf-report'),
]