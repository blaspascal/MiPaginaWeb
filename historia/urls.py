from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('institucion', views.institucion, name='institucion'),
    path('mision',views.mision, name='mision'),
    path('vision',views.vision, name='vision'),
    path('historia',views.historia, name='historia'),
    path('servicios',views.servicios, name='servicios'),
    path('contactanos',views.contactanos, name='contactanos'),
    path('fotos', views.fotos, name='fotos'),
    path('autores', views.autores, name='autores'),

    path('registros/crear', views.crear, name='crear'),
    path('registros/editar', views.editar, name='editar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)