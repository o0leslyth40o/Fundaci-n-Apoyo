from django.urls import URLPattern, path
from .views import home, crear_cuenta


URLPatterns = [
    path('', home, name="home"),
    path('', crear_cuenta, name="creacuenta"),
]