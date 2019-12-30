from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from .views import password_view
from accounts.views import register_page, login_page
from app.views import MessageCreateView  # , MessageDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', password_view, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page, name='register'),
    path('create/', MessageCreateView.as_view(), name='create'),
    path('thank-you/', TemplateView.as_view(template_name="thank-you.html"), name='thank-you'),
    # path('delete/', MessageDeleteView.as_view(), name='delete'),
]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
