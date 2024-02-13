from django.urls import path
from .viewCSV import ShowCsvInTemplate
from .viewDB import ViewFromDB
from .viewJSON import ShowJSONInTemplate

urlpatterns = [
    path("from_csv_file", ShowCsvInTemplate.as_view(), name="from_csv_file"),
    path("from_sql_db", ViewFromDB.as_view(), name="from_sql_db"),
    path("from_json_file", ShowJSONInTemplate.as_view(), name="from_json_file"),
]
