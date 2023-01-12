from django.urls import path

from angajati import views

app_name = 'angajati'

urlpatterns = [
    path('', views.AngajatiView.as_view(), name='lista_angajati'),
    path('adaugare/', views.CreateAngajatiView.as_view(), name='adaugare'),
    path('<int:pk>/update/', views.UpdateAngajatiView.as_view(), name='modificare'),
    path('<int:pk>/delete', views.delete_angajati, name='stergere'),
    path('<int:pk>/activate', views.activate_angajati, name='activare'),
]