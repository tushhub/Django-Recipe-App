from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('index/', views.index),
    # path('cars/', views.All_Carlist,name='All_Carlist'),
    path('', views.Recipe_view,name='Recipe'),
    path('show/', views.show_view, name='show_view'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
    path('update/<int:recipe_id>/', views.update_recipe, name='update_recipe'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
