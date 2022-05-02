from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    # Path to access the admin page
    path('admin/', admin.site.urls),
    # Path to render the home page
    path('', views.frontend, name='frontend'),
    # Path Login/Logout
    path('login/', include('django.contrib.auth.urls')),

    # ================================================================
    # BACKEND SECTION
    # ================================================================
    # path to access the backend page
    path('backend/',      views.backend,        name='backend'),
    # browser url  |  function in view.py |  url inside html file
    # path to add patient
    path('add_patient', views.add_patient, name='add_patient'),
    # Path to delete Patient
    path('delete_patient/<str:patient_id>',
         views.delete_patient, name="delete_patient"),
    # Path to access the Patient individualy
    path('patient/<str:patient_id>',
         views.patient, name="patient"),
    # path to edit a patient
    path('edit_patient', views.edit_patient, name='edit_patient'),

    # ================================================================
    # SUPPORT SECTION
    # ================================================================
    # path to page support
    path('support', views.support, name='support'),
]
