from django.urls import path
from apps.tool_csv_processor.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("tools/csv-processor/", csv_processor, name="tool_csv_processor"),
    path("upload-csv/", CSVUploadView.as_view(), name="upload-csv"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)